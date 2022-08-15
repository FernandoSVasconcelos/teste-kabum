import requests

# Realiza a requisição POST para a API.
def make_request(altura, largura, peso):
    json = {
            "dimensao":{
                "altura": altura,
                "largura": largura
                },
            "peso": peso
            }
            
    headers = {"Content-Type": "application/json"}

    r = requests.post('http://localhost:5000/api/task', json = json, headers = headers)

if __name__ == '__main__':
    make_request(102, 40, 400)
    make_request(152, 50, 850)
    make_request(230, 162, 5600)