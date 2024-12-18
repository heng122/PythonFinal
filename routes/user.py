from app import app, render_template, request, IMAGE_DIR
import os
import time
from sqlalchemy import create_engine, text
import psycopg2
from helpers import file_upload

try:
    engine = create_engine("postgresql+psycopg2://postgres:@localhost:5432/pos_system")

    connection = engine.connect()
except Exception as e:
    print(e)


@app.route('/user')
def user():
    module = 'user'
    return render_template('user/user.html', module=module)


@app.get('/userList')
def userList():
    result = connection.execute(text("SELECT * FROM user"))
    data = result.fetchall()
    connection.commit()
    user_list = []
    for item in data:
        user_list.append(
            {
                "id": item[0],
                "name": item[1],
                "gender": item[2],
                "phone": item[3],
                "email": item[4],
                "address": item[5],
                "image": item[6],
            }
        )
    print(user_list)
    return user_list


@app.post('/saveRecord')
def saveRecord():
    form = request.get_json()
    name = form.get('name')
    gender = form.get('gender')
    phone = form.get('phone')
    email = form.get('email')
    address = form.get('address')

    base64_string = request.json['image']
    image_path = os.path.join(IMAGE_DIR)
    image_name = f"{time.time()}.png"
    file = file_upload.upload(base64_string, image_path, image_name)
    result = connection.execute(text(f"INSERT INTO `user` VALUES(null,'{name}', '{gender}', '{phone}', '{email}', '{address}', '{image_name}')"))
    connection.commit()
    return f"{name} - {gender} - {phone} - {email} - {address}"


@app.post('/updateRecord')
def updateRecord():
    form = request.get_json()
    id = form.get('id')
    name = form.get('name')
    gender = form.get('gender')
    phone = form.get('phone')
    email = form.get('email')
    address = form.get('address')

    result = connection.execute(text(f"UPDATE `user` SET NAME = '{name}',gender = '{gender}',phone = '{phone}',email = '{email}',address = '{address}' WHERE id = {id}"))
    connection.commit()
    print(result)
    return f"{name} - {gender} - {phone} - {email} - {address}"


@app.post('/deleteRecord')
def deleteRecord():
    form = request.get_json()
    id = form.get('id')
    result = connection.execute(text(f"Delete From `user` WHERE id = {id}"))
    connection.commit()
    return f"Delete successfully"

