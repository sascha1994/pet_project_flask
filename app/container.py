from app.dao.auth_dao import AuthDAO
from app.dao.director_dao import DirectorDAO
from app.dao.favorite_dao import FavoritesDAO
from app.dao.genre_dao import GenreDAO
from app.dao.movie_dao import MovieDAO
from app.dao.user_dao import UserDAO
from app.database import db
from app.services.auth_service import AuthService
from app.services.director_service import DirectorService
from app.services.favorite_service import FavoritesService
from app.services.genre_service import GenreService
from app.services.movie_service import MovieService
from app.services.user_service import UsersService

# DAO

genre_dao = GenreDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
auth_dao = AuthDAO(session=db.session)
favorite_dao = FavoritesDAO(session=db.session)
user_dao = UserDAO(session=db.session)

# SERVICES

genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
auth_service = AuthService(dao=auth_dao)
favorite_service = FavoritesService(dao=favorite_dao)
user_service = UsersService(dao=user_dao)
