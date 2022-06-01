from app import db
from app.models import BaseModel, ModelValidationException, application
from app.models.user import User
from sqlalchemy.orm import validates
from sqlalchemy import and_
from enum import Enum



class InterviewTypeEnum(Enum):
    coding = "CODING"
    system_design = "SYSTEM DESIGN"
    pair_programming = "PAIR PROGRAMMING"
    behavioural = "BEHAVIOURAL"
    phone_interview = "PHONE INTERVIEW"
    

class InterviewStatusEnum(Enum):
    pending = "PENDING"
    scheduled = 'SCHEDULED'
    attended = 'ATTENDED'
    cancelled = 'CANCELLED'
    passed = 'PASSED'
    failed = 'FAILED'


class Interview(BaseModel):
    __tablename__ = "interview"

    id = db.Column(db.Integer, primary_key=True)
    scheduled_date = db.Column(db.DateTime)
    status = db.Column(db.Enum(InterviewStatusEnum), nullable=False, default=InterviewStatusEnum.pending)
    type = db.Column(db.Enum(InterviewTypeEnum), nullable=False)
    notes = db.Column(db.Text)

    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
    application = db.relationship('Application', backref=db.backref('interviews', lazy=True))

    @validates("status")
    def validate_interview_status(self, key, status):
        if status != InterviewStatusEnum.pending and self.scheduled_date is None:
            raise ModelValidationException("Date required for scheduled interviews.")
        return status
    
    @validates("application")
    def validate_scheduled_date(self, key, application):
        if Interview.query.filter(and_(Interview.application == application, Interview.scheduled_date >= self.scheduled_date)).all():
            raise ModelValidationException("This interview cannot be scheduled before previous interviews.")
        return application

    @classmethod
    def find_by_status(cls, status):
        return cls.query.filter_by(status=status)
    
    @classmethod
    def find_scheduled(cls):
        return cls.query.filter_by(status=InterviewStatusEnum.scheduled)

    def __repr__(self):
        # "Interview for SDE at Amazon (technical)"
        return f"<Interview for '{self.application.posting.position_title}' at '{self.application.posting.company.name.capitalize()}' ('{self.type.value}') >"
