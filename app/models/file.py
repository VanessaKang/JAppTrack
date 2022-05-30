from app import db
from app.models import BaseModel
from enum import Enum


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
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('files', lazy=True))

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name)

    @classmethod
    def find_active(cls):
        return cls.query.filter_by(is_active=True)
    
    def __repr__(self):
        return f"<File {self.name} for {self.user.username}>"