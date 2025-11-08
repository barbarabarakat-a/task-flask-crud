from flask import Flask, request
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

#criar uma Tabela: Tarefas com o CRUD (Create, Read, Update and Delete)

#Para criacao (POST) ela vai ter uma rota -> metodo: Post - Endpoint: tasks
@app.route('/tasks', methods=['POST']) #para criar rota
def create_task():#funcao que vai ser executada, que e responsavel por criar a nossa atividade
    data = request.get_json()    #Receber as informacoes que o cliente enviou. A API pode ser construida pelas informacoes de um cliente ou tambem de um banco de dados
    print(data)
    return 'Test'
# So se for rodar de forma manual; apenas para conhecimento (nao e recomendado disponibilizar para clientes reais)
if __name__ == "__main__":
    # Essa propriedade debug vai nos ajudar a visualizar muitas informacoes para entender o que esta acontcendo no servidor web
    app.run(debug=True)
