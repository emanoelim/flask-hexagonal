## Projeto curso REST APIs with Flask and Python

### Endpoints:

Novo usuário: 

* Novo usuário: POST http://127.0.0.1:5000/register - {"username": "username", "password", "password"}

Login:

* Login: POST http://127.0.0.1:5000/auth - {"username": "username", "password", "password"}

Loja:

* Cadastrar loja: POST http://127.0.0.1:5000/store - {"name": "shopee"}
* Recuperar loja pelo nome: GET http://127.0.0.1:5000/store/shopee
* Recuperar todas as lojas: GET http://127.0.0.1:5000/store
* Atualizar loja: PUT http://127.0.0.1:5000/store/shopee - {"name": "Shopee"}
* Deletar loja: DELETE http://127.0.0.1:5000/store/shopee

Item:

* Cadastrar item: POST http://127.0.0.1:5000/item - {"name": "table", "price": "150.00", "store_id": 1}
* Recuperar item pelo nome: GET http://127.0.0.1:5000/item/table
* Recuperar todos os itens: GET http://127.0.0.1:5000/item
* Atualizar item: PUT http://127.0.0.1:5000/item/table - {"name": "table", "price": "150.00", "store_id": 2}
* Deletar item: DELETE http://127.0.0.1:5000/item/table
