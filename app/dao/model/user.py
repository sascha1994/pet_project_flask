from sqlalchemy import Column, Integer, String, ForeignKey

from app.dao.model.base import BaseModel
from app.dao.model.genre import Genre


class User(BaseModel):
    __tablename__ = 'user'

    email = Column(String, unique=True, nullable=False)
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    favourite_genre = Column(Integer, ForeignKey(Genre.id))
