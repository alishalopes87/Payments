from incoming_request import incoming_request
from user_database import UserDatabase

class PaymentProcessor(object):
    def process_payment(incoming_request):
        user_database = UserDatabase()

        if incoming_request.userId in user_database.user_names:
            user_name_from_db = user_database.user_names[incoming_request.userId]

            (if incoming_request.user_name == user_name_from_db and
                validate_address(incoming_request.billingAddress, 
                user_database.addresses[incoming_request.userId]):

                try:
                    submit_payment(incoming_request.cardnumber, incoming_request.amount)
                    return True

                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    return False

        return False 


    def validate_address(address_from_request, address_from_db):
        return address_from_request == address_from_db

    def submit_payment(card, amount):
        #don't implement this. 
        pass 

