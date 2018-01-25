import json
import update_user_handler

update_success_body = json.loads(open('../mock/update_user.json').read())
update_failure_body = json.loads(open('../mock/update_user_fail.json').read())

def test_update_success():
    response = update_user_handler.create(update_success_body, '')
    assert response['statusCode'] == 200

def test_update_failure():
    response = update_user_handler.create(update_failure_body, '')
    assert response['statusCode'] == 403