from marshmallow import fields

from app.dao.serialization.base import BaseSchema


class DirectorSchema(BaseSchema):
    name = fields.Str()
