from sqlalchemy.orm import subqueryload

from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, movie_id: int):
        return self.session.query(Movie).filter(Movie.id == movie_id).one_or_none()

    def get_all(self):
        query = self.session.query(Movie).join(Movie.genre).join(Movie.director).all()
        return query

    def get_movies(self):
        return self.session.query(Movie)
