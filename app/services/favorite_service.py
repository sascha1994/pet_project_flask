from app.dao.favorite_dao import FavoritesDAO


class FavoritesService:
    def __init__(self, dao: FavoritesDAO):
        self.dao = dao

    def add_favorite(self, user_id: int, movie_id: int):
        return self.dao.create(user_id, movie_id)

    def get_all_favorites(self, uid: int):
        return self.dao.get_all_favorites(uid=uid)

    def delete_favorites(self, uid: int, movie_id: int):
        self.dao.delete_favorites(uid, movie_id)
