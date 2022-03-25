import requests
import json

url = "http://127.0.0.1:8000/search"
payload = {'id': '1', 'lang': 'en',
           'query': 'who invented python'}
r = requests.post(url, data=json.dumps(payload))
print(r.text)
