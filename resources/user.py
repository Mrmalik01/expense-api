from flask_restful import Resource, reqparse

class UserRegistry(Resource):
    # POST /register - for creating new user in the database
    def post():
        pass


class User(Resource):

    # GET /user/<username>
    def get(username):
        pass

    # SET /user/<username>
    def set(username):
        pass

    # DELETE /user/<username>
    def delete(username):
        pass
