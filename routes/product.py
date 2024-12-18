from app import app, render_template, request
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import jsonify

# Create engine and session
engine = create_engine("postgresql+psycopg2://postgres:@localhost:5432/pos_system")
Session = scoped_session(sessionmaker(bind=engine))

@app.route('/product')
def product():
    return render_template('product/product.html')

@app.get('/productList')
def productList():
    query = """
    SELECT p.id, p.name, p.cost, p.price, 
           c.name AS category_name, 
           u.name AS unit_name, 
           b.name AS brand_name, 
           t.name AS tag_name
    FROM product p
    LEFT JOIN category c ON p.category_id = c.id
    LEFT JOIN unit u ON p.unit_id = u.id
    LEFT JOIN brand b ON p.brand_id = b.id
    LEFT JOIN tag t ON p.tag_id = t.id;
    """
    with engine.connect() as connection:
        result = connection.execute(text(query))
        data = result.fetchall()

    product_list = []
    for item in data:
        product_list.append({
            "id": item[0],
            "name": item[1],
            "cost": item[2],
            "price": item[3],
            "category_name": item[4],
            "unit_name": item[5],
            "brand_name": item[6],
            "tag_name": item[7],
        })

    return jsonify(product_list)

@app.post('/saveProduct')
def saveProduct():
    form = request.get_json()
    name = form.get('name')
    cost = form.get('cost')
    price = form.get('price')
    category_id = form.get('category_id')
    unit_id = form.get('unit_id')
    brand_id = form.get('brand_id')
    tag_id = form.get('tag_id')

    query = text("""
    INSERT INTO product (name, cost, price, category_id, unit_id, brand_id, tag_id) 
    VALUES (:name, :cost, :price, :category_id, :unit_id, :brand_id, :tag_id)
    """)

    with engine.connect() as connection:
        connection.execute(query, {
            "name": name, "cost": cost, "price": price,
            "category_id": category_id, "unit_id": unit_id,
            "brand_id": brand_id, "tag_id": tag_id
        })
        connection.commit()

    return jsonify({'message': 'Product saved successfully'})

@app.post('/updateProduct')
def updateProduct():
    form = request.get_json()
    id = form.get('id')
    name = form.get('name')
    cost = form.get('cost')
    price = form.get('price')
    category_id = form.get('category_id')
    unit_id = form.get('unit_id')
    brand_id = form.get('brand_id')
    tag_id = form.get('tag_id')

    query = text("""
    UPDATE product 
    SET name = :name, cost = :cost, price = :price, 
        category_id = :category_id, unit_id = :unit_id, 
        brand_id = :brand_id, tag_id = :tag_id
    WHERE id = :id
    """)

    with engine.connect() as connection:
        connection.execute(query, {
            "id": id, "name": name, "cost": cost, "price": price,
            "category_id": category_id, "unit_id": unit_id,
            "brand_id": brand_id, "tag_id": tag_id
        })
        connection.commit()

    return jsonify({'message': 'Product updated successfully'})

@app.delete('/deleteProduct/<int:id>')
def deleteProduct(id):
    query = text("DELETE FROM product WHERE id = :id")

    with engine.connect() as connection:
        connection.execute(query, {"id": id})
        connection.commit()

    return jsonify({'message': 'Product deleted successfully'})

@app.get('/getDropdownData')
def getDropdownData():
    # Fetch dropdown data
    dropdown_data = {}

    with engine.connect() as connection:
        # Fetch categories
        category_query = "SELECT id, name FROM category;"
        category_result = connection.execute(text(category_query))
        dropdown_data['categories'] = [{"id": row[0], "name": row[1]} for row in category_result]

        # Fetch units
        unit_query = "SELECT id, name FROM unit;"
        unit_result = connection.execute(text(unit_query))
        dropdown_data['units'] = [{"id": row[0], "name": row[1]} for row in unit_result]

        # Fetch brands
        brand_query = "SELECT id, name FROM brand;"
        brand_result = connection.execute(text(brand_query))
        dropdown_data['brands'] = [{"id": row[0], "name": row[1]} for row in brand_result]

        # Fetch tags
        tag_query = "SELECT id, name FROM tag;"
        tag_result = connection.execute(text(tag_query))
        dropdown_data['tags'] = [{"id": row[0], "name": row[1]} for row in tag_result]

    return jsonify(dropdown_data)
