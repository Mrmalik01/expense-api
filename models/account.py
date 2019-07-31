from db import db

class AccountModel(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(80))
    balance = db.Column(db.String(80))
    currency = db.Column(db.String(80))
    user_name = db.Column(db.String(80), db.ForeignKey("users.username"))
    user = db.relationship("UserModel")

    def __init__(self, account_name, balance, currency, user_name, created_date, onHold):
        self.account_name = account_name
        self.balance = balance
        self.currency = currency
        self.user_name = user_name
        self.create_date = create_date
        self.onHold = onHold
    

    def json(self):
        return {
            "account_name":self.account_name,
            "balance":self.balance,
            "currency":self.currency,
            "user_name":self.user_name,
            "created_date":self.create_date,
            "on_hold":self.onHold
        }

    @classmethod
    def findAccountByAccountName(cls, accountname):
        return cls.query.filter_by(account_name=accountname)
    
    @classmethod
    def findAccountByUserName(cls, username):
        return cls.query.filter_by(user_name=username)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()