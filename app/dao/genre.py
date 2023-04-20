from app.dao.base import BaseDAO
from app.dao.model.genre import GenreModel


class GenreDao(BaseDAO):

    def get_by_id(self, genre_id: int):
        return self.session.query(GenreModel).get(genre_id)

    def get_all(self):
        return self.session.query(GenreModel).all()
