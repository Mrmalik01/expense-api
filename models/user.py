from db import db
from models.account import AccountModel

class UserModel(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email_address = db.Column(db.String(80))
    username = db.Column(db.String(80))
    phone_number = db.Column(db.String(80))
    accounts = db.relationship("AccountModel", lazy='dynamic')

    def __init__(self, full_name, password, username):
        self.full_name = full_name
        self.password = password
        self.username = username


    def json(self):
        return { 
            "full_name":self.full_name,
            "username":self.username,
            "password":self.password,
            "accounts:":[account.json for account in self.accounts] 
        }
    @classmethod
    def findById(cls, _id):
        return cls.query.filter_by(id=_id).first()
        
    @classmethod
    def findByUserName(cls, username):
        return cls.query.filter_by(username = username).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    