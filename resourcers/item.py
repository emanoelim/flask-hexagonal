from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item_repository import ItemRepository
from models.item import ItemModel


class Item(Resource):
    item_repository = ItemRepository()
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

    @jwt_required()
    def get(self, name):
        item = self.item_repository.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404  

    @jwt_required()
    def delete(self, name):
        if self.item_repository.find_by_name(name): 
            try:
                self.item_repository.delete(name)
            except:
                return {"message": "An error occurred deleting the item."}, 500
            return {'message': 'Item deleted'}
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = self.item_repository.find_by_name(name)
        if item is None:
            try:
                updeted_item = self.item_repository.insert(data['name'], data['price'])
            except:
                return {"message": "An error occurred inserting the item."}, 500
        else:
            try:
                updeted_item = self.item_repository.update(item, data['name'], data['price'])
            except:
                return {"message": "An error occurred updating the item."}, 500
        return updeted_item.json()


class ItemList(Resource):
    item_repository = ItemRepository()
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

    @jwt_required()
    def get(self):
        items = self.item_repository.find_all()
        return {'items': [item.json() for item in items]}
    
    @jwt_required()
    def post(self):
        data = Item.parser.parse_args()
        if self.item_repository.find_by_name(data['name']):
            return {'message': "An item with name '{}' already exists.".format(data['name'])}, 400
        try:
            item = self.item_repository.insert(data['name'], data['price'])
        except:
            return {"message": "An error occurred inserting the item."}, 500
        return item.json()  