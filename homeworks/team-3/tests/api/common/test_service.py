from .test_crud import main_questions, update_create, acquire_main_question, delete_main_question


def get_main_questions(test_id):
    return main_questions(test_id)


def new_main_question(request):
    id_test = request.args.get('tid')
    return update_create(id_test, None)


def get_main_question(request, id_q):
    id_test = request.args.get('tid')
    return acquire_main_question(id_test, id_q)


def remove_main_question(id_question, request):
    id_test = request.args.get('tid')
    delete_main_question(id_test, id_question)
    pass
