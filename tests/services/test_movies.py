from unittest.mock import patch

import pytest

from app.dao.model.movie import Movie
from app.services.movie_service import MovieService


@pytest.fixture()
@patch('app.dao.MovieDAO')
def movie_dao_mock(dao_mock):
    dao = dao_mock()
    dao.get_by_id.return_value = Movie(
        id=1,
        title='test_title',
        description='test_description',
        trailer='test_trailer',
        year=2020,
        rating=7.1,
        genre_id=1,
        director_id=1
    )
    dao.get_all.return_value = [
        Movie(
            id=1,
            title='test_title_1',
            description='test_description_1',
            trailer='test_trailer_1',
            year=2021,
            rating=7.2,
            genre_id=2,
            director_id=2
        ),
        Movie(
            id=2,
            title='test_title_2',
            description='test_description_2',
            trailer='test_trailer_2',
            year=2022,
            rating=7.3,
            genre_id=3,
            director_id=3
        ),
    ]
    return dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_mock):
        self.movie_service = MovieService(dao=movie_dao_mock)

    def test_get_all(self):
        movie = self.movie_service.get_all()

        assert len(movie) == 2

    def test_get_item_by_id(self):
        movie = self.movie_service.get_by_id(movie_id=1)

        assert movie is not None
        assert movie['id'] == 1
