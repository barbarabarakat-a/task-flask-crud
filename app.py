# atraves do jsonify voce consegue criar um dicionario que vai ser retornado com o json
from flask import Flask, request, jsonify
from models.task import Task

# Quando executar de forma manual (e nao esta sendo implantado ou importado de outro arquivo) tera o valor de main: __name__ = __main__

app = Flask(__name__)  # Aplicacao Flask criada

"""
# Criar uma rota, que seria por onde conseguimos comunicar com os clientes(usuario/acessar) - comunicacao:
@app.route("/")  # Retorna uma string para o usuario em formato html
def hello_world():  # O que sera acessado a partir da rota
    return "Hello World!"


@app.route("/about") #Criar uma nova rota 
def about():
    return "Pagina sobre"
"""

tasks = []
task_id_control = 1

# criar uma Tabela: Tarefas com o CRUD (Create, Read, Update and Delete)

# Para criacao (POST) ela vai ter uma rota -> metodo: Post - Endpoint: tasks


@app.route('/tasks', methods=['POST'])  # para criar rota
def create_task():  # funcao que vai ser executada, que e responsavel por criar a nossa atividade
    # Para conseguir acessar a variavel global, tornando-a local para acesso
    global task_id_control
    data = request.get_json()  # Receber as informacoes que o cliente enviou. A API pode ser construida pelas informacoes de um cliente ou tambem de um banco de dados
    new_task = Task(id=task_id_control,
                    title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id})


# em Read geralmente temos duas listagens: 1 para listagem de todas as tarefas  ou ler apenas um recurso especifico
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            # aqui nao precisamos do brak, porque quando ele encontrar, ele vai sair da funcao
            return jsonify(t.to_dict())

    return jsonify({"message": "Nao foi possivel encontrar a atividade."}), 404

# PARAMETROS DE ROTA permite que voce receba algo naquela rota (<int:id>)
# @app.route('/user/<int:user_id>')
# def show_user(user_id):
#     print(user_id)
#     print(type(user_id))
#     return "%s" % user_id

# UPDATE


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({"message": "Nao foi encontrada a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

# DELETE


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t  # nao remover na iteracao, porque vai implicar na diferenca da lista
            # para quebrar o looping, e evitar uma iteracao desnecessaria, porque nesse caso estamos dando o return fora do looping.
            break

    if not task:  # pode ser assim: task == None
        return jsonify({"message": "Nao foi possivel encontrar a atividade"}), 404

    tasks.remove(task)
    # por padrao nao precisamos colocar o retorno 200
    return jsonify({"message": "Tarefa deletada com sucesso"})


# So se for rodar de forma manual; apenas para conhecimento (nao e recomendado disponibilizar para clientes reais)
if __name__ == "__main__":
    # Essa propriedade debug vai nos ajudar a visualizar muitas informacoes para entender o que esta acontecendo no servidor web
    app.run(debug=True)
