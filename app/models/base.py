import datetime
from app.db import db


class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.now().isoformat())
    updated = db.Column(db.DateTime,
                        onupdate=datetime.datetime.now().isoformat(),
                        default=datetime.datetime.now().isoformat())

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()