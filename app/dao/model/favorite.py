from app.dao.model.base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.dao.model.movie import Movie
from app.dao.model.user import User
from app.database import db


class Favorite(db.Model):
    __tablename__ = 'favorites'

    user_id = Column(Integer, ForeignKey(User.id, ondelete='CASCADE'), primary_key=True)
    user = relationship(User)
    movie_id = Column(Integer, ForeignKey(Movie.id, ondelete='CASCADE'), primary_key=True)
    movie = relationship(Movie)
