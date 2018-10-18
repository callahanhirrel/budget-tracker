# This is the main Flask file for the budget tracker

from flask import Flask, render_template, url_for

app = Flask(__name__)

### Idea: put login on home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return None  # will eventually be render_template()

@app.route("/register")
def register():
    # form = RegistrationForm()
    return None  # will eventually be render_template()

@app.route("/login")
def login():
    # form = LoginForm()
    return None  # will eventually be render_template()




# We include this conditional so we can run this script
# directly using Python if we wish, as opposed to using
# environment variables in our virtual environment.
# (i.e. using 'python budget_tracker.py' instead of
# 'flask run' in terminal/command prompt)
if __name__ == "__main__":
    app.run(debug=True)
