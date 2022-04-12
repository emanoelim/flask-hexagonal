### Projeto curso REST APIs with Flask and Python

Endpoints:

* Novo usuário: POST http://127.0.0.1:5000/register - {"username": "username", "password", "password"}
* Login: POST http://127.0.0.1:5000/auth - {"username": "username", "password", "password"}
* Cadastrar item: POST http://127.0.0.1:5000/item - {"name": "table", "price": "150.00"}
* Recuperar item pelo nome: GET http://127.0.0.1:5000/item/table
* Recuperar todos os itens: GET http://127.0.0.1:5000/item
* Atualizar item: PUT http://127.0.0.1:5000/item/table - {"name": "table", "price": "150.00"}
* Deletar item: DELETE http://127.0.0.1:5000/item/table
