from item.adapters.outbound.item_persistence_adapter import ItemPersistenceAdapter


class ItemPersistencePort:
    def __init__(self, adapter=None):
        self.adapter = adapter or ItemPersistenceAdapter()

    def find_by_name(self, name):
        return self.adapter.find_by_name(name)

    def find_by_id(self, _id):
        return self.adapter.find_by_id(_id)

    def find_all(self):
        return self.adapter.find_all()

    def create(self, name, price):
        return self.adapter.create(name, price)

    def update(self, _id, name, price):
        return self.adapter.update(_id, name, price)

    def delete(self, _id):
        self.adapter.delete(_id)
