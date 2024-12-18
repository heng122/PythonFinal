from flask import redirect

from app import app, render_template, request
from sqlalchemy import create_engine, text

# Database connection
engine = create_engine("postgresql+psycopg2://postgres:@localhost:5432/pos_system")
connection = engine.connect()

@app.route('/categories', methods=['GET'])
def get_categories():
    result = connection.execute(text("SELECT * FROM category")).fetchall()
    return render_template('categories.html', categories=result)

@app.route('/categories', methods=['POST'])
def create_category():
    name = request.form['name']
    description = request.form.get('description')

    connection.execute(text("INSERT INTO category (name, description) VALUES (:name, :description)"),
                       {"name": name, "description": description})
    return redirect('/categories')

@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    name = request.form['name']
    description = request.form.get('description')

    connection.execute(text("UPDATE category SET name = :name, description = :description WHERE id = :id"),
                       {"name": name, "description": description, "id": category_id})
    return redirect('/categories')

@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    connection.execute(text("DELETE FROM category WHERE id = :id"), {"id": category_id})
    return redirect('/categories')

@app.route('/units', methods=['GET'])
def get_units():
    result = connection.execute(text("SELECT * FROM unit")).fetchall()
    return render_template('units.html', units=result)

@app.route('/units', methods=['POST'])
def create_unit():
    name = request.form['name']
    description = request.form.get('description')

    connection.execute(text("INSERT INTO unit (name, description) VALUES (:name, :description)"),
                       {"name": name, "description": description})
    return redirect('/units')

@app.route('/units/<int:unit_id>', methods=['PUT'])
def update_unit(unit_id):
    name = request.form['name']
    description = request.form.get('description')

    connection.execute(text("UPDATE unit SET name = :name, description = :description WHERE id = :id"),
                       {"name": name, "description": description, "id": unit_id})
    return redirect('/units')

@app.route('/units/<int:unit_id>', methods=['DELETE'])
def delete_unit(unit_id):
    connection.execute(text("DELETE FROM unit WHERE id = :id"), {"id": unit_id})
    return redirect('/units')

@app.route('/brands', methods=['GET'])
def get_brands():
    result = connection.execute(text("SELECT * FROM brand")).fetchall()
    return render_template('brands.html', brands=result)

@app.route('/brands', methods=['POST'])
def create_brand():
    name = request.form['name']
    description = request.form.get('description')

    connection.execute(text("INSERT INTO brand (name, description) VALUES (:name, :description)"),
                       {"name": name, "description": description})
    return redirect('/brands')

@app.route('/brands/<int:brand_id>', methods=['PUT'])
def update_brand(brand_id):
    name = request.form['name']
    description = request.form.get('description')

    connection.execute(text("UPDATE brand SET name = :name, description = :description WHERE id = :id"),
                       {"name": name, "description": description, "id": brand_id})
    return redirect('/brands')

@app.route('/brands/<int:brand_id>', methods=['DELETE'])
def delete_brand(brand_id):
    connection.execute(text("DELETE FROM brand WHERE id = :id"), {"id": brand_id})
    return redirect('/brands')

@app.route('/tags', methods=['GET'])
def get_tags():
    result = connection.execute(text("SELECT * FROM tag")).fetchall()
    return render_template('tags.html', tags=result)

@app.route('/tags', methods=['POST'])
def create_tag():
    name = request.form['name']
    description = request.form.get('description')

    connection.execute(text("INSERT INTO tag (name, description) VALUES (:name, :description)"),
                       {"name": name, "description": description})
    return redirect('/tags')

@app.route('/tags/<int:tag_id>', methods=['PUT'])
def update_tag(tag_id):
    name = request.form['name']
    description = request.form.get('description')

    connection.execute(text("UPDATE tag SET name = :name, description = :description WHERE id = :id"),
                       {"name": name, "description": description, "id": tag_id})
    return redirect('/tags')

@app.route('/tags/<int:tag_id>', methods=['DELETE'])
def delete_tag(tag_id):
    connection.execute(text("DELETE FROM tag WHERE id = :id"), {"id": tag_id})
    return redirect('/tags')
