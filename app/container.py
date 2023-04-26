from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.database import db
from app.services.director import DirectorService
from app.services.genre import GenreService
from app.services.movie import MovieService

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(dao=genre_dao)

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(dao=director_dao)

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(dao=movie_dao)
