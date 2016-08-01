import os
from flask import Flask
from unicode_api import UnicodeApi
from route_classes.questions import MainQuestions, MainQuestion
from route_classes.tests import Tests, Test
from route_classes.subtests import SubTests

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = UnicodeApi(app, prefix='/api/v1')

api.add_resource(MainQuestions, '/tests/<id_test>/questions')
api.add_resource(MainQuestion, '/tests/<id_test>/questions/<id_question>')
api.add_resource(Tests, '/tests')
api.add_resource(Test, '/tests/<id_test>', '/tests/<id_test>/main-questions')
api.add_resource(SubTests, '/tests/<id_test>/subtests')
