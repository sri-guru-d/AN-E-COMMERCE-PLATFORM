class CustomerNotFoundException(Exception):

    def __init__(self, message="Customer Not Found"):
        self.message = message
        super().__init__(self.message)

class ProductNotFoundException(Exception):

    def __init__(self, message="Product Not Found"):
        self.message = message
        super().__init__(self.message)

class OrderNotFoundException(Exception):

    def __init__(self, message="Order Not Found"):
        self.message = message
        super().__init__(self.message)