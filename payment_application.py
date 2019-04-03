from incoming_request import IncomingRequest
from payment_processor import PaymentProcessor


class PaymentApplication(object):
    incoming_request = IncomingRequest()
    incomingRequest.userId = 1;
    incomingRequest.userName = "ABC";
    incomingRequest.billingAddress = "123 Some Street, City Name, ST";
    incomingRequest.amount = 1;

    processor = PaymentProcessor()

    succesful_payment = processor.processor_payment(incoming_request)
    print(succesful_payment)
