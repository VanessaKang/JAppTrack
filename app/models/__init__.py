from app import db


class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        
    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class ModelValidationException(Exception):
    def json(self):
        return {
            "error": self.args[0]
        }