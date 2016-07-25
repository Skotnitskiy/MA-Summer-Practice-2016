import os
from flask import Flask, request, redirect
from flask_restful import Resource, Api
from testq import Test
from database import db_session as dbs

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


def update_create(id_q):
    js_question = request.json
    if id_q == None:
        number = request.args.get('num')
    else:
        number = id_q
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
        update_create(None)
        return redirect('/questions')



class MainQuestion(Resource):
    def get(self, id_question):
        return Test.query.first().body['main-questions'][id_question]

    def delete(self, id_question):
        body = Test.query.first().body
        body['main-questions'].pop(id_question, None)
        test = Test.query.first()
        test.body = body
        dbs.add(test)
        dbs.commit()
        pass

    def put(self, id_question):
        update_create(id_question)
        pass


api.add_resource(MainQuestions, '/questions')
api.add_resource(MainQuestion, '/questions/<id_question>')

if __name__ == '__main__':
    app.run()
