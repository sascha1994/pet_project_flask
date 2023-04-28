from flask_restx import Namespace, Resource
from flask import request

from app.container import user_service, favorite_service
from app.helpers.decorators import auth_required
from app.setup.api.models import movie

favorite_ns = Namespace('favorites')


@favorite_ns.route('/movies/')
class FavoritesView(Resource):
    @auth_required
    @favorite_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        return favorite_service.get_all_favorites(uid)


@favorite_ns.route("/movies/<int:movie_id>/")
class FavoriteView(Resource):
    @auth_required
    @favorite_ns.response(404, 'Not Found')
    @favorite_ns.marshal_with(movie, code=200, description='OK')
    def post(self, movie_id: int):
        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        favorite_service.add_favorite(uid, movie_id)

        return '', 200

    @favorite_ns.response(404, 'Not Found')
    @favorite_ns.marshal_with(movie, code=200, description='OK')
    def delete(self, movie_id: int):
        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        return favorite_service.delete_favorites(uid=uid, movie_id=movie_id)
