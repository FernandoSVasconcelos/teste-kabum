import requests

json = {
        "dimensao":{
            "altura": 17,
            "largura": 16
            },
        "peso": 2
        }
        
headers = {"Content-Type": "application/json"}

r = requests.post('http://localhost:5000/api/task', json = json, headers = headers)