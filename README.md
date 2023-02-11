# Slash Payments generate-payment-url

Original github URL : 
https://github.com/slash-fi-public/slash-payments-minimum-merchant-api

```
npm init -y

npm install typescript ts-node

npm install @types/node -D
```

tsconfig.json
```
{
  "compilerOptions": {
    "module": "CommonJS",
    "strict": true,
  }
}
```

```
npm install axios yargs crypto

npm install @types/yargs
```

## Generate Payment URL

```
npx ts-node scripts/generate-payment-url.ts --help
```

### Options:
    --env, --environment            testnet or mainnet  [string] [default: "testnet"]
    --auth, --authentication_token  Authentication Token can be obtained from the Merchant Management screen  [string] [required] [default: false]
    --hash, --hash_token            Hash Token can be obtained from the Merchant Management screen  [string] [required] [default: false]
    -o, --order_code                The value set by the merchant to uniquely identify the payment  [string] [required] [default: false]
    -a, --amount                    The amount to be charged by your deposit currency. It is Zero or more.If the payer determines the amount to be paid, this field can be null. So this field is optional.  [number] [default: false]
    --theme, --color_theme          dark or light  [string] [default: "dark"]
    --callback, --callback_url      Custom Callback URL that will be called when the transaction’s status was changed  [string] [default: false]
    --help                          Show help  [boolean]

### IN ( Example )
```
npx ts-node scripts/generate-payment-url.ts --auth 0eee78a07b89c948050168521396d833 --hash 2de7aa4926d7b1c149dd57d6ead69fc0 -o t202302112252
```
-o order_code is uniquely identifed code ( need to change ).

### OUT ( Example )
```
{
  "url": "https://testnet.slash.fi/payment/dcf9cfa16994442d3fa20fa6c12f8ae0",
  "token": "dcf9cfa16994442d3fa20fa6c12f8ae0"
}
```


## Python Example

### Edit scripts/slash_req.py
```
### Authentication Token
AUTH_TOKEN = "0eee78a07b89c948050168521396d833";

### Hash Token
HASH_TOKEN = "2de7aa4926d7b1c149dd57d6ead69fc0";
  
### Code set by the merchant to uniquely identify the payment
order_code = "t202302112330"  
```
### Run
### IN ( Example )
```
python3 scripts/slash_req.py
```
### OUT ( Example )
```
{'identification_token': '0eee78a07b89c948050168521396d833', 'order_code': 't202302112330', 'verify_token': '906442201cf348fb4264450172a5e509350ae7e36da604824f25d563b73f2537'}
200
{"url":"https:\/\/testnet.slash.fi\/payment\/77ed979cad9e1326e5cea7a8f618fa7f","token":"77ed979cad9e1326e5cea7a8f618fa7f"}
```
get url ( delete back slash )