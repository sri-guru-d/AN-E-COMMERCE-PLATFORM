import unittest

class TestEcommerceSystem(unittest.TestCase):
    def setUp(self):

        self.order_processor = ecom.entity.OrderProcessorRepositoryImpl()

    def tearDown(self):

        pass

    def test_create_product_success(self):

        product = {'product_id':81,'name': 'Test Product', 'description': 'Test Description', 'price': 50.0, 'stock_quantity': 10}
        result = self.order_processor.createProduct(product)
        self.assertTrue(result)

    def test_add_to_cart_success(self):

        cart_id = 902

        customer_id = 1
        customer = {'customer_id': customer_id}
        product_id = 1
        product = {'product_id': product_id}
        quantity = 2
        result = self.order_processor.addToCart(cart_id, customer, product, quantity)
        self.assertTrue(result)

    def test_place_order_success(self):

        order_id=901
        customer = {'customer_id': 1, 'cart_id': 1}  # Assuming 'cart_id' is required for placing an order
        products_quantity_map = self.order_processor.retrieveProductsFromCart(customer['customer_id'],customer['cart_id']) # Example: {product_id: quantity}
        shipping_address = 'Test Address'
        result = self.order_processor.placeOrder(order_id,customer, products_quantity_map, shipping_address)
        self.assertTrue(result)

    def test_customer_not_found_exception(self):

        with self.assertRaises(ecom.exception.CustomerNotFoundException):
            self.order_processor.getOrdersByCustomer(999)

    def test_product_not_found_exception(self):

        with self.assertRaises(ecom.exception.ProductNotFoundException):
            self.order_processor.deleteProductByID(999)

if __name__ == '__main__':
    unittest.main()
