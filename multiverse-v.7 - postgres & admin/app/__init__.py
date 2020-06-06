from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)
app.config['SECRET_KEY'] = '2aaab7247ffd3e644c7d056cd115969f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:buba@localhost/socratica'
db = SQLAlchemy(app)



bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'



from app import routes
from flask_admin import Admin   
from flask_admin.contrib.sqla import ModelView
from .models import User

admin = Admin(app)
admin.add_view(ModelView(User, db.session))