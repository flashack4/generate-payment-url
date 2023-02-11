import requests
import hashlib
  
# api-endpoint
API_ENDPOINT = "https://testnet.slash.fi/api/v1/payment/receive"

# Authentication Token
AUTH_TOKEN = "0eee78a07b89c948050168521396d833";

# Hash Token
HASH_TOKEN = "2de7aa4926d7b1c149dd57d6ead69fc0";
  
# Code set by the merchant to uniquely identify the payment
order_code = "t202302112330"

# Set amount and Generate verify token
#amount_to_be_charged = 10 # this number must be Zero or more
raw = '{}::::{}'.format(order_code, HASH_TOKEN)
verify_token = hashlib.sha256(raw.encode("utf-8")).hexdigest()

# data to be sent to api
data = {'identification_token':AUTH_TOKEN,
        'order_code':order_code,
        'verify_token':verify_token}
  
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)

print(data)
print(r.status_code)
print(r.text)

# extracting response text 
# payment_flow_starting_url = r.url
# print("The URL is:%s"%payment_flow_starting_url)