import requests
import json

url = "http://127.0.0.1:8000/search"
payload = {'id': '1', 'lang': 'en', 'query': 'when was python created?'}
r = requests.post(url, data=json.dumps(payload))
print(r.text)
