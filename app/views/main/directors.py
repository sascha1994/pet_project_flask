from flask_restx import Resource, Namespace

# from decorators import auth_required
from app.container import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorView(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors, 200


@directors_ns.route('/<int:director_id>/')
class DirectorView(Resource):
    def get(self, director_id: int):
        director = director_service.get_item_by_id(director_id)
        return director, 200
