from flask_restful import Resource

class AccountRegistry(Resource):

    # POST /account-register/<username>
    def post(username):
        pass


class Account(Resource):

    # GET /account/<accountname>
    def get(accountname):
        pass

    # DELETE /account/<accountname>
    def delete(accountname):
        pass


class Transaction(Resource):

    # POST /transaction/<accountname>
    def post(accountname):
        pass