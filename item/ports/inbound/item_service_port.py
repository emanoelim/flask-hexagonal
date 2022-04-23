from typing import List

from flask_restful import fields

from item.adapters.model.item_model import ItemModel
from item.application.service.item_service import ItemService


class ItemServicePort:
    service = ItemService()
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'price': fields.Float,
        'image': fields.String
    }

    def find_by_id(self, _id: int) -> ItemModel:
        return self.service.find_by_id(_id)

    def find_all(self) -> List[ItemModel]:
        return self.service.find_all()

    def create(self, name: str, price: float, image: str) -> ItemModel:
        return self.service.create(name, price, image)

    def update(self, _id: int, name: str, price: float, image: str) -> ItemModel:
        return self.service.update(_id, name, price, image)

    def delete(self, _id: int) -> None:
        self.service.delete(_id)
