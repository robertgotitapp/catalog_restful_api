from sqlalchemy import Column, String
from .base import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = 'categories'

    name = Column(String(40), unique=True)
    description = Column(String(200))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()



