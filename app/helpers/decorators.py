import jwt
from flask import request, abort

from flask import current_app


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            data = jwt.decode(token, key=current_app.config['JWT_SECRET'],
                              algorithms=current_app.config['JWT_ALGORITHM'])
        except Exception as e:
            print("JWT Decode Exception here", e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper


# def auth_req(func):
#     def wrapper(*args, **kwargs):
#         if 'Authorization' not in request.headers:
#             abort(401)
#
#         data = request.headers['Authorization']
#         token = data.split("Bearer ")[-1]
#         try:
#             jwt.decode(token, key=current_app.config['JWT_SECRET'], algorithms=current_app.config['JWT_ALGORITHM'])
#         except Exception as e:
#             print("JWT Decode Exception", e)
#             abort(401)
#
#         return func(*args, **kwargs)
#
#     return wrapper
