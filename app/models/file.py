from app import db


Applied = db.Table('applied',
    db.Column('file_id', db.Integer, db.ForeignKey('file.id'), primary_key=True),
    db.Column('application_id', db.Integer, db.ForeignKey('application.id'), primary_key=True)
)


class File(db.Model):
    __tablename__ = "file"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('applications', lazy=True))

    def __repr__(self):
        return f"<File {self.name} for {self.user.username}>"