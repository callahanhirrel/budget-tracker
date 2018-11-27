from flask import render_template, url_for, flash, redirect, request
from src import app, db, bcrypt
from src.forms import RegistrationForm, LoginForm, UpdateAccountForm
from src.models import User
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image

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
        user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                    email=form.email.data.lower(), password=hashed_pw, occupation=form.occupation.data,
                    department=form.department.data, is_dept_chair=form.is_dept_chair.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.first_name.data} {form.last_name.data}.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/home")
@login_required
def home():
    return render_template('home.html', title='Budgets in Real Time Home')

# This function is used to update a user's profile image.
# Returns the new random-hex-ified profile image filename
def save_img(form_img):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_img.filename)  # use '_' as a variable name since we aren't using the variable
    new_img_filename = random_hex + file_ext
    img_path = os.path.join(app.root_path, 'static/profile_pictures', new_img_filename)
    output_size = (125, 125)
    img = Image.open(form_img)
    img.thumbnail(output_size)
    img.save(img_path)
    return new_img_filename

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    # TODO fix this snarky lil bug (Issue #5)
    img_file = url_for('static', filename=f'profile_pictures/{current_user.img_file}')
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.img.data:
            new_img_file = save_img(form.img.data)
            current_user.img_file = new_img_file
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data.lower()
        db.session.commit()
        flash('Account successfully updated.', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
        form.department.data = current_user.department
        form.occupation.data = current_user.occupation
        form.is_dept_chair.data = current_user.is_dept_chair
    return render_template('account.html', title='My Account', form=form, img_file=img_file)

@app.route("/logout")
def logout():
    logout_user()
    # Since the login page serves as the `main` page, we will redirect there upon logout.
    return redirect(url_for('login'))
