from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


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

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
            
        return {'message': 'Item not found'}, 404  

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item: 
            item.delete()
            return {'message': 'Item deleted'}

        return {'message': 'Item not found'}, 404

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(data['name'], data['price'])
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

    @jwt_required()
    def get(self):
        items = ItemModel.find_all()
        return {'items': [item.json() for item in items]}
    
    @jwt_required()
    def post(self):
        data = Item.parser.parse_args()

        if ItemModel.find_by_name(data['name']):
            return {'message': "An item with name '{}' already exists.".format(data['name'])}, 400
        
        item = ItemModel(**data)
        try:
            item.save()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201