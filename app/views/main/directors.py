from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.serialization.director import DirectorSchema

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class GenreView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@directors_ns.route('/<int:director_id>')
class GenreView(Resource):
    def get(self, director_id: int):
        director = director_service.get_by_id(director_id)
        return director_schema.dump(director), 200
