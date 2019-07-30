from flask import Flask
from flask_restful import Resource, Api
from resources.user import User, UserRegistry
from resources.account import Account, AccountRegistry, Transaction

app = Flask(__name__)
app.secret_code = "ItIsSecret"
api = Api(app)







print("Working")

api.add_resource(User, '/user')
api.add_resource(UserRegistry, '/register')
api.add_resource(Account, '/account')
api.add_resource(AccountRegistry,'/account-register')
api.add_resource(Transaction,'/transaction')

if __name__ == "main":
    app.run(PORT=5000)
