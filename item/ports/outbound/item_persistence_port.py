from typing import List

from item.adapters.model.item_model import ItemModel
from item.adapters.outbound.item_persistence_adapter import ItemPersistenceAdapter


class ItemPersistencePort:
    def __init__(self, adapter=None):
        self.adapter = adapter or ItemPersistenceAdapter()

    def find_by_name(self, name: str) -> ItemModel:
        return self.adapter.find_by_name(name)

    def find_by_id(self, _id: int) -> ItemModel:
        return self.adapter.find_by_id(_id)

    def find_all(self) -> List[ItemModel]:
        return self.adapter.find_all()

    def create(self, name: str, price: float, image: str = None) -> ItemModel:
        return self.adapter.create(name, price, image)

    def update(self, _id: int, name: str, price: float, image: str = None) -> ItemModel:
        return self.adapter.update(_id, name, price, image)

    def delete(self, _id: int) -> None:
        self.adapter.delete(_id)
