from flask import jsonify
from src.managers.IdManager import generateId

class UserManager():

  def __init__(self) -> None:
    self.users = []

  def getUser(self, user_id:int):
    return next((user for user in self.users if user["id"] == user_id), None)
  
  def getUsers(self, returnAsJson:bool):
    if jsonify:
      return jsonify(self.users)
    else:
      return self.users
  
  def createUser(self, data:dict, returnNewUser:bool, returnAsJson:bool):
    new_user = {
        "id":generateId(self.users),
        "name":data["name"],
        "lastname":data["lastname"]
      }
    self.users.append(new_user)

    if (returnNewUser, returnAsJson) == (True, True):
      return jsonify(new_user)
    

    
    match (returnNewUser, returnAsJson):
      case True, True:
        return jsonify(new_user)
      case False, True:
        pass
      case True, False:
        return new_user
      case False, False:
        pass