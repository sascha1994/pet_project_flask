from app.dao.model.genre import GenreModel
from app.database import db
from app.dao.model.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users '
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favorite_genre = db.Column(db.db.ForeignKey(GenreModel.id))
