from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Luan',
        'habilidades':['python','dart'],
    }, 
    
    {
        'id': 1,
        'nome': 'Paulo',
        'habilidades': ['C#','javascript'],
    }
]

# Buscar, Deletar e alterar desenvolvedor pelo ID 
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except  IndexError:
            mensagem = 'desenvolvedor {} nao existe'.format(id)
            response = {'status':'erro', 'message': mensagem }       
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({
        'status': 'sucesso', 
        'mensagem': 'Registro Apagado'
        })
# Listar todos os desenvolvedores e incluir novos desenvolvedores
@app.route('/dev/', methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados  = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)
    