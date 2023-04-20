from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.serialization.movie import MovieSchema

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class GenreView(Resource):
    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200


@movies_ns.route('/<int:movie_id>')
class GenreView(Resource):
    def get(self, movie_id: int):
        movie = movie_service.get_by_id(movie_id)
        return movie_schema.dump(movie), 200
