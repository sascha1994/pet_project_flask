from unittest.mock import patch

import pytest

from app.dao.model.director import Director
from app.services.director_service import DirectorService


@pytest.fixture()
@patch('app.dao.DirectorDAO')
def director_dao_mock(dao_mock):
    dao = dao_mock()
    dao.get_by_id.return_value = Director(id=1, name='test_director_1')
    dao.get_all.return_value = [
        Director(id=1, name='test_director_1'),
        Director(id=2, name='test_director_2'),
    ]
    return dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao_mock):
        self.director_service = DirectorService(dao=director_dao_mock)

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) == 2

    def test_get_item_by_id(self):
        director = self.director_service.get_item_by_id(movie_id=1)

        assert director is not None
        assert director['id'] == 1
