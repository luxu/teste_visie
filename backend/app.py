from datetime import datetime
import json

from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)

from visie import *


@app.route('/')
def list():
    connection = conexao()
    pessoas = listar(connection)
    return jsonify(pessoas)


@app.route('/<int:id_pessoa>', methods=['GET'])
def searchbyid(id_pessoa):
    connection = conexao()
    pessoa = consultar_por_id(connection, id_pessoa)
    return jsonify(pessoa)


@app.route('/<nome>', methods=['GET'])
def searchbyname(nome):
    connection = conexao()
    pessoas = consultar_por_nome(connection, nome)
    return jsonify(pessoas)


@app.route('/adicionar', methods=['POST'])
def add():
    connection = conexao()
    data = json.loads(request.data)
    nome = data['nome']
    rg = data['rg']
    cpf = data['cpf']
    data_nascimento = datetime.strptime(data['data_nascimento'], '%d/%m/%Y')
    data_admissao = datetime.strptime(data['data_admissao'], '%d/%m/%Y')
    funcao = data['funcao']
    data = {
        'nome': nome,
        'rg': rg,
        'cpf': cpf,
        'data_nascimento': data_nascimento,
        'data_admissao': data_admissao,
        'funcao': funcao,
    }
    inserir(connection, data)
    return 'Adicionado a pessoa'


@app.route('/atualizar', methods=['POST'])
def update():
    data = json.loads(request.data)
    if id_pessoa := data['id_pessoa']:
        nome = data['nome']
        rg = data['rg']
        cpf = data['cpf']
        funcao = data['funcao']
        data_nascimento = datetime.strptime(data['data_nascimento'], '%d/%m/%Y')
        data_admissao = datetime.strptime(data['data_admissao'], '%d/%m/%Y')
        data = {
            'nome': nome,
            'rg': rg,
            'cpf': cpf,
            'data_nascimento': data_nascimento,
            'data_admissao': data_admissao,
            'funcao': funcao,
            'id_pessoa': id_pessoa,
        }
        connection = conexao()
        error = alterar(connection, data)
        if not error:
            return f'Pessoa..: {nome} atualizada!'
        return f'ERRO...: {error}'
    else:
        return 'ID não passado!'


@app.route('/deletar', methods=['DELETE'])
def delete():
    data = json.loads(request.data)
    id_pessoa = data['id_pessoa']
    if id_pessoa:
        connection = conexao()
        try:
            retorno = deletar(connection, id_pessoa)
            return f'Pessoa de ID..: {id_pessoa} deletada com sucesso!'
        except Exception as err:
            return err
    else:
        return f'ID não passado!'


if __name__ == '__main__':
    app.run()
