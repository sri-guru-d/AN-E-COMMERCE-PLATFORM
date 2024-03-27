import pyodbc
from dao.OrderProcessorRepository import OrderProcessorRepository
from util import db_conn_util
import pyodbc
from exceptions import exceptions

class OrderProcessorRepositoryImpl(OrderProcessorRepository):
    def __init__(self):
        self.conn = db_conn_util.DBConnection.getConnection()

    def retrieveProductsFromCart(self, customer_id, cart_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT p.product_id, p.price, c.quantity FROM cart c JOIN products p ON c.product_id = p.product_id WHERE c.customer_id = ? AND c.cart_id = ?",
                (customer_id, cart_id))
            rows = cursor.fetchall()
            products_quantity_map = {}
            for row in rows:
                product_id = row.product_id
                price = row.price
                quantity = row.quantity
                print(f"Raw quantity for product {product_id}: {quantity}")
                try:
                    quantity = int(quantity)
                except ValueError:
                    print(f"Error converting quantity to integer for product {product_id}. Quantity value: {quantity}")
                    quantity = 0
                print(f"Processed quantity for product {product_id}: {quantity}")
                products_quantity_map[product_id] = {'price': price, 'quantity': quantity}
            return products_quantity_map
        except pyodbc.Error as ex:
            print(f"Error retrieving products from cart: {ex}")
            return None

    def createProduct(self, product):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO products (product_id,name, description, price, stock_quantity) VALUES (?,?, ?, ?, ?)",
                           (product['product_id'],product['name'], product['description'], product['price'], product['stock_quantity']))
            self.conn.commit()
            print("Product created successfully")
            return True
        except pyodbc.Error as ex:
            print(f"Error creating product: {ex}")
            return False

    def createCustomer(self, customer):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO customers (customer_id,name, email, password) VALUES (?,?, ?, ?)",
                           (customer['customer_id'],customer['name'], customer['email'], customer['password']))
            self.conn.commit()
            print("Customer created successfully")
            return True
        except pyodbc.Error as ex:
            print(f"Error creating customer: {ex}")
            return False

    def deleteProduct(self, productId):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM products WHERE product_id = ?", (productId,))
            self.conn.commit()
            print("Product deleted successfully")
            return True
        except pyodbc.Error as ex:
            print(f"Error deleting product: {ex}")
            return False

    def deleteCustomer(self, customerId):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customerId,))
            self.conn.commit()
            print("Customer deleted successfully")
            return True
        except pyodbc.Error as ex:
            print(f"Error deleting customer: {ex}")
            return False

    def addToCart(self,cart_id, customer, product, quantity):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO cart (cart_id,customer_id, product_id, quantity) VALUES (?,?, ?, ?)",
                           (cart_id,customer['customer_id'], product['product_id'], quantity))
            self.conn.commit()
            print("Product added to cart successfully")
            return True
        except pyodbc.Error as ex:
            print(f"Error adding product to cart: {ex}")
            return False

    def removeFromCart(self, customer, product):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM cart WHERE customer_id = ? AND product_id = ?",
                           (customer['customer_id'], product['product_id']))
            self.conn.commit()
            print("Product removed from cart successfully")
            return True
        except pyodbc.Error as ex:
            print(f"Error removing product from cart: {ex}")
            return False

    def getAllFromCart(self, customer):
        try:
            cursor = self.conn.cursor()

            rows = cursor.execute("SELECT products.* FROM products JOIN cart ON products.product_id = cart.product_id WHERE cart.customer_id = ?",
                           (customer['customer_id'],))
            products = []
            for row in rows:
                products.append({'product_id': row.product_id, 'name': row.name, 'description': row.description, 'price': row.price, 'stock_quantity': row.stock_quantity})
            return products
        except pyodbc.Error as ex:
            print(f"Error getting products from cart: {ex}")
            return []

    def placeOrder(self, order_id, customer, products_quantity_map, shippingAddress):
        try:
            cursor = self.conn.cursor()


            cart_products = self.retrieveProductsFromCart(customer['customer_id'], customer['cart_id'])

            total_price = sum(
                item['quantity'] * item['price'] for item in products_quantity_map.values()
            )


            cursor.execute(
                "INSERT INTO orders (order_id, customer_id, order_date, total_price) VALUES (?, ?, GETDATE(), ?)",
                (order_id, customer['customer_id'], total_price))


            for product_id, item in products_quantity_map.items():
                cart_quantity = cart_products.get(product_id, {'quantity': 0})['quantity']
                if cart_quantity >= item['quantity']:
                    cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
                                   (order_id, product_id, item['quantity']))
                    self.conn.commit()
                    print(f"Product with ID {product_id} added to order successfully")
                else:
                    print(f"Insufficient quantity for product with ID {product_id} in the cart")
                    return False

            print("Order placed successfully")
            return True
        except pyodbc.Error as ex:
            print(f"Error placing order: {ex}")
            return False

    def getOrdersByCustomer(self, customerId):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT products.*, order_items.quantity FROM products JOIN order_items ON products.product_id = order_items.product_id JOIN orders ON orders.order_id = order_items.order_id WHERE orders.customer_id = ?",
                           (customerId,))
            rows = cursor.fetchall()
            orders = []
            for row in rows:
                orders.append({'product_id': row.product_id, 'name': row.name, 'description': row.description, 'price': row.price, 'stock_quantity': row.stock_quantity, 'quantity': row.quantity})
            return orders
        except pyodbc.Error as ex:
            print(f"Error getting orders by customer: {ex}")
            return []

    def customerExists(self, customer_id):
        try:
            cursor = self.conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM customers WHERE customer_id = ?", (customer_id,))
            count = cursor.fetchone()[0]  # Fetch the count result
            return count > 0
        except pyodbc.Error as ex:
            print(f"Error checking if customer exists: {ex}")
            return False

    def deleteProductByID(self,product_id):
        if not self.ProductExists(product_id):
            raise exceptions.ProductNotFoundException(f"Product with ID {product_id} not found")
        try:
            cursor = self.conn.cursor()

            cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
            self.conn.commit()  # Commit the transaction
            print("Product deleted successfully")
            return True
        except pyodbc.Error as ex:
            print(f"Error deleting product: {ex}")
            return False

    def ProductExists(self, product_id):
        try:
            cursor = self.conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM products WHERE product_id = ?", (product_id,))
            count = cursor.fetchone()[0]  # Fetch the count result
            return count > 0
        except pyodbc.Error as ex:
            print(f"Error checking if customer exists: {ex}")
            return False