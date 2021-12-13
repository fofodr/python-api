from flask import Flask
import requests
import json

app = Flask(__name__)
@app.route('/webhook', methods = ['POST'])
def webhook():
    url = "https://webexapis.com/v1/messages"
    data = json.dumps({
        "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl",
        #"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vZTQ5ZDEwNTAtZWRjYy0xMWU4LThkOGItNDE0ZTM5NDdkY2Fi",
        #"toPersonEmail": "judrodriguez@bancobcr.com",
        #"toPersonEmail": "lrdelgado@bancobcr.com",
        "text": "Compañeros Bienvenidos a la reunión!!"
    })
    headers = {
        "Authorization": "Bearer MmRkOGU1MjAtODlhZi00MjQ4LWEyZmItYTRjNzk0ZDExNTcwMWYyNTk4YjMtMTYz_PF84_2a001399-4e85-4adc-b568-32f8032f2ae7",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, data=data)
    return 'Success Rodolfo'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)