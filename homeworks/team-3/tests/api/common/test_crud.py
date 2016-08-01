from .models import Test
from database import db_session as dbs


def update_create(id_test, id_q, json_question):
    body = Test.query.filter_by(id=id_test).first().body
    body['main-questions'].update({id_q: json_question})
    test = Test.query.filter_by(id=id_test).first()
    test.body = body
    dbs.add(test)
    dbs.commit()
    pass


def main_questions(test_id):
    return Test.query.filter_by(id=test_id).first().body['main-questions']


def main_question(test_id, id_question, json_question):
    return update_create(test_id, id_question, json_question)


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


def tests_all():
    return Test.query.all()


def test_save(title, body):
    test = Test(title, body)
    dbs.add(test)
    dbs.commit()
    pass


def test(id_test):
    return Test.query.filter_by(id=id_test).first().body


def delete_test(id_test):
    test = Test.query.filter_by(id=id_test).first()
    dbs.delete(test)
    dbs.commit()

def save_main_questions(id_test, main_qs):
    body = Test.query.filter_by(id=id_test).first().body
    body['main-questions'].update(main_qs)
    test = Test.query.filter_by(id=id_test).first()
    test.body = body
    dbs.add(test)
    dbs.commit()
    pass


def subtests(id_test):
    return Test.query.filter_by(id=id_test).first().body['next']

def create_subtest(id_test, subtest_key):
    body = Test.query.filter_by(id=id_test).first().body
    body['next'].update({subtest_key: {"results":{}, "questions":{}}})
    test = Test.query.filter_by(id=id_test).first()
    test.body = body
    dbs.add(test)
    dbs.commit()
    pass

def subtest(id_test, subtest_key):
    return Test.query.filter_by(id=id_test).first().body['next'][subtest_key]