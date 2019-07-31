from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel

class UserRegistry(Resource):

    help_msg = "This field is required"
    parser = reqparse.RequestParser()
    parser.add_argument("full_name", type=str, help=help_msg)
    parser.add_argument("password", type=str, help=help_msg)
    parser.add_argument("username", type=str, help=help_msg)

    # POST /register - for creating new user in the database
    def post(self):
        data = UserRegistry.parser.parse_args()
        username = data['username']
        user = UserModel.findByUserName(username)
        if user:
            return {"message":"This username is taken"}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {"message":"User account created"}


class User(Resource):

    help_msg = "this field is required"
    parser = reqparse.RequestParser()
    parser.add_argument("full_name", type=str, help=help_msg)
    parser.add_argument("password", type=str, help=help_msg)

    # GET /user/<username>
    def get(self, username):
        user = UserModel.findByUserName(username)
        if user:
            return user.json()
        return {"message":"User does not exist in the system"}

    @jwt_required()
    # DELETE /user/<username>
    def delete(self,username):
        user = UserModel.findByUserName(username)
        if user:
            try:
                user.delete_from_db()
                return {"message":"User deleted"}
            except:
                return {"message":"Error while deleting user from the database"}
        else:
            return {"message":"User does not exist"}


