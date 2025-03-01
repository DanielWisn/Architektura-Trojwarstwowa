from repository import UserRepository
from datetime import date

current_year = date.today().year

class UserController:
    def __init__(self, repository : UserRepository) -> None:
        self._repository = repository
    
    def get_user(self,user_id:int=None) -> list:
        if user_id == None:
            return self._repository.get_user()
        else:
            return self._repository.get_user(user_id=user_id)

    def add_user(self,user:dict):
        try:
            if user["lastName"] == None or user["firstName"] == None or user["birthYear"] == None or user["group"] == None:
                return 400
        except:
            return 400
        user["age"] = current_year - user["birthYear"]
        del user["birthYear"]
        return self._repository.add_user(user)

    def edit_user(self,user:dict,user_id:int):
        try:
            if user["lastName"] == None or user["firstName"] == None or user["age"] == None or user["group"] == None:
                return 400
        except:
            return 400
        return self._repository.edit_user(user,user_id)

    def delete_user(self,user_id:int):
        return self._repository.delete_user(user_id)