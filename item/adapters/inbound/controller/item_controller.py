from flask_restful import Resource, marshal_with, abort

from item.application.exception.exception import ItemNotFound, ItemAlreadyExists
from item.adapters.dto.item_dto import CreateItemDto
from item.ports.inbound.item_service_port import ItemServicePort


class ItemController(Resource):
    """
    Controller Rest API.
    O controller não deve se comunicar diretamente com a camada application, deve passar por uma porta (ItemServicePort)
    """
    port = ItemServicePort()
    resource_fields = port.resource_fields

    @marshal_with(resource_fields, envelope='data')
    def get(self, id):
        """
        Get item by id
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
        responses:
          200:
            description: item
          404:
            description: item not found
        """
        item = self.port.find_by_id(id)
        if item:
            return item
        abort(404, message="Item not found.")

    def delete(self, id):
        """
        Delete item by id
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
        responses:
          200:
            description: item deleted
          404:
            description: item not found
        """
        try:
            self.port.delete(id)
            return {'message': 'Item deleted'}
        except ItemNotFound as e:
            abort(e.status_code, message=e.message)

    @marshal_with(resource_fields, envelope='data')
    def put(self, id):
        """
        Update item by id
        ---
        parameters:
          - name: name
            in: path
            type: string
            required: true
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                price:
                  type: number
        responses:
          200:
            description: item updated
          400:
            description: invalid data
          404: 
            description: item not found
        """
        data = CreateItemDto.parser.parse_args()
        try:
            item = self.port.update(id, **data)
            return item
        except ItemNotFound as e:
            abort(e.status_code, message=e.message)


class ItemListController(Resource):
    port = ItemServicePort()
    resource_fields = port.resource_fields

    @marshal_with(resource_fields, envelope='data')
    def get(self):
        """
        Get all items
        ---
        responses:
          200:
            description: items
        """
        items = self.port.find_all()
        return items
    
    @marshal_with(resource_fields, envelope='data')
    def post(self):
        """
        Create item
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                price:
                  type: number
        responses:
          201:
            description: item created
          400:
            description: invalid data
        """
        data = CreateItemDto.parser.parse_args()
        try:
            item = self.port.create(**data)
            return item, 201
        except ItemAlreadyExists as e:
            abort(e.status_code, message=e.message)
