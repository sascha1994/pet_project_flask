from marshmallow import Schema, fields

from app.dao.serialization.director import DirectorSchema
from app.dao.serialization.genre import GenreSchema


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)
