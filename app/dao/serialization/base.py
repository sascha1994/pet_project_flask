from marshmallow import Schema, fields


class BaseSchema(Schema):
    id = fields.Int(dump_only=True)
