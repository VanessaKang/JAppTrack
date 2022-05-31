from sqlalchemy.orm import validates
from app import db
from app.models import BaseModel, ModelValidationException


class Company(BaseModel):
    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    
    @validates('name')
    def validate_name(self, key, name):
        # Ensure uniqueness by lowercasing
        if isinstance(name, str):
            name = name.lower()
        if Company.query.filter_by(name=name).first():
            raise ModelValidationException("Company name is not unique.")
        return name
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def __repr__(self):
        return f"<Company '{self.name}'>"