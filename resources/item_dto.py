from flask_restful import reqparse, fields


class CreateItemDto:
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
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="This field 'store_id' cannot be left blank!"
    )


class GetItemDto:
    resource_fields = {'name': fields.String, 'price': fields.Float, 'store_id': fields.Integer}
