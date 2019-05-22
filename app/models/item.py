from .base import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db import db_session


class ItemModel(BaseModel):
    __tablename__ = 'items'

    name = Column(String(40))
    description = Column(String(200))
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    category = relationship('CategoryModel')
    user = relationship('UserModel')

    def __init__(self, name, description, price, category_id, user_id):
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.user_id = user_id

    def delete_from_db(self):
        db_session.delete(self)
        db_session.commit()

    @classmethod
    def get_items_by_category(cls, category_id):
        ItemModel.query.filter(category_id=category_id).all()

    @classmethod
    def find_based_on_offset_and_limit(cls, offset, limit, category_id):
        return cls.query.filter_by(category_id=category_id).offset(offset).limit(limit).all()

    @classmethod
    def find_by_name(cls, category_id, _name):
        return cls.query.filter_by(category_id=category_id).filter_by(name=_name).all()

    @classmethod
    def find_by_id_with_filter_by_category(cls, category_id, _id):
        return cls.query.filter_by(category_id=category_id).filter_by(id=_id).one_or_none()

    @classmethod
    def count_rows(cls):
        return cls.query.count()