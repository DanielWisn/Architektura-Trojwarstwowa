from src.repository import UserRepository
from pytest import fixture
import json
from http import HTTPStatus

@fixture(autouse=True,scope="module")
def clear_users_json():
    with open('./src/users.json','r') as f:
        USERS_BEFORE_TESTS = json.load(f)
    yield
    with open('./src/users.json','w') as f:
        json.dump(USERS_BEFORE_TESTS,f)

def get_user(lista:list[dict],key:"str",value:"str") -> dict:
    for i in lista:
        if i[key] == value:
             return i

def test_get_users():
    with open('./src/users.json','r') as f:
            users = json.load(f)

    assert UserRepository.get_user()[0] == users

def test_get_users_id():
    with open('./src/users.json','r') as f:
            users = json.load(f)
    assert UserRepository.get_user(0)[0] == get_user(users,"id",0)

def test_add_user():
    UserRepository.add_user({"firstName":"Test","lastName":"User","age":22,"group":"admin"})
    with open('./src/users.json','r') as f:
            users = json.load(f)
    answer = get_user(users,"firstName","Test")
    assert  None != answer

def test_edit_user():
    with open('./src/users.json','r') as f:
            users = json.load(f)
    users.append({"id":200})
    with open('./src/users.json','w') as f:
            json.dump(users,f)
    UserRepository.edit_user({"firstName":"Test","lastName":"User","age":22,"group":"admin"},200)
    with open('./src/users.json','r') as f:
            users = json.load(f)
    answer = get_user(users,"id",200)
    assert {"firstName":"Test","lastName":"User","age":22,"group":"admin","id":200} == answer

def test_edit_user_error_id():
    assert UserRepository.edit_user({"firstName":"Test","lastName":"User","age":22,"group":"admin"},201) == HTTPStatus.BAD_REQUEST

def test_delete_user():
    with open('./src/users.json','r') as f:
            users = json.load(f)
    users.append({"id":500})
    with open('./src/users.json','w') as f:
            json.dump(users,f)
    UserRepository.delete_user(500)
    with open('./src/users.json','r') as f:
            users = json.load(f)
    answer = get_user(users,"id",500)
    assert None == answer

def test_delete_user_error():
    assert UserRepository.delete_user(305) == HTTPStatus.BAD_REQUEST