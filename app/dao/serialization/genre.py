from marshmallow import Schema, fields


class GenreSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
