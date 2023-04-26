from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, genre_id: int):
        return self.session.query(Genre).filter(Genre.id == genre_id).one_or_none()

    def get_all(self):
        return self.session.query(Genre).all()
