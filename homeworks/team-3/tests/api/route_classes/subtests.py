from flask.ext.restful import Resource
from common.test_service import get_subtests, new_subtest, get_subtest, remove_subtest, new_sub_questions


class SubTests(Resource):
    def get(self, id_test):
        return get_subtests(id_test)

    def post(self, id_test):
        new_subtest(id_test)
        pass

class SubTest(Resource):
    def get(self, id_test, subtest_key):
        return get_subtest(id_test, subtest_key)

    def delete(self, id_test, subtest_key):
        remove_subtest(id_test, subtest_key)
        pass

    def post(self, id_test):
        new_sub_questions(id_test)
        pass
