from app.dao.model.director import DirectorModel
from app.dao.model.genre import GenreModel
from app.database import db
from app.dao.model.base import BaseModel


class MovieModel(BaseModel):
    __tablename__ = 'movies'
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey(GenreModel.id))
    director_id = db.Column(db.Integer, db.ForeignKey(DirectorModel.id))
