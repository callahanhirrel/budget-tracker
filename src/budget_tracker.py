# This is the main Flask file for the budget tracker

from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# TODO temporary secret key
app.config['SECRET_KEY'] = '4c1b98566bb86432a39a8d5baa91d184'

@app.route("/")
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route("/about")
def about():
    return None  # will eventually be render_template()

@app.route("/register")
def register():
    form = RegistrationForm()
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
