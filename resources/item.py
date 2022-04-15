from flask_restful import Resource, marshal_with, abort
from flask_jwt import jwt_required
from models.item import ItemModel
from models.store import StoreModel
from resources.item_dto import CreateItemDto, GetItemDto


class Item(Resource):
    @jwt_required()
    @marshal_with(GetItemDto.resource_fields, envelope='data')
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
            return item
        abort(404, message="Item not found.") 

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
    @marshal_with(GetItemDto.resource_fields, envelope='data')
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
        data = CreateItemDto.parser.parse_args()

        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(**data)
        else:
            item.name = data['name']
            item.price = data['price']
        try:
            item.save()
        except:
            abort(500, message="An error occurred inserting the item.")

        return item


class ItemList(Resource):
    @jwt_required()
    @marshal_with(GetItemDto.resource_fields, envelope='data')
    def get(self):
        """
        Get all items
        ---
        responses:
          200:
            description: items
        """
        items = ItemModel.find_all()
        return items
    
    @jwt_required()
    @marshal_with(GetItemDto.resource_fields, envelope='data')
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
        data = CreateItemDto.parser.parse_args()

        if ItemModel.find_by_name(data['name']):
            abort(400, message="An item with name '{}' already exists.".format(data['name'])) 

        if not StoreModel.find_by_id(data['store_id']):
            abort(400, message="Store with id '{}' not found.".format(data['store_id'])) 

        
        item = ItemModel(**data)
        try:
            item.save()
        except:
            abort(500, message="An error occurred inserting the item.")

        return item, 201