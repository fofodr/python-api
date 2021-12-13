import requests
import json

url = "https://webexapis.com/v1/messages"
token = "NmRjNTMzM2MtYjE5Zi00ZGI0LTllODctOTk5MTI0MzFmOTJiNzY2MzllOGItZGEz_PF84_2a001399-4e85-4adc-b568-32f8032f2ae7"
roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl"

payload = {
    "roomId": roomId,
    "text": "¡VIVA HEREDIA!"
}

data = json.dumps(payload)

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=data)

print(response.text)