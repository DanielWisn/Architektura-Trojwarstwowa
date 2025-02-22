from flask import Flask
from controller import UserController
from repository import UserRepository


app = Flask(__name__)

@app.get("/users")
def get_users() -> None:
    repository = UserRepository()
    controller = UserController(repository=repository)
    return controller.get_user()

@app.get("/users/<int:id>")
def get_user(id: int) -> None:
    repository = UserRepository()
    controller = UserController(repository=repository)
    return controller.get_user(user_id=id)

if __name__ == '__main__':
    app.run()