
class Customer:
    def __init__(self, customer_id, name, email, password):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__password = password

    # Getters and setters
    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

class Product:
    def __init__(self, product_id: str, p_name: str, price: float, description: str, stock_quantity: int):
        self.product_id = product_id
        self.p_name = p_name
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity

    def get_product_id(self) -> str:
        return self.product_id

    def set_product_id(self, product_id):
        self.product_id = product_id

    def get_name(self):
        return self.p_name

    def set_name(self, p_name):
        self.p_name = p_name

    def get_price(self) -> float:
        return self.price

    def set_price(self, price):
        self.price = price

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_stock_quantity(self):
        return self.stock_quantity

    def set_stock_quantity(self, stock_quantity):
        self.stock_quantity = stock_quantity

class Order:
    def __init__(self, order_id, customer_id, order_date, total_price, shipping_address):
        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__order_date = order_date
        self.__total_price = total_price
        self.__shipping_address = shipping_address

    # Getters and setters
    def get_order_id(self):
        return self.__order_id

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_order_date(self):
        return self.__order_date

    def set_order_date(self, order_date):
        self.__order_date = order_date

    def get_total_price(self):
        return self.__total_price

    def set_total_price(self, total_price):
        self.__total_price = total_price

    def get_shipping_address(self):
        return self.__shipping_address

    def set_shipping_address(self, shipping_address):
        self.__shipping_address = shipping_address

class OrderItem:
    def __init__(self, order_item_id, order_id, product_id, quantity):
        self.__order_item_id = order_item_id
        self.__order_id = order_id
        self.__product_id = product_id
        self.__quantity = quantity

    # Getters and setters
    def get_order_item_id(self):
        return self.__order_item_id

    def set_order_item_id(self, order_item_id):
        self.__order_item_id = order_item_id

    def get_order_id(self):
        return self.__order_id

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity