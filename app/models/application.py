from app import db
from app.models.file import Applied
from datetime import datetime
from enum import Enum


class ApplicationStatusEnum(Enum):
    submitted = "SUBMITTED"
    planned = "PLANNED"
    viewed = "VIEWED"
    rejected = "REJECTED"
    interview = "INTERVIEW"
    accepted = "ACCEPTED"


class Application(db.Model):
    __tablename__ = "application"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    notes = db.Column(db.Text)
    recruiter = db.Column(db.String(100))
    status = db.Column(db.Enum(ApplicationStatusEnum), nullable=False, default=ApplicationStatusEnum.planned)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('applications', lazy=True))
    
    posting_id = db.Column(db.Integer, db.ForeignKey('posting.id'), nullable=False)
    posting = db.relationship('Posting', backref=db.backref('applications', lazy=True))

    files = db.relationship('File', secondary=Applied, lazy='subquery', backref=db.backref('applications', lazy=True))
    
    def __repr__(self):
        return f"<Application '{self.user.username}' for '{self.posting.position_title}' at '{self.posting.company.name.capitalize()}'>"
