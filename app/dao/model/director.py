from sqlalchemy import Column, String

from app.dao.model.base import BaseModel


class Director(BaseModel):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)
