import werkzeug
from flask_restful import reqparse


class CreateItemDto:
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        location='form',
        help="The field 'name' cannot be left blank!",

    )
    parser.add_argument(
        'price',
        type=float,
        required=True,
        location='form',
        help="This field 'price' cannot be left blank!"
    )
    parser.add_argument(
        'image',
        type=werkzeug.datastructures.FileStorage,
        required=False,
        location='files',
    )
