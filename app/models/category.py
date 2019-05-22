from sqlalchemy import Column, String
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship
from .base import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = 'categories'

    name = Column(String(40), unique=True)
    description = Column(String(200))

    items = relationship('ItemModel')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_based_on_offset_and_limit(cls, offset, limit):
        return cls.query.offset(offset).limit(limit).all()

    @classmethod
    def count_rows(cls):
        return cls.query.count()

