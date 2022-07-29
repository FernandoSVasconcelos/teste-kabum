from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
tasks = []

@app.route('/')
def home():
    return 'The API is running...'

# @app.route('/api/task', methods = ['GET'])
# def api_return():
#     return jsonify(tasks)

@app.route('/api/task/<int:task_id>', methods = ['GET'])
def api_return(task_id):
    task = tasks[task_id]
    entrega_ninja = {
        "nome": "Entrega Ninja",
        "valor_frete": (task['peso'] * 0.3) / 10,
        "prazo_dias": 6
    }
    entrega_kabum = {
        "nome": "Entrega KaBuM",
        "valor_frete": (task['peso'] * 0.2) / 10,
        "prazo_dias": 4
    }
    return jsonify([entrega_ninja, entrega_kabum])

@app.route('/api/task', methods=['POST'])
def create_task():
    if not request.json or not 'peso' in request.json:
        return(400)
    task = {
        'dimensao': {
            'altura':request.json['dimensao']['altura'],
            'largura':request.json['dimensao']['largura']
        },
        'peso': request.json['peso']
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run('0.0.0.0')