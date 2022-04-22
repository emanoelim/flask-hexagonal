from flask_restful import reqparse


class CreateItemDto:
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help="The field 'name' cannot be left blank!"
    )
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field 'price' cannot be left blank!"
    )
