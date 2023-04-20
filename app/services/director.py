from app.dao.model.director import DirectorModel
from app.services.base import BaseService


class DirectorService(BaseService[DirectorModel]):
    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, director_id: int):
        return self.dao.get_by_id(director_id)
