from flask import Flask
from flask_restful import Resource, Api
from resources.user import User, UserRegistry
from resources.account import Account, AccountRegistry, Transaction
from flask_jwt import JWT
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = "ItIsSecret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

jwt = JWT(app, authenticate, identity)

@app.before_first_request
def create_all_tables():
    db.create_all()

print("Working")

api.add_resource(Account, '/account/<string:username>')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UserRegistry, '/register')
api.add_resource(AccountRegistry,'/account-register')
api.add_resource(Transaction,'/transaction')

if __name__ == "__main__":
    import os
    from db import db
    db.init_app(app)
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)

