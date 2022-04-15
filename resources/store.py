from flask_restful import Resource, marshal_with, abort
from flask_jwt import jwt_required
from models.store import StoreModel
from resources.store_dto import CreateStoreDto, GetStoreDto


class Store(Resource):
    @jwt_required()
    @marshal_with(GetStoreDto.resource_fields, envelope='data')
    def get(self, name):
        """
        Get store by name
        ---
        parameters:
          - in: path
            name: name
            type: string
            required: true
        responses:
          200:
            description: store
          404:
            description: store not found
        """
        store = StoreModel.find_by_name(name)
        if store:
            return store
        abort(404, message="Item not found.")  

    @jwt_required()
    def delete(self, name):
        """
        Delete store by name
        ---
        parameters:
          - in: path
            name: name
            type: string
            required: true
        responses:
          200:
            description: store deleted
          404: 
            description: store not found
        """
        store = StoreModel.find_by_name(name)
        if store: 
            store.delete()
            return {'message': 'Store deleted'}

        return {'message': 'Store not found'}, 404

    @jwt_required()
    @marshal_with(GetStoreDto.resource_fields, envelope='data')
    def put(self, name):
        """
        Update store by name
        ---
        parameters:
          - name: name
            in: path
            type: string
            required: true
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
        responses:
          200:
            description: store updated
          400:
            description: invalid data
          404: 
            description: store not found
        """
        data = CreateStoreDto.parser.parse_args()

        store = StoreModel.find_by_name(name)
        if store is None:
            store = StoreModel(**data)
        else:
            store.name = data['name']
        try:
            store.save()
        except:
            abort(500, message="An error occurred inserting the store.")

        return store


class StoreList(Resource):
    @jwt_required()
    @marshal_with(GetStoreDto.resource_fields, envelope='data')
    def get(self):
        """
        Get all stores
        ---
        responses:
          200:
            description: stores
        """
        stores = StoreModel.find_all()
        return stores
    
    @jwt_required()
    @marshal_with(GetStoreDto.resource_fields, envelope='data')
    def post(self):
        """
        Create store
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
        responses:
          201:
            description: store created
          400:
            description: invalid data
        """
        data = CreateStoreDto.parser.parse_args()

        if StoreModel.find_by_name(data['name']):
            abort(400, message="An store with name '{}' already exists.".format(data['name'])) 
        
        store = StoreModel(**data)
        try:
            store.save()
        except:
            abort(500, message="An error occurred inserting the store.")

        return store, 201