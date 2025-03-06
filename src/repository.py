import json
from http import HTTPStatus

class UserRepository:
    @staticmethod
    def get_user(user_id:int=None) -> list:
        with open('./src/users.json','r') as f:
            users = json.load(f)
        if user_id != None:
            for i in range(len(users)):
                if  users[i]["id"] == user_id:
                    return users[i],HTTPStatus.ACCEPTED
            else:
                return HTTPStatus.BAD_REQUEST
        return users,HTTPStatus.ACCEPTED
    @staticmethod
    def add_user(user:dict) -> None:
        with open('./src/users.json','r') as f:
            users = json.load(f)
        new_id = len(users)
        for i in range(len(users)-1):
            if (users[i]["id"] + 1) != (users[i+1]["id"]):
                new_id = users[i]["id"] + 1
                break
        user["id"] = new_id
        users.append(user)
        with open('./src/users.json','w') as f:
            json.dump(users,f)
        return HTTPStatus.ACCEPTED
            
    @staticmethod
    def edit_user(user:dict,user_id:int):
        with open('./src/users.json','r') as f:
            users = json.load(f)
        id_in_users = False
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                edit_user_id = i
                id_in_users = True
                break
        if id_in_users == False:
            return HTTPStatus.BAD_REQUEST
        try:
            users[edit_user_id]["firstName"] = user["firstName"]
            users[edit_user_id]["lastName"] = user["lastName"]
            users[edit_user_id]["age"] = user["age"]
            users[edit_user_id]["group"] = user["group"]
            with open('./src/users.json','w') as f:
                json.dump(users,f)
            return HTTPStatus.ACCEPTED
        except:
            return HTTPStatus.BAD_REQUEST
        
    @staticmethod
    def delete_user(user_id:int):
        with open('./src/users.json','r') as f:
            users = json.load(f)
        id_in_users = False
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                delete_user_id = i
                id_in_users = True
                break
        if id_in_users == False:
            return HTTPStatus.BAD_REQUEST
        elif id_in_users == True:
            users.pop(delete_user_id)
            with open('./src/users.json','w') as f:
                json.dump(users,f)
            return HTTPStatus.ACCEPTED