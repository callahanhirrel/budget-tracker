from src import db, login_manager
from flask_login import UserMixin
import enum

# This function helps the login manager load a user still in their session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# We will use this enum to represent departments in the database
class Departments(enum.Enum):
    bio = 'BIO'
    psych = 'PSYCH'
    admin = 'ADMIN'

# We want to inherit from both the database model and our login manager's UserMixin class
# User ~one -> zero or more~ Request
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)         # 60 characters due to hashing
    img_file = db.Column(db.String(100), nullable=False, default='default-user-icon.jpg')
    occupation = db.Column(db.String(30), nullable=False)       # professor, administrator, etc...
    department = db.Column(db.Enum(Departments), nullable=False)
    is_dept_chair = db.Column(db.Boolean, nullable=False, default=False)
    requests = db.relationship('Request', backref='requester', lazy=True)

    # TODO relationships:
    #   rltshp = db.relationship('className', backref='reference in other table', lazy=True)
    #   foreign_key = db.Column(db.Integer, db.ForeignKey('table.column', nullable=False))

    def __repr__(self):
        return f"User('{self.last_name}', '{self.first_name}', '{self.email}')"

# BudgetReport ~one -> many~ BudgetReportEntry
class BudgetReportEntry(db.Model):
    obj_code = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    original_budget = db.Column(db.Float(asdecimal=True), nullable=True)
    revised_budget = db.Column(db.Float(asdecimal=True), nullable=False)
    encumbered_amounts = db.Column(db.Float(asdecimal=True), nullable=False, default=0)
    mtd_activity = db.Column(db.Float(asdecimal=True), nullable=False, default=0)
    ytd_activity = db.Column(db.Float(asdecimal=True), nullable=False, default=0)
    #parent_report = db.Column(db.Integer, db.ForeignKey('budgetreport.id'), nullable=False)

# BudgetReport ~one -> many~ BudgetReportEntry
class BudgetReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.Enum(Departments), nullable=False)
    dept_code = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    #entries = db.relationship('BudgetReportEntry', backref='report', lazy=True)

# User ~one -> zero or more~ Request
class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    obj_code = db.Column(db.Integer, nullable=False)
    class_name = db.Column(db.String(20), nullable=False)
    class_code = db.Column(db.Integer(), nullable=False)
    request_text = db.Column(db.String(150), nullable=False)
    who_requested = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
