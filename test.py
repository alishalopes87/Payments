import unittest 
from incoming_request import IncomingRequest
from payment_processor import *
from user_database import *
import sys
import logging
# https://realpython.com/python-testing/#more-advanced-testing-scenarios
#added unit tests 


class TestPaymentProcessor(unittest.TestCase):
    "Tests for site."
    def test_credit_card_invalid(self):

        self.assertFalse(validator("371682001927199"))

    def test_credit_card_valid(self):
        self.assertTrue(validator("3716820019271998"))

    def test_payment_success(self):
        """
        Test that payment was successful

        """
        incoming_request = IncomingRequest()
        incoming_request.user_id = 1;
        incoming_request.user_name = "ABC";
        incoming_request.billing_address = "123 Some Street, City Name, ST";
        incoming_request.amount = 1;
        #added card_number attritbute to validate
        incoming_request.card_number = "3716820019271998" 

        processor = PaymentProcessor()
        result = processor.process_payment(incoming_request)
        self.assertTrue(result)

    def test_payment_failure_bad_cc(self):
        incoming_request = IncomingRequest()
        incoming_request.user_id = 1;
        incoming_request.user_name = "ABC";
        incoming_request.billing_address = "123 Some Street, City Name, ST";
        incoming_request.amount = 1;
        #added card_number attritbute to validate
        incoming_request.card_number = "371682001927199" 

        processor = PaymentProcessor()
        result = processor.process_payment(incoming_request)
        self.assertFalse(result)

    def test_payment_fail_user_not_in_db(self):
        """Test payment failure due to user not in DB"""

        incoming_request = IncomingRequest()
        incoming_request.user_id = 4;
        incoming_request.user_name = "ABC";
        incoming_request.billing_address = "123 Some Street, City Name, ST";
        incoming_request.amount = 1;
        #added card_number attritbute to validate
        incoming_request.card_number = "3716820019271998" 

        processor = PaymentProcessor()
        result = processor.process_payment(incoming_request)
        self.assertFalse(result)

    def test_payment_fail_username_mismatch(self):
        incoming_request = IncomingRequest()
        incoming_request.user_id = 1;
        incoming_request.user_name = "Tom Hardy";
        incoming_request.billing_address = "123 Some Street, City Name, ST";
        incoming_request.amount = 1;
        #added card_number attritbute to validate
        incoming_request.card_number = "3716820019271998" 

        processor = PaymentProcessor()
        result = processor.process_payment(incoming_request)
        self.assertFalse(result)


    def test_payment_fail_address_not_in_db(self):
        incoming_request = IncomingRequest()
        incoming_request.user_id = 1;
        incoming_request.user_name = "ABC";
        incoming_request.billing_address = "525 Stockton St, SF";
        incoming_request.amount = 1;
        #added card_number attritbute to validate
        incoming_request.card_number = "3716820019271998" 

        processor = PaymentProcessor()
        result = processor.process_payment(incoming_request)
        self.assertFalse(result)

    def test_submit_payment_fail(self):
        incoming_request = IncomingRequest()
        incoming_request.user_id = 1;
        incoming_request.user_name = "ABC";
        incoming_request.billing_address = "123 Some Street, City Name, ST";
        incoming_request.amount = 1;
        #added card_number attritbute to validate
        incoming_request.card_number = "3716820019271998" 

        processor = PaymentProcessor()
        processor.submit_payment = submit_function_fail
        result = processor.process_payment(incoming_request)
        self.assertFalse(result)

class TestUserDatabase(unittest.TestCase):
    def test_new_user(self):
        """Test add user function"""

        user_database = UserDatabase()

        user_database.add_new_user(3, "Alisha Lopes", "200 Shady Acres")
        self.assertTrue(3 in user_database.user_names,"UserId not in database")
        self.assertTrue(user_database.user_names[3]=="Alisha Lopes","Name incorrect")
        self.assertTrue(user_database.addresses[3]=="200 Shady Acres","Address incorrect")

def submit_function_fail(a,b):
    raise Error("Payment failed")

if __name__ == "__main__":
    unittest.main()
    