__all__ = [
    'GenreDAO',
    'DirectorDAO',
    'MovieDAO',
    'UserDAO',
    'AuthDAO',
    'FavoritesDAO'
]

from app.dao.auth_dao import AuthDAO
from app.dao.director_dao import DirectorDAO
from app.dao.favorite_dao import FavoritesDAO
from app.dao.genre_dao import GenreDAO
from app.dao.movie_dao import MovieDAO
from app.dao.user_dao import UserDAO
