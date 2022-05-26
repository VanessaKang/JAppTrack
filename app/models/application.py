from app import db

class Application(db.Model):
    __tablename__ = "application"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('applications', lazy=True))
    
    posting_id = db.Column(db.Integer, db.ForeignKey('posting.id'), nullable=False)
    posting = db.relationship('Posting', backref=db.backref('applications', lazy=True))

    def __repr__(self):
        return f"<Application '{self.user.username}' for '{self.posting.position_title}' at '{self.posting.company.name.capitalize()}'>"
