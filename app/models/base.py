import datetime
from sqlalchemy import Column, Integer, DateTime
from app.db import Base, db_session


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.now().isoformat())
    updated = Column(DateTime,
                     default=datetime.datetime.now().isoformat(),
                     onupdate=datetime.datetime.now().isoformat())

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db_session.add(self)
        db_session.commit()
