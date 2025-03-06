from flask import Flask,jsonify
from flask.typing import ResponseReturnValue
from flask import request
from src.controller import UserController
from src.repository import UserRepository
from http import HTTPStatus


app = Flask(__name__)

@app.get("/users")
def get_users() -> ResponseReturnValue:
    repository = UserRepository()
    controller = UserController(repository=repository)
    return jsonify(controller.get_user()), HTTPStatus.OK

@app.get("/users/<int:id>")
def get_user(id: int) -> ResponseReturnValue:
    repository = UserRepository()
    controller = UserController(repository=repository)
    user = controller.get_user(user_id=id)
    if user == HTTPStatus.BAD_REQUEST:
        return jsonify(),HTTPStatus.BAD_REQUEST
    else:
        return jsonify(user), HTTPStatus.OK

@app.post("/users")
def post_user() -> ResponseReturnValue:
    repository = UserRepository()
    controller = UserController(repository=repository)
    user = request.json
    if controller.add_user(user) == HTTPStatus.ACCEPTED:
        return jsonify(),HTTPStatus.ACCEPTED
    else:
        return jsonify(),HTTPStatus.BAD_REQUEST

@app.patch("/users/<int:user_id>")
def patch_user(user_id:int) -> ResponseReturnValue:
    repository = UserRepository()
    controller = UserController(repository=repository)
    user = request.json
    if controller.edit_user(user,user_id) == HTTPStatus.ACCEPTED:
        return jsonify(),HTTPStatus.ACCEPTED
    else:
        return jsonify(),HTTPStatus.BAD_REQUEST

@app.delete("/users/<int:user_id>")
def delete_user(user_id:int) -> ResponseReturnValue:
    repository = UserRepository()
    controller = UserController(repository=repository)
    if controller.delete_user(user_id) == HTTPStatus.ACCEPTED:
        return jsonify(),HTTPStatus.ACCEPTED
    else:
        return jsonify(),HTTPStatus.BAD_REQUEST

if __name__ == '__main__':
    app.run()