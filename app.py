from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resourcers.user import UserRegister
from resourcers.item import Item, ItemList


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'asdf'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/item')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
