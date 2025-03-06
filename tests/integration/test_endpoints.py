from flask.testing import FlaskClient
from flask import Flask
from pytest import fixture
from http import HTTPStatus
from random import randint
from src.app import app
import json

@fixture(autouse=True,scope="module")
def clear_users_json():
    with open('./src/users.json','r') as f:
        USERS_BEFORE_TESTS = json.load(f)
    yield
    with open('./src/users.json','w') as f:
        json.dump(USERS_BEFORE_TESTS,f)

@fixture
def client() -> FlaskClient:
    return app.test_client()

def test_flask_app_exists() -> None:
    assert isinstance(app,Flask)

def test_get_users_endpoint(client: FlaskClient) -> None:
    result = client.get("users")
    assert result.status_code == HTTPStatus.OK

def test_get_users_endpoint(client: FlaskClient) -> None:
    result = client.get("users/1")
    assert result.status_code == HTTPStatus.OK

def test_get_users_endpoint_error_id(client: FlaskClient) -> None:
    result = client.get("users/423")
    assert result.status_code == HTTPStatus.BAD_REQUEST

def test_post_user_endpoint(client: FlaskClient) -> None:
    result = client.post("users",json={"firstName":"Test","lastName":"User","group":"admin","birthYear":2000})
    assert result.status_code == HTTPStatus.ACCEPTED

def test_post_user_endpoint_error_none(client: FlaskClient) -> None:
    result = client.post("users",json={"firstName":"Test","lastName":"User","group":"admin"})
    assert result.status_code == HTTPStatus.BAD_REQUEST

def test_post_user_endpoint_error_birthYear(client: FlaskClient) -> None:
    result = client.post("users",json={"firstName":"Test","lastName":"User","group":"admin","birthYear":2100})
    assert result.status_code == HTTPStatus.BAD_REQUEST

def test_post_user_endpoint_group_error_value(client: FlaskClient) -> None:
    result = client.post("users",json={"firstName":"Test","lastName":"User","group":"error","age":23})
    assert result.status_code == HTTPStatus.BAD_REQUEST

def test_patch_user_endpoint(client: FlaskClient) -> None:
    result = client.patch("users/2",json={"firstName":"Test","lastName":"User","group":"admin","age":10})
    assert result.status_code == HTTPStatus.ACCEPTED

def test_patch_user_endpoint_none_value(client: FlaskClient) -> None:
    result = client.patch("users/2",json={"firstName":"Test","lastName":"User","group":"admin"})
    assert result.status_code == HTTPStatus.BAD_REQUEST

def test_patch_user_endpoint_group_error_value(client: FlaskClient) -> None:
    result = client.patch("users/2",json={"firstName":"Test","lastName":"User","group":"error","age":23})
    assert result.status_code == HTTPStatus.BAD_REQUEST

def test_patch_user_endpoint_error_id(client: FlaskClient) -> None:
    result = client.patch("users/444",json={"firstName":"Test","lastName":"User","group":"admin","age":10})
    assert result.status_code == HTTPStatus.BAD_REQUEST

def test_delete_user(client) -> None:
    result = client.delete("/users/1")
    assert result.status_code == HTTPStatus.ACCEPTED


def test_delete_user_error_id(client) -> None:
    result = client.delete("/users/2320")
    assert result.status_code == HTTPStatus.BAD_REQUEST