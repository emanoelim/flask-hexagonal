from item.application.exception.exception import ItemAlreadyExists, ItemNotFound
from item.ports.outbound.item_persistence_port import ItemPersistencePort


class ItemService:
    """
    Service que contém a lógica da aplicação. Não deve se comunicar diretamente com os adapters. Para salvar o Item,
    por exemplo, deve passar pela porta ItemPersistencePort.
    Por padrão, ItemPersistencePort utiliza o ItemPersistenceAdapter. Se for necessário utilizar outro adapter, deve
    ser definido ao instanciar a porta. Ex.: port = ItemPersistencePort(S3Adapter()).
    """
    port = ItemPersistencePort()

    def find_by_id(self, _id):
        item = self.port.find_by_id(_id)
        return item

    def find_all(self):
        return self.port.find_all()

    def create(self, name, price):
        if self.port.find_by_name(name):
            raise ItemAlreadyExists(message=f'An item with name {name} already exists.')
        item = self.port.create(name, price)
        return item

    def update(self, _id, name, price):
        item = self.port.find_by_id(_id)
        if not item:
            raise ItemNotFound()
        item = self.port.update(_id, name, price)
        return item

    def delete(self, _id):
        item = self.port.find_by_id(_id)
        if not item: 
            raise ItemNotFound()
        self.port.delete(_id)
