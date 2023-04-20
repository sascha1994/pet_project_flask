from marshmallow import fields

from app.dao.serialization.base import BaseSchema


class MovieSchema(BaseSchema):
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
