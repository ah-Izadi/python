import requests
response = requests.get('https://a.4cdn.org/boards.json').json()
for k in response:
    for index in range(len(response[k])):
        for item_k in response[k][index]:
            if item_k=="title":
                print(item_k,':',response[k][index][item_k])