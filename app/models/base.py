import datetime
from sqlalchemy import Column, Integer, DateTime
from app.db import Base, db_session


class BaseModel(Base):
    """
    Base class that provides the basic interface for every class to inherits from
    """
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime,
                     default=datetime.datetime.utcnow,
                     onupdate=datetime.datetime.utcnow)

    @classmethod
    def find_by_id(cls, _id):
        """
        Return the item with the provided id
        :param _id: the id of the item to be searched for
        :return: the item with the provided id, if the item could not be found, return none
        """
        return cls.query.filter_by(id=_id).one_or_none()

    def save_to_db(self):
        """
        Save the change to the database
        """
        db_session.add(self)
        db_session.commit()
