from flask import request

from .test_crud import main_questions, update_create, acquire_main_question, delete_main_question


def get_main_questions(test_id):
    return main_questions(test_id)


def new_main_question(id_test):
    key = request.args.get('key')
    return update_create(id_test, key)


def get_main_question(id_test, id_q):
    return acquire_main_question(id_test, id_q)


def remove_main_question(id_test, id_q):
    delete_main_question(id_test, id_q)
    pass


def update_main_question(id_test, id_q):
    return update_create(id_test, id_q)