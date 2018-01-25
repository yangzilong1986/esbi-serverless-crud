import json
import get_user_handler

get_success_body = json.loads(open('../mock/get_user.json').read())
get_failure_body = json.loads(open('../mock/get_user_fail.json').read())

def test_get_success():
    response = get_user_handler.create(get_success_body, '')
    assert response['statusCode'] == 200

def test_get_failure():
    response = get_user_handler.create(get_failure_body, '')
    assert response['statusCode'] == 403