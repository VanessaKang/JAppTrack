from app import db
from enum import Enum


class InterviewTypeEnum(Enum):
    coding = "CODING"
    system_design = "SYSTEM DESIGN"
    pair_programming = "PAIR PROGRAMMING"
    behavioural = "BEHAVIOURAL"
    phone_interview = "PHONE INTERVIEW"
    

class InterviewStatusEnums(Enum):
    pending = "PENDING"
    scheduled = 'SCHEDULED'
    attended = 'ATTENDED'
    cancelled = 'CANCELLED'
    passed = 'PASSED'
    failed = 'FAILED'


class Interview(db.Model):
    __tablename__ = "interview"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    status = db.Column(db.Enum(InterviewStatusEnums), nullable=False, default=InterviewStatusEnums.pending)
    type = db.Column(db.Enum(InterviewTypeEnum), nullable=False)
    notes = db.Column(db.Text)

    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
    application = db.relationship('Application', backref=db.backref('interviews', lazy=True))

    def __repr__(self):
        # "Interview for SDE at Amazon (technical)"
        return f"<Interview for '{self.application.posting.position_title}' at '{self.application.posting.company.name.capitalize()}' ('{self.type.value}') >"
