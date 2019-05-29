from .base import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db import db_session


class ItemModel(BaseModel):
    """
    Item model
    """
    __tablename__ = 'items'

    name = Column(String(40))
    description = Column(String(200))
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    category = relationship('CategoryModel')
    user = relationship('UserModel')

    def __init__(self, name, description, price, category_id, user_id):
        """
        Item constructor
        :param name: item name
        :param description: item description
        :param price: item price
        :param category_id: item category id
        :param user_id: item user id
        """
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.user_id = user_id

    def delete_from_db(self):
        """
        Delete the selected data from database
        """
        db_session.delete(self)
        db_session.commit()

    @classmethod
    def get_items_by_category(cls, category_id):
        """
        Return the number of items from the provided category_id
        :param category_id: the category_id of the category items to be returned
        :return: all items that belongs to category being provided
        """
        ItemModel.query.filter(category_id=category_id).all()

    @classmethod
    def find_based_on_offset_and_limit(cls, offset, limit, category_id):
        """
        Return up to 'limit' number of rows of items belongs to the category being provided starting from 'offset' row
        :param offset: the number of starting row to be returned
        :param limit: the number of rows to be returned
        :param category_id: the category_id of the category items to be returned
        :return: the list of items belong to the provided category with the provided offset, limit number
        """
        return cls.query.filter_by(category_id=category_id).offset(offset).limit(limit).all()

    @classmethod
    def find_by_id_and_category(cls, category_id, _id):
        """
        Return the item with the provided id that also belongs to the selected category
        :param category_id: the category_id of the item to be returned
        :param _id: the id of the item to be returned
        :return: the item with the provided category_id and id, return None if of record matches the search
        """
        return cls.query.filter_by(category_id=category_id).filter_by(id=_id).one_or_none()

    @classmethod
    def count_rows(cls, category_id):
        """
        Return number of total items belongs to the selected category in the database
        :param category_id: the category_id of category items being count
        :return: number of total items of the selected category
        """
        return cls.query.filter_by(category_id=category_id).count()
