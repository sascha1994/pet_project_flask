from app.dao.model.favorite import Favorite
from app.dao.model.movie import Movie


class FavoritesDAO:

    def __init__(self, session):
        self.session = session

    def create(self, user_id: int, movie_id: int):
        new_favorite = Favorite(
            user_id=user_id,
            movie_id=movie_id,
        )

        self.session.add(new_favorite)
        self.session.commit()

        return new_favorite

    def get_all_favorites(self, uid: int):
        query = self.session.query(Movie).join(Favorite).filter(Favorite.user_id == uid).all()
        return query

    def get_one_favorite(self, user_id: int, movie_id: int):
        favorite = self.session.query(
            Favorite
        ).filter(
            Favorite.user_id == user_id,
            Favorite.movie_id == movie_id
        ).one()
        return favorite

    def delete_favorites(self, uid: int, movie_id: int):
        favorite = self.get_one_favorite(uid, movie_id)

        self.session.delete(favorite)
        self.session.commit()
