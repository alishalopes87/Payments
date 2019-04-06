import unittest 
from payment_application import *
from payment_processor import PaymentProcessor
from user_database import *
import sys
import logging
# https://realpython.com/python-testing/#more-advanced-testing-scenarios
#added unit tests 


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)



class TestPaymentProcessor(unittest.TestCase):
    "Tests for site."

    # def setUpClass(cls):
    #     cls._connection = createExpensiveConnectionObject()
    def testSimpleMsg(self):
        stream_handler.stream = sys.stdout
        print("AA")
        logging.getLogger().info("BB")

    def test_payment_success(self):
        """
        Test that payment was successful

        """
        processor = PaymentProcessor()
        result = processor.process_payment(incoming_request)
        self.assertTrue(result)

    def test_incoming_request(self):
        incoming_request = IncomingRequest()
        incoming_request.user_id = 1;
        incoming_request.user_name = "ABC";
        incoming_request.billing_address = "123 Some Street, City Name, ST";
        incoming_request.amount = 1;
        #added card_number attritbute to validate
        incoming_request.card_number = "3716820019271998" 
        assert incoming_request.amount > 0

    def test_new_user(self):
        user_database = UserDatabase()

        user_database.add_new_user(1, "Alisha Lopes", "200 Shady Acres")
        self.assertTrue(1 in user_database.user_names)
        



if __name__ == "__main__":
    unittest.main()
    