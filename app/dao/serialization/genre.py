from marshmallow import fields

from app.dao.serialization.base import BaseSchema


class GenreSchema(BaseSchema):
    name = fields.Str()
