from flask import request

from .test_crud import (main_questions,
                        update_create,
                        acquire_main_question,
                        delete_main_question,
                        tests_all,
                        test_save,
                        test,
                        delete_test,
                        save_main_questions,
                        subtests,
                        create_subtests,
                        subtest,
                        delete_subtest,
                        save_sub_questions,
                        subtest_results,
                        subtest_result,
                        delete_subtest_result, save_subtest_results)


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


def get_test(id_test):
    return test(id_test)


def remove_test(id_test):
    delete_test(id_test)
    pass


def new_main_questions(id_test):
    main_qs = request.json
    save_main_questions(id_test, main_qs)
    pass


def get_subtests(id_test):
    return subtests(id_test)


def new_subtests(id_test):
    subtests = request.json
    create_subtests(id_test, subtests)
    pass


def get_subtest(id_test, subtest_key):
    return subtest(id_test, subtest_key)


def remove_subtest(id_test, subtest_key):
    delete_subtest(id_test, subtest_key)
    pass


def new_sub_questions(id_test, subtest_key):
    sub_qs = request.json
    save_sub_questions(id_test, subtest_key, sub_qs)
    pass


def get_subtest_results(id_test, subtest_key):
    return subtest_results(id_test, subtest_key)


def get_subtest_result(id_test, subtest_key, person_key):
    return subtest_result(id_test, subtest_key, person_key)


def new_subtest_results(id_test, subtest_key):
    results = request.json
    save_subtest_results(id_test, subtest_key, results)
    pass


def remove_subtest_result(id_test, subtest_key, person_key):
    delete_subtest_result(id_test, subtest_key, person_key)
    pass
