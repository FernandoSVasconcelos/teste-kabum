from flask import Flask, jsonify, request, make_response
from validation import valida_frete, valida_retorno

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
tasks = []

@app.route('/')
def home():
    return 'The API is running...'

@app.route('/api/task/<int:task_id>', methods = ['GET'])
def api_return(task_id):
    entrega_ninja, entrega_kabum = valida_frete(tasks[task_id])
    response = valida_retorno(entrega_ninja, entrega_kabum)

    return jsonify(response)

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