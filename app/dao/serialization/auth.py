from marshmallow import Schema, fields


class AuthUserSchema(Schema):
    id = fields.Int()
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class AuthRegisterRequest(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class UserSchema(Schema):
    email = fields.Str(required=True)
    name = fields.Str(required=True)
    surname = fields.Str()
    # favourite_genre = fields.Nested(GenreSchema, only=['name'])
