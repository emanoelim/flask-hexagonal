from flask_restful import reqparse, fields


class CreateStoreDto:
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="The field 'name' cannot be left blank!"
    )


class GetStoreDto:
    resource_fields = {'name': fields.String}