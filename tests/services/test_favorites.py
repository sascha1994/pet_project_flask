from unittest.mock import patch

import pytest

from app.dao.model.favorite import Favorite
from app.services.favorite_service import FavoritesService


@pytest.fixture()
@patch('app.dao.FavoritesDAO')
def favorites_dao_mock(dao_mock):
    dao = dao_mock()
    dao.get_all_favorites.return_value = [
        Favorite(user_id=1, movie_id=1),
        Favorite(user_id=1, movie_id=2),
    ]
    dao.create.return_value = Favorite(user_id=1, movie_id=1)
    dao.delete_favorites.return_value = None
    return dao


class TestFavoritesService:
    @pytest.fixture(autouse=True)
    def genre_service(self, favorites_dao_mock):
        self.favorites_service = FavoritesService(dao=favorites_dao_mock)

    def test_get_all_favorites(self):
        favorites = self.favorites_service.get_all_favorites(uid=1)

        assert len(favorites) == 2

    def test_add_favorite(self):
        favorite = self.favorites_service.add_favorite(user_id=1, movie_id=1)

        assert favorite is not None

    def test_delete_favorites(self):
        favorite = self.favorites_service.delete_favorites(uid=1, movie_id=1)

        assert favorite is None
