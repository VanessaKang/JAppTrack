from app import db
from datetime import datetime
import enum

class Posting(db.Model):
    __tablename__ = "posting"

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    company = db.relationship('Company', backref=db.backref('postings', lazy=True))
    # url = db.Column(db.String(200))
    # deadline = db.Column(db.DateTime)
    # position_title = db.Column(db.String(100), nullable=False)
    # location = db.Column(db.String(100))
    # source = db.Column(db.String(100), nullable=False)
    # notes = db.Column(db.String(250))
    # path = db.Column(db.String(100))
    # skills = db.Column(db.String(100))
    # experience = db.Column(db.Integer)
    # salary = db.Column(db.Integer)

    def __repr__(self):
        return f"<Posting '{self.id}'>"

class Company(db.Model):
    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    
    def __init__(self, **kwargs):
        super(Company, self).__init__(**kwargs)

        # Ensure uniqueness by lowercasing strings
        if isinstance(self.name, str):
            self.name = self.name.lower()
        
    def __repr__(self):
        return f"<Company '{self.name}'>"

# class InterviewStatusEnums(enum.Enum):
#     scheduled = 'SCHEDULED'
#     attended = 'ATTENDED'
#     cancelled = 'CANCELLED'
#     passed = 'PASSED'
#     failed = 'FAILED'


# class Interview(db.Model):
#     __tablename__ = "interview"

#     id = db.Column(db.Integer, primary_key=True)
#     application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
#     application = db.relationship('Application', backref=db.backref('interviews', lazy=True))
#     date = db.Column(db.DateTime, nullable=False)
#     status = db.Column(db.Enum(InterviewStatusEnums), nullable=False, default=InterviewStatusEnums.scheduled)
#     type = db.Column(db.String(30), nullable=False)
#     notes = db.Column(db.String(250))

#     def __repr__(self):
#         return f"<Interview '{self.application_id}' '{self.type}'>"

# class ApplicationMethodEnums(enum.Enum):
#     linkedIn = "LINKEDIN"

# class Application(db.Model):
#     __tablename__ = "application"

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     user = db.relationship('User', backref=db.backref('applications', lazy=True))
#     posting_id = db.Column(db.Integer, db.ForeignKey('posting.id'), nullable=False)
#     posting = db.relationship('Posting', backref=db.backref('applications', lazy=True))
#     method = db.Column(db.Enum(ApplicationMethodEnums), nullable=False, default=ApplicationMethodEnums.linkedIn)
    