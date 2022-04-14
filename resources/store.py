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
            return store.json()
            
        return {'message': 'Store not found'}, 404  

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
        """
        Get all stores
        ---
        responses:
          200:
            description: stores
        """
        stores = StoreModel.find_all()
        return {'Stores': [store.json() for store in stores]}
    
    @jwt_required()
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
        data = Store.parser.parse_args()

        if StoreModel.find_by_name(data['name']):
            return {'message': "An store with name '{}' already exists.".format(data['name'])}, 400
        
        store = StoreModel(**data)
        try:
            store.save()
        except:
            return {"message": "An error occurred inserting the store."}, 500

        return store.json(), 201