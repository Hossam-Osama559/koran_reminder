from twilio.rest import Client
from dotenv import load_dotenv 
import os 

load_dotenv()

class alert_handler:




    @classmethod
    def alert(cls,msg):


        account_sid = os.environ["account_sid"]
        auth_token =os.environ["auth_token"]
        client = Client(account_sid, auth_token)

        # api call
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f"{msg}",
        to=os.environ["phone_number"]
        )    

