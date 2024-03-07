/*******************************************************E-COMMERCE PLATFORM********************************************************/

--CREATING A DATABASE TITLED AS 'E-COMMERCE'
CREATE DATABASE ECOMMERCE;

--USING A DATABASE 'E-COMMERCE' CREATE APPROPRIATE TABLES
USE ECOMMERCE;

--CREATING TABLE CUSTOMERS
CREATE TABLE customers(
customer_id varchar(10) not null Primary Key,
c_name varchar(30),
email varchar(50),
password varchar(8)
);

--CREATING TABLE PRODUCTS
CREATE TABLE products(
product_id varchar(10) not null Primary Key,
p_name varchar(30),
price decimal(10,2),
description text,
stock_quantity int
);

--CREATING TABLE CART
CREATE TABLE cart(
cart_id varchar(10) not null Primary Key,
customer_id varchar(10) foreign key references customers(customer_id),
product_id varchar(10) foreign key references products(product_id),
quantity int);--CREATING TABLE ORDERSCREATE TABLE orders(
order_id varchar(10) not null Primary Key,
customer_id varchar(10) foreign key references customers(customer_id),
order_date date,
total_price decimal(10,2),
shipping_address text
);

--CREATING TABLE ORDER ITEMS
CREATE TABLE order_items(
order_item_id varchar(10) not null Primary Key,
order_id  varchar(10) foreign key references orders(order_id),
product_id varchar(10) foreign key references products(product_id),
item_quantity int
);
--INSERTING FIVE SAMPLE RECORDS IN THE APPROPRIATE TABLES FOR UNIT TESTING
INSERT INTO customers(customer_id,c_name,email,password)
VALUES
		('C01','Aravindh','aravindh@gmai;.com','Ara@2003'),
		('C02','Arun Kumar','arunkumar@gmail.com','aru@1234'),
		('C03','Bala','bala2003@gmail.com','bal@5678'),
		('C04','Darshan','darshan@gmail.com','dar@9012'),
		('C05','Vignesh','vignesh@gmail.com','vig@3456');

INSERT INTO products(product_id,p_name,price,description,stock_quantity)
VALUES
		('P01','Havells Fan',2000.00,'ceiling fan',50),
		('P02','Oxford Dictionary',1999.00,'Eng. to Eng.,Illustrated',15),
		('P03','Marie Gold',10.00,'perfect snack for tea',100),
		('P04','Lakme Sun Screen Lotion',275.00,'protect from UV rays',25),
		('P05','Ashirvath Atta',85.00,'purely manufactured',10);

INSERT INTO cart(cart_id,customer_id,product_id,quantity)
VALUES
		('CA1','C01','P05',5),
		('CA2','C02','P04',6),
		('CA3','C03','P01',15),
		('CA4','C04','P02',2),
		('CA5','C05','P03',25);

INSERT INTO orders(order_id,customer_id,order_date,total_price,shipping_address)
VALUES
		('OR1','C01','2024-02-29',425.00,'Adayar, Chennai'),
		('OR2','C02','2024-03-04',1650.00,'Karaikal, Puducherry'),
		('OR3','C03','2024-03-01',15000.00,'Yanam, Puducherry'),
		('OR4','C04','2024-03-02',4998.00,'Collector Office, Nagapattinam'),
		('OR5','C05','2024-02-28',250.00,'Bus Stand, Kumbakonam');

INSERT INTO order_items(order_item_id,order_id,product_id,item_quantity)
VALUES
		('IT01','OR1','P05',5),
		('IT02','OR2','P04',6),
		('IT03','OR3','P01',15),
		('IT04','OR4','P02',2),
		('IT05','OR5','P03',25);

--DISPLYING FIVE TABLES (CUSTOMERS,PRODUCTS, CART, ORDERS, ORDER_ITEMS) WITH FIVE SAMPLE RECORDS ON EACH TABLE
SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM cart;
SELECT * FROM orders;
SELECT * FROM order_items;