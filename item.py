from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from item_repository import ItemRepository


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
            return item
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
        updated_item = {'name': data['name'], 'price': data['price']}
        if item is None:
            try:
                self.item_repository.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the item."}, 500
        else:
            try:
                self.item_repository.update(updated_item)
            except:
                return {"message": "An error occurred updating the item."}, 500
        return updated_item


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
        return {'items': items}
    
    @jwt_required()
    def post(self):
        data = Item.parser.parse_args()
        if self.item_repository.find_by_name(data['name']):
            return {'message': "An item with name '{}' already exists.".format(data['name'])}, 400
        item = {'name': data['name'], 'price': data['price']}
        try:
            self.item_repository.insert(item)
        except:
            return {"message": "An error occurred inserting the item."}, 500
        return item  