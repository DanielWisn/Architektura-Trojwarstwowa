from src.repository import UserRepository
from src.controller import UserController
from pytest import fixture
import json
from unittest.mock import Mock
from datetime import date


@fixture(autouse=True,scope="module")
def clear_users_json():
    with open('./src/users.json','r') as f:
        USERS_BEFORE_TESTS = json.load(f)
    yield
    with open('./src/users.json','w') as f:
        json.dump(USERS_BEFORE_TESTS,f)

@fixture
def repository() -> Mock:
    return Mock(UserRepository)

@fixture
def controller(repository: Mock) -> UserController:
    return UserController(repository=repository)

def test_UserController_get_user_returns_from_repository(controller:UserController, repository: Mock) -> None:
    repository.get_user.return_value = {"firstName":"Test","lastName":"User","age":22,"group":"admin","id":232}
    actual = controller.get_user(user_id=232)
    expected = {"firstName":"Test","lastName":"User","age":22,"group":"admin","id":232}
    assert expected == actual


def test_UserController_add_user_returns_error_from_repository(controller:UserController) -> None:
    assert 400 == controller.add_user({"firstName":"Test","lastName":"User","age":22,"group":"admin"})

def test_UserController_calculate_age(controller:UserController) -> None:
    pass


def test_UserController_add_user_returns_from_repository(controller:UserController, repository: Mock) -> None:
    repository.add_user.return_value = 201
    actual = controller.add_user({"firstName":"Test","lastName":"User","group":"admin","birthYear":2000})
    expected = 201
    assert expected == actual