from incoming_request import IncomingRequest
from user_database import *
import sys 
#python logging module 
import logging 

# Range check: check numbers to ensure they are within a range of possible values, e.g., the value for month should lie between 1 and 12.
# Reasonable check: check values for their reasonableness, e.g. (age > 16) && (age < 100)
# Arithmetic check: check variables for values that might cause problems such as division by zero.
# Format check: check that the data is in a specified format (template), e.g., dates have to be in the format DD/MM/YYYY.
#library for cc validation 



#add test

#add logging print out info to retroactively figure out what happened
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')

def validator(card_num):
    """validates credit card base on 16 digit input"""

    validatelist=[]

    for num in card_num:
        validatelist.append(int(num))


    for i in range(0,len(card_num),2):


        validatelist[i] = validatelist[i]*2

        if validatelist[i] >= 10:

            validatelist[i] = validatelist[i]//10 + validatelist[i]%10


    if sum(validatelist)%10 == 0:
        return True 
        print('This a valid credit card') 

    else:
        return False

class PaymentProcessor(object):
    def process_payment(self,incoming_request):
        user_database = UserDatabase()
        if not validator(incoming_request.card_number):
            logging.warning('This is not valid credit card')
            return False
    
           


        if incoming_request.user_id in user_database.user_names:
            user_name_from_db = user_database.user_names[incoming_request.user_id]
            if (
                incoming_request.user_name == user_name_from_db and
                self.validate_address(incoming_request.billing_address, 
                    user_database.addresses[incoming_request.user_id])
                ):

                try:
                    self.submit_payment(incoming_request.card_number, incoming_request.amount)
                    return True

                except:
                    logging.warning("Unexpected error:", sys.exc_info()[0])
                    return False

        return False 


    def validate_address(self,address_from_request, address_from_db):
        return address_from_request == address_from_db

    def submit_payment(self,card, amount):
        #don't implement this. 
        pass 
