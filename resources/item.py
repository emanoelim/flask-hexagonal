from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
from models.store import StoreModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="The field 'name' cannot be left blank!"
    )
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field 'price' cannot be left blank!"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="This field 'store_id' cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        """
        Get item by name
        ---
        parameters:
          - in: path
            name: name
            type: string
            required: true
        responses:
          200:
            description: item
          404:
            description: item not found
        """
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
            
        return {'message': 'Item not found'}, 404  

    @jwt_required()
    def delete(self, name):
        """
        Delete item by name
        ---
        parameters:
          - in: path
            name: name
            type: string
            required: true
        responses:
          200:
            description: item deleted
          404:
            description: item not found
        """
        item = ItemModel.find_by_name(name)
        if item: 
            item.delete()
            return {'message': 'Item deleted'}

        return {'message': 'Item not found'}, 404

    @jwt_required()
    def put(self, name):
        """
        Update item by name
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
                price:
                  type: number
                store_id:
                  type: integer
        responses:
          200:
            description: item updated
          400:
            description: invalid data
          404: 
            description: item not found
        """
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(**data)
        else:
            item.name = data['name']
            item.price = data['price']
        try:
            item.save()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json()


class ItemList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field 'name' cannot be left blank!"
    )
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field 'price' cannot be left blank!"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="This field 'store_id' cannot be left blank!"
    )

    @jwt_required()
    def get(self):
        """
        Get all items
        ---
        responses:
          200:
            description: items
        """
        items = ItemModel.find_all()
        return {'items': [item.json() for item in items]}
    
    @jwt_required()
    def post(self):
        """
        Create item
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
                price:
                  type: number
                store_id:
                  type: integer
        responses:
          201:
            description: item created
          400:
            description: invalid data
        """
        data = Item.parser.parse_args()

        if ItemModel.find_by_name(data['name']):
            return {'message': "An item with name '{}' already exists.".format(data['name'])}, 400

        if not StoreModel.find_by_id(data['store_id']):
            return {'message': "Store with id '{}' not found.".format(data['store_id'])}, 400

        
        item = ItemModel(**data)
        try:
            item.save()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201