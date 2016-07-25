import os

import sqlalchemy
from flask import Flask, jsonify
from flask_restful import Resource, Api
from testq import Test

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


class MainQuestions(Resource):
    def get(self):
        return Test.query.first().body['main-questions']


class MainQuestion(Resource):
    def get(self, id_question):
        return Test.query.first().body['main-questions'][id_question]


api.add_resource(MainQuestions, '/questions')
api.add_resource(MainQuestion, '/questions/<id_question>')

if __name__ == '__main__':
    app.run()
