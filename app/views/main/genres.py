from flask_restx import Resource, Namespace

# from decorators import auth_required
from app.container import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    # @auth_required
    def get(self):
        genres = genre_service.get_all()
        return genres, 200


@genres_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    # @auth_required
    def get(self, genre_id: int):
        genre = genre_service.get_item_by_id(genre_id)
        return genre, 200
