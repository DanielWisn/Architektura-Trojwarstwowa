from repository import UserRepository

class UserController:
    def __init__(self, repository : UserRepository) -> None:
        self._repository = repository
    
    def get_user(self,user_id:int=None) -> list:
        if user_id == None:
            return self._repository.get_user()
        else:
            return self._repository.get_user(user_id=user_id)

    
