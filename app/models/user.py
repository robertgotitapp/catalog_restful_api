from db import db
from .base import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'

    username = db.Column(db.String(30))
    password = db.Column(db.String(256))
    name = db.Column(db.String(40))
    email = db.Column(db.String(40))

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
