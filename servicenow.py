import requests
import json
import base64

url = "https://dev43030.service-now.com/api/now/table/incident"
username = "admin"
password = "46VRzPnvfSGv"
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl"

payload = {
    "short_description": "Tiquete abierto desde Python CGI",
    "description": "Prueba apertura ticket",
    "category": "Network",
    "caller_id": "abraham.lincoln@example.com"
}

data = json.dumps(payload)

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, auth=(username, password), headers=headers, data=data)

print(response.text)