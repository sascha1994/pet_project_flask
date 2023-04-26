from app.dao.auth import AuthDAO
from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.database import db
from app.services.auth import AuthService
from app.services.director import DirectorService
from app.services.genre import GenreService
from app.services.movie import MovieService

# DAO

genre_dao = GenreDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
auth_dao = AuthDAO(session=db.session)

# SERVICES

genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
auth_service = AuthService(dao=auth_dao)
