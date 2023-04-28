from flask import request
from flask_restx import Resource, Namespace, abort

# from decorators import auth_required
from app.container import movie_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        data = {
            'status': request.args.get('status'),
            'page': request.args.get("page")
        }
        movies = movie_service.get_all(data)

        return movies, 200


@movies_ns.route('/<int:mid>/')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_by_id(mid)

        if not movie:
            abort(404, message='Movie not found')

        return movie, 200
