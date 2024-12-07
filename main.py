from flask import Flask, request, jsonify

app = Flask(__name__)

lista = [ {"id": 1, "nome": "João"}, {"id": 2, "nome": "Maria"} ]

# GET /pessoas
@app.route('/pessoas', methods=['GET'])
def pessoas():
    try:
        return jsonify(lista), 200
    except:
        return jsonify({"erro": "Erro ao retornar a lista de pessoas"}), 500

# GET /pessoas/id
@app.route('/pessoas/<int:id>', methods=['GET'])
def pessoas_id(id):
    try:
        for pessoa in lista:
            if pessoa['id'] == id:
                return jsonify(pessoa)
    except:
        return jsonify({"erro": "Pessoa não encontrada"}), 404

# POST /pessoas
@app.route('/pessoas', methods=['POST'])
def nova_pessoa():
	pessoa = request.json
	
	if len(lista) > 0:
		novoId = len(lista) + 1
	else:
		novoId = 1
		
	try:
		pessoa['id'] = novoId  # Adiciona o ID ao dicionário pessoa
          
		lista.append({"id": novoId, "nome": pessoa['nome']})
		
		return jsonify({"mensagem": "Pessoa adicionada com sucesso", "pessoa": pessoa}), 201
	
	except:
		return jsonify({"mensagem": "Erro ao adicionar pessoa"}), 400

# PUT /pessoas/id
@app.route('/atualizar/<int:id>', methods=['PUT'])
def atualizar(id):
	pessoa = request.json
	indice = -1
	
	for index, valor in enumerate(lista):
		if valor['id'] == id:
			indice = index
	
	# Valor não encontrado
	if indice == -1:
		return jsonify({"erro": "Pessoa não encontrada"}), 404
	try:
		if 'nome' in pessoa:
			lista[indice]['nome'] = pessoa['nome']
		else:
			return jsonify({"erro": "Nome não informado"}), 400

		return jsonify({"mensagem": "Pessoa atualizada com sucesso", "pessoa": lista[indice]})
	except:
		return jsonify({"mensagem": "Erro ao tentar atualizar", "pessoa": lista[indice]})


@app.route('/pessoas/deletar/<int:id>', methods=['DELETE'])
def deletar(id):
    indice = -1

    for index, d in enumerate(lista):
        if d['id'] == id:
            indice = index

    if indice == -1:
        return jsonify({"erro": "Pessoa não encontrada"}), 404
    try: 
        lista.pop(indice)

        return jsonify({"mensagem": "Pessoa deletada com sucesso"})
    
    except:
        return jsonify({"mensagem": "Erro ao tentar deletar"}), 400


if __name__ == '__main__':
    app.run(debug=True)