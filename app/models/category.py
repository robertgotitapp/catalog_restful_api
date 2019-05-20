from app.db import db
from .base import BaseModel


class CategoryModel(BaseModel):
    __tablename = 'categories'

    name = db.Column(db.String(40), unique=True)
    description = db.Column(db.String(200))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()



