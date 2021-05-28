from twilio.rest import Client
from decouple import config
import pandas, time
excel_data = pandas.read_excel('phones.xlsx', sheet_name=None)

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client_phone = config('PHONE')
client = Client(account_sid, auth_token)

phone_arr = excel_data['Sheet1'].to_numpy()
message = open("message.txt", "r")

for phone in phone_arr:
    phone = "+58%s" % phone[0]

    try:
        message = client.messages.create(
            body=message.read(),
            from_=client_phone,
            to=phone
        )

        if not message.error_code:
            print("Enviado:", phone)
    except Exception:
        print("Error!: ", phone)
        pass
    time.sleep(10)
