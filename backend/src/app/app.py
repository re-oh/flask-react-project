from flask import Flask, jsonify, request
from src.managers.IdManager import generateId
from src.managers.UserManager import UserManager
app = Flask(__name__)


users = UserManager()

@app.route('/users', methods=['GET'])
def get_users():
    OK_RESPONSE = 200
    return users.getUsers(returnAsJson=True), OK_RESPONSE

@app.route('/users/<int:user_id>', methods=['GET'])
def get_single_user(user_id):
    OK_RESPONSE = 200
    BAD_RESPONSE = 404
    user = users.getUser(user_id)
    if user:
      return user, OK_RESPONSE
    elif user == None:
      return f"invalid user id:{user_id}", BAD_RESPONSE
    
@app.route('/users', methods=['POST'])
def create_user():
    OK_RESPONSE = 200
    BAD_RESPONSE = 401
    data = request.get_json()

    if 'name' in data and 'lastname' in data:
      new_user = users.createUser(data, returnNewUser=True, returnAsJson=True)
      return new_user, OK_RESPONSE
    else:
      return f"invalid UserData:{jsonify(data)}", BAD_RESPONSE

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
  OK_RESPONSE = 204
  BAD_RESPONSE = 404
  data = request.get_json()

  if 'name' in data and 'lastname' in data and users.userExists(user_id):
    users.patchUser(user_id, data)
    return f"patched user {user_id}\n with new data {jsonify(data)}", OK_RESPONSE
  
  else:
    return f"Invalid user Id{user_id} data not patched", BAD_RESPONSE

@app.route('/users/<int:user_id>', methods=['PUT'])
def create_or_update_user(user_id):
    OK_RESPONSE = {
      "PATCHED":204,
      "CREATED":200
    }
    data = request.get_json()  

    if users.userExists(user_id):
      if 'name' in data and 'lastname' in data:
        users.patchUser(user_id, data)
        return f"patched user {user_id}\n with new data {jsonify(data)}", OK_RESPONSE['PATCHED']
  
      else:
        new_user = users.createUser(data, returnNewUser=True, returnAsJson=True)
        return new_user, OK_RESPONSE['CREATED']


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    OK_RESPONSE = 204
    users = (user for user in users if user["id"] != user_id)
    return f"removed user {user_id}", 204

if __name__ == '__main__':
    app.run(debug=True)
