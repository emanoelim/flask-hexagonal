from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from db import db

from item.adapters.inbound.controller.item_controller import ItemController, ItemListController


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# utilizar o flask flask sqlalchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'asdf'
api = Api(app)

swagger = Swagger(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(ItemController, '/item/<string:id>')
api.add_resource(ItemListController, '/item')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
