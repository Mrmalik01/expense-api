from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(user_name, password):
    user = UserModel.findByUserName(user_name)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.findById(user_id)

    

