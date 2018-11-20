from src import db

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
