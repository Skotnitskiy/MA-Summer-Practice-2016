import os
from flask import Flask, request, redirect
from flask_restful import Resource, Api
from testq import Test
from database import db_session as dbs

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


def update_create():
    js_question = request.json
    number = request.args.get('num')
    body = Test.query.first().body
    body['main-questions'].update({number: js_question})
    test = Test.query.first()
    test.body = body
    dbs.add(test)
    dbs.commit()
    pass


class MainQuestions(Resource):
    def get(self):
        return Test.query.first().body['main-questions']

    def post(self):
        update_create()
        return redirect('/questions')

    def put(self):
        update_create()
        pass


class MainQuestion(Resource):
    def get(self, id_question):
        return Test.query.first().body['main-questions'][id_question]


api.add_resource(MainQuestions, '/questions')
api.add_resource(MainQuestion, '/questions/<id_question>')

if __name__ == '__main__':
    app.run()
