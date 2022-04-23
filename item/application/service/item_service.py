from item.application.exception.exception import ItemAlreadyExists, ItemNotFound
from item.ports.outbound.item_persistence_port import ItemPersistencePort
from item.ports.outbound.upload_port import UploadPort


class ItemService:
    """
    Service que contém a lógica da aplicação. Não deve se comunicar diretamente com os adapters. Para salvar o Item,
    por exemplo, deve passar pela porta ItemPersistencePort.
    Por padrão, ItemPersistencePort utiliza o ItemPersistenceAdapter. Se for necessário utilizar outro adapter, deve
    ser definido ao instanciar a porta. Ex.: persistence_port = ItemPersistencePort(S3Adapter()).
    """
    persistence_port = ItemPersistencePort()
    upload_port = UploadPort()

    def find_by_id(self, _id):
        item = self.persistence_port.find_by_id(_id)
        return item

    def find_all(self):
        return self.persistence_port.find_all()

    def create(self, name, price, image):
        if self.persistence_port.find_by_name(name):
            raise ItemAlreadyExists(message=f'An item with name {name} already exists.')

        item = self.persistence_port.create(name, price)

        if image:
            file_name = f'item/{item.id}/{image.filename}'
            image_url = self.upload_port.upload_file(image, file_name)
            item = self.persistence_port.update(item.id, name, price, image_url)
        return item

    def update(self, _id, name, price, image):
        item = self.persistence_port.find_by_id(_id)
        if not item:
            raise ItemNotFound()

        image_url = item.image
        if image:
            file_name = f'item/{_id}/{image.filename}'
            image_url = self.upload_port.upload_file(image, file_name) or image_url
        item = self.persistence_port.update(_id, name, price, image_url)
        return item

    def delete(self, _id):
        item = self.persistence_port.find_by_id(_id)
        if not item: 
            raise ItemNotFound()
        self.persistence_port.delete(_id)
