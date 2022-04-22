from flask_restful import fields

from item.application.service.item_service import ItemService


class ItemServicePort:
    service = ItemService()
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'price': fields.Float
    }

    def find_by_id(self, _id):
        return self.service.find_by_id(_id)

    def find_all(self):
        return self.service.find_all()

    def create(self, name, price):
        return self.service.create(name, price)

    def update(self, _id, name, price):
        return self.service.update(_id, name, price)

    def delete(self, _id):
        self.service.delete(_id)
