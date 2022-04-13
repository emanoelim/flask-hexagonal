from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="The field 'name' cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
            
        return {'message': 'Store not found'}, 404  

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store: 
            store.delete()
            return {'message': 'Store deleted'}

        return {'message': 'Store not found'}, 404

    @jwt_required()
    def put(self, name):
        data = Store.parser.parse_args()

        store = StoreModel.find_by_name(name)
        if store is None:
            store = StoreModel(**data)
        else:
            store.name = data['name']
        try:
            store.save()
        except:
            return {"message": "An error occurred inserting the store."}, 500

        return store.json()


class StoreList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field 'name' cannot be left blank!"
    )

    @jwt_required()
    def get(self):
        stores = StoreModel.find_all()
        return {'Stores': [store.json() for store in stores]}
    
    @jwt_required()
    def post(self):
        data = Store.parser.parse_args()

        if StoreModel.find_by_name(data['name']):
            return {'message': "An store with name '{}' already exists.".format(data['name'])}, 400
        
        store = StoreModel(**data)
        try:
            store.save()
        except:
            return {"message": "An error occurred inserting the store."}, 500

        return store.json(), 201