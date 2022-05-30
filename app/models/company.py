from app import db
from app.models import BaseModel


class Company(BaseModel):
    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    
    def __init__(self, **kwargs):
        super(Company, self).__init__(**kwargs)

        # Ensure uniqueness by lowercasing strings
        if isinstance(self.name, str):
            self.name = self.name.lower()
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def __repr__(self):
        return f"<Company '{self.name}'>"