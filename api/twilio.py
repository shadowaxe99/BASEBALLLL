```python
from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

def send_sms(to, message_name):
    messages = {
        'player_added': 'A new player has been added to your roster.',
        'meeting_scheduled': 'A new meeting has been scheduled.',
        'contract_updated': 'A contract has been updated.'
    }

    message = client.messages.create(
        body=messages[message_name],
        from_='+your_twilio_number',
        to=to
    )

    return message.sid
```