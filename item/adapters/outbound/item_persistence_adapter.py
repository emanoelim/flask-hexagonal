from item.adapters.outbound.repository.item_repository import ItemRepository


class ItemPersistenceAdapter:
    """
    Deve implementar as funções conforme a porta ItemPersistencePort.
    """
    respository = ItemRepository()

    def find_by_name(self, name):
        return self.respository.find_by_name(name)

    def find_by_id(self, _id):
        return self.respository.find_by_id(_id)

    def find_all(self):
        return self.respository.find_all()

    def create(self, name, price, image=None):
        return self.respository.create(name, price, image)

    def update(self, _id, name, price, image=None):
        return self.respository.update(_id, name, price, image)

    def delete(self, _id):
        self.respository.delete(_id)
