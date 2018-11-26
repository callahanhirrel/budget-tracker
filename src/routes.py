from flask import render_template, url_for, flash, redirect, request
from src import app, db, bcrypt
from src.forms import RegistrationForm, LoginForm, UpdateAccountForm
from src.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next = request.args.get('next')
            # Fancy ternary conditional in our return statement
            # instruction_1 `if` condition `else` instruction_2
            return redirect(next) if next else redirect(url_for('home'))
        else:
            flash('Login was unsuccessful. Please check email and password and try again.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/about")
def about():
    return None  # will eventually be render_template()

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
@login_required
def home():
    return render_template('home.html', title='Budgets in Real Time Home')

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    # TODO fix this snarky lil bug (Issue #5)
    img_file = url_for('static', filename=f'profile_pictures/{current_user.img_file}')
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account successfully updated.', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='My Account', form=form, img_file=img_file)

@app.route("/logout")
def logout():
    logout_user()
    # Since the login page serves as the `main` page, we will redirect there upon logout.
    return redirect(url_for('login'))
