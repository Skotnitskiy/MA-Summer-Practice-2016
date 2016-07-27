from flask import request
from .test import Test
from database import db_session as dbs


def update_create(id_test, id_q):
    js_question = request.json
    body = Test.query.filter_by(id=id_test).first().body
    body['main-questions'].update({id_q: js_question})
    test = Test.query.filter_by(id=id_test).first()
    test.body = body
    dbs.add(test)
    dbs.commit()
    pass


def main_questions(test_id):
    return Test.query.filter_by(id=test_id).first().body['main-questions']


def main_question(test_id, id_question):
    return update_create(test_id, id_question)


def acquire_main_question(test_id, id_question):
    return Test.query.filter_by(id=test_id).first().body['main-questions'][id_question]


def delete_main_question(test_id, id_question):
    body = Test.query.filter_by(id=test_id).first().body
    body['main-questions'].pop(id_question, test_id)
    test = Test.query.filter_by(id=test_id).first()
    test.body = body
    dbs.add(test)
    dbs.commit()
    pass
