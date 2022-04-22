from db import db
from item.adapters.model.item_model import ItemModel


class ItemRepository:
    @staticmethod
    def find_by_name(name):
        return ItemModel.query.filter_by(name=name).first()

    @staticmethod
    def find_by_id(_id):
        return ItemModel.query.filter_by(id=_id).first()

    @staticmethod
    def find_all():
        return ItemModel.query.all()

    @staticmethod
    def create(name, price):
        item = ItemModel(name, price)
        db.session.add(item)
        db.session.commit()
        return item

    def update(self, _id, name, price):
        item = self.find_by_id(_id)
        if item:
            item.name = name
            item.price = price
            db.session.add(item)
            db.session.commit()
        return item

    def delete(self, _id):
        item = self.find_by_id(_id)
        if item:
            db.session.delete(item)
            db.session.commit()
