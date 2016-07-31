from flask import request

from .test_crud import main_questions, update_create, acquire_main_question, delete_main_question, tests_all, test_save


def get_main_questions(test_id):
    return main_questions(test_id)


def new_main_question(id_test):
    key = request.args.get('key')
    json_question = request.json
    return update_create(id_test, key, json_question)


def get_main_question(id_test, id_q):
    return acquire_main_question(id_test, id_q)


def remove_main_question(id_test, id_q):
    delete_main_question(id_test, id_q)
    pass


def update_main_question(id_test, id_q):
    json_question = request.json
    return update_create(id_test, id_q, json_question)

def get_tests():
    return tests_all()

def new_test():
    title = request.args.get('title')
    body = request.json
    return test_save(title, body)