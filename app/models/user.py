from app import db
from app.models import BaseModel
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    # password_hash = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password_hash = self.set_password(self.password_hash)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() 
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_active(cls):
        return cls.query.filter_by(is_active=True).all()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<User '{self.username}'>"
