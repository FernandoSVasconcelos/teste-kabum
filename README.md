# KaBuM! Back-end Challenge
 
 A REST API designed to retrieve the available shipping options according to the input sent inside the request body. Built using [Python 3.10](https://www.python.org/downloads/) with [Flask Micro Framework](https://flask.palletsprojects.com/en/2.2.x/).

## Getting Started

### Follow the instructions to get a copy of the project up and running using [Visual Studio Code IDE](https://code.visualstudio.com/).

- Clone or download the repo.
- Open the terminal/cmd and type: pip install -r requirements.txt
- Open the project in Visual Studio Code IDE.
- Go to teste-kabum/src/.
- Then run: python main_api.py

### Sending the requests using library [requests](https://pypi.org/project/requests/)

- With the project running, run: python make_request.py. To send an POST request to `http://127.0.0.1:5000/api/task`.
- Use the body of the Json in make_request.py to inform the input data in JSON format.

### To access the responses of the requests

- Go to `http://127.0.0.1:5000/api/task/<request_numer>`.
- For example: `http://127.0.0.1:5000/api/task/0`

### Test cases

#### input

```json
{
    "dimensao": {
        "altura":102,
        "largura":40
    },
    "peso":400
}
```

#### output

```json
[
    {
        "nome":"Entrega Ninja",
        "valor_frete": 12.00,
        "prazo_dias": 6
    },
    {
        "nome":"Entrega KaBuM",
        "valor_frete": 8.00,
        "prazo_dias": 4
    }
]
```

---

#### input

```json
{
    "dimensao": {
        "altura":152,
        "largura":50
    },
    "peso":850
}
```

#### output

```json
[
    {
        "nome":"Entrega Ninja",
        "valor_frete": 25.50,
        "prazo_dias": 6
    }
]
```

---

#### input

```json
{
    "dimensao": {
        "altura":230,
        "largura":162
    },
    "peso":5600
}
```

#### output

```json
[]
```