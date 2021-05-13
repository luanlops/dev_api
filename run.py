from flask import Flask, request
from flask_restful import Resource, Api
import json



app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'carlos',
        'habilidades':['python','dart'],
    }, 
    
    {
        'id': 1,
        'nome': 'joao',
        'habilidades': ['C++','javascript'],
    }
]

# Buscar, Deletar e alterar um desenvolvedor pelo ID 
class Desenvolvedor(Resource):
    def get(self, id):
            try:
                response = desenvolvedores[id]
            except  IndexError:
                mensagem = 'desenvolvedor {} nao existe'.format(id)
                response = {'status':'erro', 'message': mensagem }
            except Exception:
                mensagem = 'Erro desconhecido. Procure a Administracao da API'
                response = {'status':'erro', 'message':mensagem}       
            return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self,id):
        desenvolvedores.pop(id)
        return {
        'status': 'sucesso', 
        'mensagem': 'Registro Apagado'
        }

# Listar todos os desenvolvedores e incluir novos desenvolvedores
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados  = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')

if __name__ == '__main':
    app.run(debug=True)