from app import db
from app.models import BaseModel, application
from app.models.user import User
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
    date = db.Column(db.DateTime)
    status = db.Column(db.Enum(InterviewStatusEnum), nullable=False, default=InterviewStatusEnum.pending)
    type = db.Column(db.Enum(InterviewTypeEnum), nullable=False)
    notes = db.Column(db.Text)

    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
    application = db.relationship('Application', backref=db.backref('interviews', lazy=True))

    @classmethod
    def find_by_status(cls, status):
        return cls.query.filter_by(status=status)
    
    @classmethod
    def find_scheduled(cls):
        return cls.query.filter_by(status=InterviewStatusEnum.scheduled)

    def __repr__(self):
        # "Interview for SDE at Amazon (technical)"
        return f"<Interview for '{self.application.posting.position_title}' at '{self.application.posting.company.name.capitalize()}' ('{self.type.value}') >"
