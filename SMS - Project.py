from twilio.rest import Client

account_sid = 'AC2d54c6f6d8c6331968bac2df10bfbc8c'
auth_token = '9fiaz0uanaa7gmhmtrlg4zfbr2hqi7wh'
client = Client(account_sid, auth_token)

message = client.messages.create(
    to= '+17868781393', 
    from_= '+12058414293',
    body= 'Hello from Python!'
)

print(message.sid)
