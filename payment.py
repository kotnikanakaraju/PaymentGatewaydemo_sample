

Keyid='rzp_test_OijlThSARF%Q'
keySecret='90jFNAKWcnJTodAIURIQYgz2'

import rozorpay 
rozorpay.Client(auth=(keyid,keySecret))

# checkout
data={
    'ammount':'100*100',
    "currency":"INR",
    "Receipt": "feeltohappy"
    "notes":{
        "name":"virenadra",
        "payment_for":"css"
    }
}

order=Client.order.create(data=data)
print(order)
