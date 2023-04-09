import time
from twilio.rest import Client


# Send captured video via SMS using Twilio
account_sid = 'AC4e706298e8b3ea2bfcd1fc84f5a1a440'
auth_token = 'd9f0dae25279510d0b2a0514ccfa94c1'
client = Client(account_sid, auth_token)


def sendMsg():
    message = client.messages.create(
        body='We have found some movement near the object./n Captured video has been send to you through Gmail.',
        from_='+15076051161',  # your Twilio phone number
        to='+919550739128',  # recipient's phone number
    )
    print(message.status)

    print('Send.')