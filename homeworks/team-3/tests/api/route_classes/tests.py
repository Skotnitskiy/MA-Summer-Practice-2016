from flask.ext.restful import Resource, fields, marshal_with
from common.test_service import get_tests, new_test

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
}


class Tests(Resource):
    @marshal_with(resource_fields, envelope='tests')
    def get(self):
        return get_tests()

    def post(self):
        new_test()
        pass
