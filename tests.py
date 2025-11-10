#vamos precisar de duas bibliotecas: pytest e request

import pytest
import requests

#CRUD: 
#Definir variaveis:
BASE_URL = 'http://127.0.0.1:5000'
tasks = [] #Para que eu consiga testar as tarefas que serao incluidas

#Vamos testar primeiro o CREATE:
def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descricao da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)   #como enviar? - Usando o request POST, ele vai enviar uma requisicao, json para enviar os dados que voce quer
#Para saber se deu certo: toda vez que o POST responde, ele responde um objeto, portanto vamos armazenar essa objeto em uma variavel: response
    assert response.status_code == 200 #inserimos o assert para testar essas duas informacoes, se elas serao compativeis

   
    #recuperar a resposta do servidor:
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])


#Vamos testar o READ: duas opcoes - 1. para todas as atividades 2. para uma atividade especifica
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks") #essa requisicao nao tem nenhum corpo
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response.json()['id'] 


#Vamos testar o UPDATE 
def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": False,
            "description": "Nova descricao",
            "title": "Titulo atualizado"
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        response.status_code == 200
        response_json= response.json()
        assert "message" in response.json()

#Nova requisicao a tarefa especifica:
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['title'] == payload['title']
    assert response_json['description'] == payload['description']
    assert response_json['completed'] == payload['completed']


#Vamos testar o DELETE
def test_delete_task():
    if tasks: #Aqui vamos validar, se eu eu consigo apagar a tarefa criada la em cima
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}") #entre parenteses esta o endpoint
        response.status_code == 200

        #Essa verificacao e pra depois de apagar, a tarefa deve dar como nao encontrada, porque ela nao existe.
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404 


     #Testar API:
    #abre o terminal -> digita pytest test.py -v (usa o comando -v para dar todas as informacoes)

        