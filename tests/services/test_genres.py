from unittest.mock import patch

import pytest

from app.dao.model.genre import Genre
from app.services.genre_service import GenreService


@pytest.fixture()
@patch('app.dao.GenreDAO')
def genre_dao_mock(dao_mock):
    dao = dao_mock()
    dao.get_by_id.return_value = Genre(id=1, name='test_genre')
    dao.get_all.return_value = [
        Genre(id=1, name='test_genre_1'),
        Genre(id=2, name='test_genre_2'),
    ]
    return dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao_mock):
        self.genre_service = GenreService(dao=genre_dao_mock)

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) == 2

    def test_get_item_by_id(self):
        genre = self.genre_service.get_item_by_id(genre_id=1)

        assert genre is not None
        assert genre['id'] == 1
