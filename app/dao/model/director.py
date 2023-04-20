from app.database import db
from app.dao.model.base import BaseModel


class DirectorModel(BaseModel):
    __tablename__ = 'directors'
    name = db.Column(db.String(255), unique=True, nullable=False)
