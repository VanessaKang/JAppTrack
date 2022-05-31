from sqlalchemy.orm import validates
from app import db
from app.models.file import Applied
from app.models import BaseModel, ModelValidationException
from datetime import datetime
from enum import Enum


class ApplicationStatusEnum(Enum):
    planned = "PLANNED"
    submitted = "SUBMITTED"
    viewed = "VIEWED"
    rejected = "REJECTED"
    interview = "INTERVIEW"
    accepted = "ACCEPTED"


class Application(BaseModel):
    __tablename__ = "application"

    id = db.Column(db.Integer, primary_key=True)
    submission_date = db.Column(db.DateTime)
    notes = db.Column(db.Text)
    recruiter = db.Column(db.String(100))
    status = db.Column(db.Enum(ApplicationStatusEnum), nullable=False, default=ApplicationStatusEnum.planned)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('applications', lazy=True))
    
    posting_id = db.Column(db.Integer, db.ForeignKey('posting.id'), nullable=False)
    posting = db.relationship('Posting', backref=db.backref('applications', lazy=True))

    files = db.relationship('File', secondary=Applied, lazy='subquery', backref=db.backref('applications', lazy=True))

    @validates("status")
    def validate_submission_date(self, key, status):
        if status != ApplicationStatusEnum.planned and self.submission_date is None:
            raise ModelValidationException("Date is required for submitted applications")
        return status

    @classmethod
    def find_by_status(cls, status):
        return cls.query.filter_by(status=status)

    def __repr__(self):
        return f"<Application '{self.user.username}' for '{self.posting.position_title}' at '{self.posting.company.name.capitalize()}'>"
