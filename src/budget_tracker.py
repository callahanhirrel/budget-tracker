# This is the main Flask file for the budget tracker

from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '4c1b98566bb86432a39a8d5baa91d184'   # TODO temporary secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'     # set the database file location
db = SQLAlchemy(app)                                            # Create the instance of SQLAlchemy() we can interact with

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)         # 60 characters due to hashing
    # TODO relationships:
    #   rltshp = db.relationship('className', backref='reference in other table', lazy=True)
    #   foreign_key = db.Column(db.Integer, db.ForeignKey('table.column', nullable=False))

    def __repr__(self):
        return f"User('{self.last_name}', '{self.first_name}', '{self.email}')"

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # TODO if email/password combination matches that of a user:
        flash(f'Successfully logged in!', 'success')
        return redirect(url_for('home'))
        # TODO else, flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/about")
def about():
    return None  # will eventually be render_template()

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/home")
def home():
    return None  # will eventually be render_template()




# We include this conditional so we can run this script
# directly using Python if we wish, as opposed to using
# environment variables in our virtual environment.
# (i.e. using 'python budget_tracker.py' instead of
# 'flask run' in terminal/command prompt)
if __name__ == "__main__":
    app.run(debug=True)
