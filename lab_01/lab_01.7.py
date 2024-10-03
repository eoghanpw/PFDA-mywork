# Program that prints json from url.
# Author: Eoghan Walsh

import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
jsonstring = json.dumps(data)
print(data)
print(jsonstring)
