import os

from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from settings import DEBUG, SQLALCHEMY_DATABASE_URI
from db import db

from item.adapters.inbound.controller.item_controller import ItemController, ItemListController


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # utilizar o flask sqlalchemy
app.secret_key = os.environ.get('SECRET_KEY')
api = Api(app)
swagger = Swagger(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(ItemController, '/item/<string:id>')
api.add_resource(ItemListController, '/item')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=DEBUG)

