from app.dao.movie import MovieDAO
from app.dao.serialization.movie import MovieSchema


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_by_id(self, movie_id: int):
        movie = self.dao.get_by_id(movie_id)

        return MovieSchema().dump(movie)

    def get_all(self, data):
        movies = self.dao.get_all()

        status = data.get('status')
        page = data.get('page')

        # if status and status == 'new':
        #     movies_query = self.dao.get_new(movies_query)
        #
        # if page:
        #     limit = current_app.config['ITEMS_PER_PAGE']
        #     offset = (page - 1) * limit
        #     movies_query = self.dao.get_pages(movies_query, limit, offset)
        #
        # movies = self.dao.get_all(movies_query)
        return MovieSchema(many=True).dump(movies)
