from difflib import IS_CHARACTER_JUNK
from wsgiref import validate
from app import db
from app.models import BaseModel, ModelValidationException
from sqlalchemy.orm import validates
from enum import Enum
from datetime import datetime


class FileTypeEnum(Enum):
    resume = "RESUME"
    cover_letter = "COVER LETTER"
    reference = "REFERENCE"
    letter_of_recommendation = "LETTER OF RECOMMENDATION"
    transcript = "TRANSCRIPT"
    porfolio = "PORTFOLIO"
    other = "OTHER"
    

Applied = db.Table('applied',
    db.Column('file_id', db.Integer, db.ForeignKey('file.id'), primary_key=True),
    db.Column('application_id', db.Integer, db.ForeignKey('application.id'), primary_key=True)
)

class File(BaseModel):
    __tablename__ = "file"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(FileTypeEnum), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('files', lazy=True))

    @validates('user')
    def validate_name(self, key, user):
        if File.query.filter_by(name=self.name, is_active=True, user=user).first():
            raise ModelValidationException("File name for this user already exists.")
        return user
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name)

    @classmethod
    def find_active(cls):
        return cls.query.filter_by(is_active=True)
    
    def set_inactive(self):
        self.is_active = False

    def __repr__(self):
        return f"<File {self.name} for {self.user.username}>"