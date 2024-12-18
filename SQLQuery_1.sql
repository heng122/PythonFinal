 create table user
 (
     id      INTEGER not null
         primary key AUTO_INCREMENT,
     name    TEXT    not null,
     gender  TEXT,
     phone   TEXT,
     email   TEXT,
     address TEXT,
     photo   TEXT
 );


 CREATE TABLE unit (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(255) NOT NULL,
     description VARCHAR(255)
 );

 CREATE TABLE tag (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(255) NOT NULL,
     description VARCHAR(255)
 );
 
 CREATE TABLE brand (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(255) NOT NULL,
     description VARCHAR(255)
 );

 CREATE TABLE category (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(255) NOT NULL,
     description VARCHAR(255)
 );

 CREATE TABLE product (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(255) NOT NULL,
     cost DECIMAL(10, 2) NOT NULL,
     price DECIMAL(10, 2) NOT NULL,
     category_id INT,
     unit_id INT,
     brand_id INT,
     tag_id INT,
     FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE SET NULL,
     FOREIGN KEY (unit_id) REFERENCES unit(id) ON DELETE SET NULL,
     FOREIGN KEY (brand_id) REFERENCES brand(id) ON DELETE SET NULL,
     FOREIGN KEY (tag_id) REFERENCES tag(id) ON DELETE SET NULL
 );


-- Insert new categories
INSERT INTO category (name, description)
VALUES
 ('Electronics', 'Electronic devices and gadgets'),
('Fashion', 'Clothing, shoes, and accessories'),
('Home & Kitchen', 'Home appliances, kitchenware, and furniture'),
('Books', 'Books, magazines, and educational materials'),
('Beauty & Personal Care', 'Cosmetics, skincare, and personal hygiene products'),
('Sports & Outdoors', 'Sporting goods and outdoor equipment');

-- Insert new units
INSERT INTO unit (name, description)
VALUES
 ('Piece', 'Sold by piece'),
('Kilogram', 'Sold by weight in kilograms'),
('Liter', 'Sold by volume in liters'),
('Box', 'Packaged and sold by box'),
('Pair', 'Sold as a pair, such as shoes or gloves'),
('Dozen', 'Sold by the dozen');

-- Insert new brands
INSERT INTO brand (name, description)
VALUES
 ('Apple', 'Apple Inc. products'),
('Samsung', 'Samsung electronics and products'),
('Nike', 'Nike sportswear and footwear'),
('Sony', 'Sony electronic products and gaming consoles'),
('LG', 'LG home appliances and electronics'),
('Adidas', 'Adidas sports and fashion products');

-- Insert new tags
INSERT INTO tag (name, description)
VALUES
 ('Smartphone', 'Products related to smartphones'),
('Laptop', 'Products related to laptops and notebooks'),
('Tablet', 'Products related to tablets and iPads'),
('Footwear', 'Products related to shoes, sandals, and footwear'),
('Fitness', 'Products related to fitness and workout equipment'),
('Gaming', 'Products related to gaming, consoles, and accessories');


-- Insert a new product
INSERT INTO product (name, cost, price, category_id, unit_id, brand_id, tag_id)
VALUES ('iPhone 13', 700.00, 999.99,
    (SELECT id FROM category WHERE name = 'Electronics'),
    (SELECT id FROM unit WHERE name = 'Piece'),
    (SELECT id FROM brand WHERE name = 'Apple'),
    (SELECT id FROM tag WHERE name = 'Smartphone'));

SELECT * FROM product;

select * from user;

