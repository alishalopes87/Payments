import unittest 
from payment_application import *
from payment_processor import PaymentProcessor
# https://realpython.com/python-testing/#more-advanced-testing-scenarios
#added unit tests 

class Test(unittest.TestCase):
    "Tests for site."

    # def setUpClass(cls):
    #     cls._connection = createExpensiveConnectionObject()

    def success(self):
        """
        Test that payment was successful

        """
        result = processor.process_payment(incoming_request)
        self.assertTrue(result)


    # def tearDownClass(cls):
    #     cls._connection.destroy()



if __name__ == "__main__":
    unittest.main()
    "YAY ALL TESTS PASSED!"
    