from flask import render_template, url_for, flash, redirect
from flask import get_flashed_messages
from src import app, db, bcrypt
from src.forms import RegistrationForm, LoginForm
from src.models import User

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
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.first_name.data} {form.last_name.data}.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/home")
def home():
    return None  # will eventually be render_template()
