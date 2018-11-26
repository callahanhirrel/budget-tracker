from src import db, login_manager
from flask_login import UserMixin

# This function helps the login manager load a user still in their session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# We want to inherit from both the database model and our login manager's UserMixin class
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)         # 60 characters due to hashing
    img_file = db.Column(db.String(100), nullable=False, default='default-user-icon.jpg')
    # TODO relationships:
    #   rltshp = db.relationship('className', backref='reference in other table', lazy=True)
    #   foreign_key = db.Column(db.Integer, db.ForeignKey('table.column', nullable=False))

    def __repr__(self):
        return f"User('{self.last_name}', '{self.first_name}', '{self.email}')"
