from app.dao.base import BaseDAO
from app.dao.model.movie import MovieModel


class MovieDao(BaseDAO):

    def get_by_id(self, movie_id: int):
        return self.session.query(MovieModel).get(movie_id)

    def get_all(self):
        return self.session.query(MovieModel).all()
