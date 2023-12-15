from flask import jsonify
from managers.IdManager import IdManager

class UserManager():

  def __init__(self, IdManager:IdManager ) -> None:
    self.Id: IdManager = IdManager
    self.users: list[dict] = []

  def getUser(self, user_id:int):
    return next((user for user in self.users if user["id"] == user_id), None)
  
  def userExists(self, user_id:int) -> bool:
    user = self.getUser(user_id)
    if user:
      return True
    elif not user:
      return False

  
  def getUserIndex(self, user_id:int) -> int:
    return next((index for index, user in enumerate(self.users) if user["id"] == user_id), None)
  
  def getUsers(self, returnAsJson:bool) -> list[dict]:
    if returnAsJson:
      return jsonify(self.users)
    else:
      return self.users
  
  def createUser(self, data:dict, returnNewUser:bool, returnAsJson:bool):
    new_user = {
        "id":self.Id.genId(),
        "name":data["name"],
        "lastname":data["lastname"]
      }
    self.users.append(new_user)

    if returnNewUser and returnAsJson:
      return jsonify(new_user)
    elif returnNewUser and not returnAsJson:
      return new_user
    else:
      pass

  def patchUser(self, user_id:int, data:dict):
    userIndex = self.getUserIndex(user_id)
  
    self.users[userIndex]['name'] = str(data['name'])
    self.users[userIndex]['lastname'] = str(data['lastname'])