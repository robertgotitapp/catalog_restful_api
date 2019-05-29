from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import BaseModel


class CategoryModel(BaseModel):
    """
    Category model
    """
    __tablename__ = 'categories'

    name = Column(String(40), unique=True)
    description = Column(String(200))

    items = relationship('ItemModel')

    def __init__(self, name, description):
        """
        Constructor
        :param name: category name
        :param description: category description
        """
        self.name = name
        self.description = description

    @classmethod
    def find_by_name(cls, name):
        """
        Return the category with the provided name
        :param _id: the name of the category to be searched for
        :return: the category with the provided name, if the category could not be found, return none
        """
        return cls.query.filter_by(name=name).one_or_none()

    @classmethod
    def find_based_on_offset_and_limit(cls, offset, limit):
        """
        Return up to 'limit' number of rows of categories starting from 'offset' row
        :param offset: the number of starting row to be returned
        :param limit: the number of rows to be returned
        :return: the list of categories with the provided offset, limit number
        """
        return cls.query.offset(offset).limit(limit).all()

    @classmethod
    def count_rows(cls):
        """
        Return number of total categories in the database
        :return: number of total categories
        """
        return cls.query.count()
