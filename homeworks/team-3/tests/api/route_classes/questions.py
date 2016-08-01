from flask.ext.restful import Resource
from common.test_service import (get_main_questions,
                                 new_main_question,
                                 get_main_question,
                                 remove_main_question,
                                 update_main_question
                                 )


class MainQuestions(Resource):
    def get(self, id_test):
        return get_main_questions(id_test)

    def post(self, id_test):
        new_main_question(id_test)
        pass


class MainQuestion(Resource):
    def get(self, id_test, id_question):
        return get_main_question(id_test, id_question)

    def delete(self, id_test, id_question):
        remove_main_question(id_test, id_question)
        pass

    def put(self, id_test, id_question):
        update_main_question(id_test, id_question)
        pass
