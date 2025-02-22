import json

class UserRepository:
    def get_user(self, user_id:int=None) -> list:
        with open('./src/users.json','r') as f:
            users = sorted(json.load(f), key=lambda x: x["id"])
        if user_id != None:
            for i in range(len(users)):
                if  users[i]["id"] == user_id:
                    return users[i]
        return users