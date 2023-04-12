import time
from twilio.rest import Client
import os

def sendMsg():

    # Auth    
    account_sid = os.getenv('sid')
    auth_token = os.getenv('token')
    client = Client(account_sid, auth_token)

    # Send SMS using Twilio
    message = client.messages.create(
        body='We have found some movement near the object./n Captured video has been send to you through Gmail.',
        from_='+15076051161',  # your Twilio phone number
        to='+919550739128',  # recipient's phone number
    )

    print('Send.')