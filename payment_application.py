from incoming_request import IncomingRequest
from payment_processor import *



incoming_request = IncomingRequest()
incoming_request.user_id = 1;
incoming_request.user_name = "ABC";
incoming_request.billing_address = "123 Some Street, City Name, ST";
incoming_request.amount = 1;
#added card_number attritbute to validate
incoming_request.card_number = "3716820019271998" 
processor = PaymentProcessor()

succesful_payment = processor.process_payment(incoming_request)
print(succesful_payment)
# Check on successful payment,
#  a success code is sent to the application 
#  and a confirmation page is shown to the user

