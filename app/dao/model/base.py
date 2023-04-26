from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String

from app.database import db


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
