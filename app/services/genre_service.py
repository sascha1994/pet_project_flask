from app.dao.genre_dao import GenreDAO
from app.dao.serialization.genre import GenreSchema


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_item_by_id(self, genre_id: int):
        genre = self.dao.get_by_id(genre_id)

        return GenreSchema().dump(genre)

    def get_all(self):
        genres = self.dao.get_all()

        return GenreSchema(many=True).dump(genres)
