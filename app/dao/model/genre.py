from sqlalchemy import Column, String

from app.dao.model.base import BaseModel


class Genre(BaseModel):
    __tablename__ = 'genres'

    name = Column(String(255), unique=True, nullable=False)
