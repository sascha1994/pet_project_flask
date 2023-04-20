from app.database import db
from app.dao.model.base import BaseModel


class GenreModel(BaseModel):
    __tablename__ = 'genres'
    name = db.Column(db.String(255), unique=True, nullable=False)
