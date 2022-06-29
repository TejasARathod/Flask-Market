import imp
import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__) # referring to the local python file we are working with
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # pointer for our database file
app.config['SECRET_KEY'] = '*************'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page" # redirecting to login page after get started
login_manager.login_message_category = "info"
from market import route
