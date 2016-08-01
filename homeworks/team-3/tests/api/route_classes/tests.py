from flask.ext.restful import Resource, fields, marshal_with
from common.test_service import get_tests, new_test, get_test, remove_test, new_main_questions

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


class Test(Resource):
    def get(self, id_test):
        return get_test(id_test)

    def delete(self, id_test):
        remove_test(id_test)
        pass

    def post(self, id_test):
        new_main_questions(id_test)
        pass
