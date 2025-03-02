from src.repository import UserRepository
from src.controller import UserController
from pytest import fixture
from unittest.mock import Mock
from datetime import date

@fixture
def repository() -> Mock:
    return Mock(UserRepository)

@fixture
def controller(repository: Mock) -> UserController:
    return UserController(repository=repository)

def test_UserController_get_user_returns_from_repository(controller:UserController, repository: Mock) -> None:
    repository.get_user.return_value = {"firstName":"Test","lastName":"User","age":22,"group":"admin","id":232}
    actual = controller.get_user()
    expected = {"firstName":"Test","lastName":"User","age":22,"group":"admin","id":232}
    assert expected == actual

def test_UserController_get_user_id_returns_from_repository(controller:UserController, repository: Mock) -> None:
    repository.get_user.return_value = {"firstName":"Test","lastName":"User","age":22,"group":"admin","id":232}
    actual = controller.get_user(user_id=232)
    expected = {"firstName":"Test","lastName":"User","age":22,"group":"admin","id":232}
    assert expected == actual

def test_UserController_add_user_returns_error_from_repository(controller:UserController) -> None:
    assert 400 == controller.add_user({"firstName":"Test","lastName":"User","age":22,"group":"admin"})

def test_UserController_calculate_age(controller:UserController) -> None:
    actual = controller.calculate_age(2000)
    expected = date.today().year - 2000
    assert expected == actual

def test_UserController_add_user_returns_from_repository(controller:UserController, repository: Mock) -> None:
    repository.add_user.return_value = 201
    actual = controller.add_user({"firstName":"Test","lastName":"User","group":"admin","birthYear":2000})
    expected = 201
    assert expected == actual

def test_UserController_patch_user_returns_from_repository(controller:UserController, repository: Mock) -> None:
    repository.edit_user.return_value = 202
    actual = controller.edit_user({"firstName":"Test","lastName":"User","group":"admin","age":25},200)
    expected = 202
    assert expected == actual

def test_UserController_patch_user_returns_error_from_repository(controller:UserController) -> None:
    assert 400 == controller.edit_user({"firstName":"Test","lastName":"User","age":22,"group":"admin"},None)

def test_UserController_delete_user_returns_from_repository(controller:UserController, repository: Mock) -> None:
    repository.delete_user.return_value = 203
    actual = controller.delete_user(200)
    expected = 203
    assert expected == actual

def test_UserController_delete_user_returns_error_from_repository(controller:UserController) -> None:
    assert 400 == controller.delete_user(None)