import json
import delete_user_handler

delete_success_body = json.loads(open('../mock/delete_user.json').read())
delete_failure_body = json.loads(open('../mock/delete_user_fail.json').read())

def test_delete_success():
    response = delete_user_handler.create(delete_success_body, '')
    assert response['statusCode'] == 200

def test_delete_failure():
    response = delete_user_handler.create(delete_failure_body, '')
    assert response['statusCode'] == 403