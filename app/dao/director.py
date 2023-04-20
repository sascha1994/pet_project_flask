from app.dao.base import BaseDAO
from app.dao.model.director import DirectorModel


class DirectorDao(BaseDAO):

    def get_by_id(self, director_id: int):
        return self.session.query(DirectorModel).get(director_id)

    def get_all(self):
        return self.session.query(DirectorModel).all()
