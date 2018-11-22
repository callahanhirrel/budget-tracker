# Set up imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Create the instance of the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = '4c1b98566bb86432a39a8d5baa91d184'   # TODO temporary secret key
# Set the database file location to be in the same relative directory as this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Create the instance of SQLAlchemy() we can interact with
db = SQLAlchemy(app)
# Create an instance of Bcrypt() for password hashing
bcrypt = Bcrypt(app)
# Create an instance of LoginManager to help us manage user sessions
login_manager = LoginManager(app)
# Set the login view to redirect users to login page if they try to access
#  a page for which they need to be logged in to view
login_manager.login_view = 'login'  # Function name of login route
login_manager.login_message_category = 'info'

# Put this down here to avoid circular import issues
from src import routes
