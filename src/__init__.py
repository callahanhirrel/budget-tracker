# Set up imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Create the instance of the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = '4c1b98566bb86432a39a8d5baa91d184'   # TODO temporary secret key
# Set the database file location to be in the same relative directory as this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Create the instance of SQLAlchemy() we can interact with
db = SQLAlchemy(app)
# Create an instance of Bcrypt() for password hashing
bcrypt = Bcrypt(app)

# Put this down here to avoid circular import issues
from src import routes
