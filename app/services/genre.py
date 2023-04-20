from app.dao.model.genre import GenreModel
from app.services.base import BaseService


class GenreService(BaseService[GenreModel]):
    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, genre_id: int):
        return self.dao.get_by_id(genre_id)
