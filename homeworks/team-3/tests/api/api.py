import os
from flask import Flask, request, redirect
from flask_restful import Resource, Api
from common.test_service import get_main_questions, new_main_question, get_main_question, remove_main_question

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


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


# def put(self, id_question):
#         update_create(id_question)
#         pass


api.add_resource(MainQuestions, '/questions')
api.add_resource(MainQuestion, '/questions/<id_question>')

if __name__ == '__main__':
    app.run()
