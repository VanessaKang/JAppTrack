from app import db
from enum import Enum
from sqlalchemy.orm import validates
from app.models import BaseModel, ModelValidationException


class PostingSourceEnum(Enum):
    linkedin = "LINKEDIN"
    referral = "REFERRAL"
    website = "COMPANY WEBSITE"
    recruiter = "RECRUITER"
    indeed = "INDEED"
    monster = "MONSTER"
    glassdoor = "GLASSDOOR"
    other = "OTHER"


class Posting(BaseModel):
    __tablename__ = "posting"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    deadline = db.Column(db.DateTime)
    position_title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    source = db.Column(db.Enum(PostingSourceEnum), nullable=False)
    notes = db.Column(db.Text)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    company = db.relationship('Company', backref=db.backref('postings', lazy=True))

    @validates("url")
    def validate_url(self, key, url):
        if Posting.query.filter_by(url=url).first():
            raise ModelValidationException("Posting exists.")
        return url

    def __repr__(self):
        return f"<Posting '{self.position_title}' at '{self.company.name.capitalize()}'>"
