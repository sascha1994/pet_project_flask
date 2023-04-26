from app.dao.director import DirectorDAO
from app.dao.serialization.director import DirectorSchema


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_item_by_id(self, movie_id: int):
        director = self.dao.get_by_id(movie_id)

        return DirectorSchema().dump(director)

    def get_all(self):
        directors = self.dao.get_all()

        return DirectorSchema(many=True).dump(directors)
