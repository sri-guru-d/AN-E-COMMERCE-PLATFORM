from dao import OrderProcessorRepositoryImpl
from util import db_conn_util
from entity.model import Customer,Product,Order,OrderItem
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl,OrderProcessorRepository
from exceptions import exceptions,testing

class EcomApp:
    @staticmethod
    def main():
        order = OrderProcessorRepositoryImpl()
        order_repo = db_conn_util.DBConnection()
        order_repo.getConnection()


        while True:
            print("\nMenu:")
            print("1. Register Customer")
            print("2. Create Product")
            print("3. Delete Product")
            print("4. Add to Cart")
            print("5. View Cart")
            print("6. Place Order")
            print("7. View Customer Order")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Register Customer
                customer_id = input("Enter customer ID: ")
                name = input("Enter customer name: ")
                email = input("Enter customer email: ")
                password = input("Enter customer password: ")
                customer = {'customer_id':customer_id,'name': name, 'email': email, 'password': password}
                order.createCustomer(customer)

            elif choice == "2":
                # Create Product
                product_id=int(input("Enter product ID:"))
                name = input("Enter product name: ")
                description = input("Enter product description: ")
                price = float(input("Enter product price: "))
                stock_quantity = int(input("Enter product stock quantity: "))
                product = {'product_id':product_id,'name': name, 'description': description, 'price': price, 'stock_quantity': stock_quantity}
                order.createProduct(product)
            elif choice == "3":
                # Delete Product
                product_id = int(input("Enter product ID to delete: "))
                order.deleteProduct(product_id)
            elif choice == "4":
                # Add to Cart
                cart_id=int(input("Enter Cart ID:"))
                customer_id = int(input("Enter customer ID: "))
                product_id = int(input("Enter product ID to add to cart: "))
                quantity = int(input("Enter quantity: "))
                customer = {'customer_id': customer_id}
                product = {'product_id': product_id}
                order.addToCart(cart_id,customer, product, quantity)
            elif choice == "5":
                # View Cart
                customer_id = int(input("Enter customer ID: "))
                customer = {'customer_id': customer_id}
                cart_items = order.getAllFromCart(customer)
                print("Cart Items:")
                for item in cart_items:
                    print(item)
            elif choice == "6":

                order_id=int(input("Enter the order ID:"))
                customer_id = int(input("Enter customer ID: "))

                cart_id=int(input("Enter cart ID:"))
                customer = {'customer_id': customer_id, 'cart_id': cart_id}
                products_quantity_map=order.retrieveProductsFromCart(customer_id,cart_id)

                shipping_address = input("Enter shipping address: ")
                order.placeOrder(order_id, customer, products_quantity_map, shipping_address)
            elif choice == "7":

                customer_id = int(input("Enter customer ID: "))
                orders = order.getOrdersByCustomer(customer_id)
                print("Customer Orders:")
                for order in orders:
                    print(order)

            elif choice == "8":
                print("Exiting...")
                order_repo.close_connection()
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    EcomApp.main()
