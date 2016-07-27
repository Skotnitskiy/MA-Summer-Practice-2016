import os
from flask import Flask
from flask_restful import Api
from route_classes.questions import MainQuestions, MainQuestion

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(MainQuestions, '/questions')
api.add_resource(MainQuestion, '/questions/<id_question>')

if __name__ == '__main__':
    app.run()
