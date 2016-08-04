from flask.ext.restful import Resource
from common.test_service import get_subtest_results, new_subtest_results, get_subtest_result, remove_subtest_result


class Results(Resource):
    def get(self, id_test, subtest_key):
        return get_subtest_results(id_test, subtest_key)

    def post(self, id_test, subtest_key):
        new_subtest_results(id_test, subtest_key)
        pass


class Result(Resource):
    def get(self, id_test, subtest_key, person_key):
        return get_subtest_result(id_test, subtest_key, person_key)

    def delete(self, id_test, subtest_key, person_key):
        remove_subtest_result(id_test, subtest_key, person_key)
        pass
