import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
for item_k in response['bpi'].keys():
    print('price of bitcoin per ' , response['bpi'][item_k]['description'] , ' is ' ,response['bpi'][item_k]['rate_float'])