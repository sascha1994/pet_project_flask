from app.dao.model.movie import MovieModel
from app.services.base import BaseService


class MovieService(BaseService[MovieModel]):
    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, movie_id: int):
        return self.dao.get_by_id(movie_id)
