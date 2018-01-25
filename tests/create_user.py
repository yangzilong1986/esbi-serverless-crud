import json
import create_user_handler

create_success_body = json.loads(open('../mock/create_user.json').read())
create_failure_body = json.loads(open('../mock/create_user_fail.json').read())

def test_create_success():
    response = create_user_handler.create(create_success_body, '')
    assert response['statusCode'] == 200

def test_create_failure():
    response = create_user_handler.create(create_failure_body, '')
    assert response['statusCode'] == 403