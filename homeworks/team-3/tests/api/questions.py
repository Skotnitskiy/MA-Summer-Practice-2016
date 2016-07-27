from flask.ext.restful import Resource
from flask import request
from common.test_service import (get_main_questions,
                                 new_main_question,
                                 get_main_question,
                                 remove_main_question,
                                 update_main_question
                                 )

class MainQuestions(Resource):
    def get(self):
        id_test = request.args.get('tid')
        return get_main_questions(id_test)

    def post(self):
        new_main_question(request)
        pass


class MainQuestion(Resource):
    def get(self, id_question):
        return get_main_question(request, id_question)

    def delete(self, id_question):
        remove_main_question(id_question, request)
        pass

    def put(self, id_question):
        update_main_question(request, id_question)
        pass

