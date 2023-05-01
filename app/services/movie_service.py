from app.dao.movie_dao import MovieDAO
from app.dao.serialization.movie import MovieSchema


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_by_id(self, movie_id: int):
        movie = self.dao.get_by_id(movie_id)

        return MovieSchema().dump(movie)

    def get_all(self):
        movies = self.dao.get_all()
        return MovieSchema(many=True).dump(movies)
