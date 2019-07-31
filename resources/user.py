from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel

class UserRegistry(Resource):

    help_msg = "This field is required"
    parser = reqparse.RequestParser()
    parser.add_argument("full_name", type=str, help=help_msg)
    parser.add_argument("password", type=str, help=help_msg)
    parser.add_argument("email_address", type=str, help=help_msg)
    parser.add_argument("user_name", type=str, help=help_msg)
    parser.add_argument("phone_number", type=str, help=help_msg)
    # POST /register - for creating new user in the database
    @jet_required()
    def post():
        data = parser.parse()
        user_name = data['user_name']
        user = UserModel.findByUserName(user_name)
        if user:
            return {"message":"This username is taken"}, 400
        user = UserModel(*data)
        user.save_to_db()
        return user


class User(Resource):

    help_msg = "this field is required"
    parser = reqparse.RequestParser()
    parser.add_argument("full_name", type=str, help=help_msg)
    parser.add_argument("password", type=str, help=help_msg)
    parser.add_argument("email_address", type=str, help=help_msg)
    parser.add_argument("phone_number", type=str, help=help_msg)
    # GET /user/<username>
    def get(username):
        user = UserModel.findByUserName(username)
        if user:
            return user.json()
        return {"message":"User does not exist in the system"}

    # SET /user/<username>
    def set(username):
        user = UserModel.findByUserName(username)
        if user:
            data = parser.parse()
            user.set(*data)
        else:
            user = UserModel(*data)
    

            

    # DELETE /user/<username>
    def delete(username):
        pass
