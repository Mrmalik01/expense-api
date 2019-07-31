from db import db
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email_address = db.Column(db.String(80))
    user_name = db.Column(db.String(80))
    phone_number = db.Column(db.String(80))

    def __init__(self, full_name, password, email_address, user_name, phone_number):
        self.full_name = full_name
        self.password = password
        self.email_address = email_address
        self.user_name = user_name
        self.phone_number= phone_number

    def set(self, full_name, password, email_address, user_name, phone_number):
        self.full_name = full_name
        self.password = password
        self.email_address = email_address
        self.user_name = user_name
        self.phone_number= phone_number
        return True

    def json(self):
        return { 
                    "full_name":self.full_name,
                    "email_address":self.email_address,
                    "user_name":self.user_name,
                    "phone_number":self.phone_number 
                }
    @classmethod
    def findById(cls, _id):
        return cls.query.filter_by(id=_id).first()
        
    @classmethod
    def findByUserName(cls, username):
        return cls.query.filter_by(user_name = username).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    