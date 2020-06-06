from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=True, nullable=False)
    surname = db.Column(db.String(20), unique=True, nullable=False)
    enterdate = db.Column(db.String(20), unique=True, nullable=False)
    company = db.Column(db.String(20), unique=True, nullable=False)
    companytype = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    county = db.Column(db.String(20), unique=True, nullable=False)
    city = db.Column(db.String(20), unique=True, nullable=False)
    phonenumber = db.Column(db.String(20), unique=True, nullable=False) 

    def __repr__(self):
        return f"User('{self.firstname}', '{self.email}')"
