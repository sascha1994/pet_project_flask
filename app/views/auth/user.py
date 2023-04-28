from flask import request
from flask_restx import Namespace, Resource

from app.container import user_service
from app.helpers.decorators import auth_required
from app.setup.api.models import user

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    # @auth_required
    @user_ns.response(404, 'Not Found')
    @user_ns.marshal_with(user, code=200, description='OK')
    def get(self):
        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        return user_service.get_item(uid)

    @user_ns.response(404, 'Not Found')
    @user_ns.marshal_with(user, code=206, description='OK')
    def patch(self):
        data_update = request.json
        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        user_service.partial_update(uid, data_update)

        return ''


@user_ns.route('/password/')
class UserView(Resource):
    @user_ns.response(404, 'Not Found')
    @user_ns.marshal_with(user, code=204, description='OK')
    def put(self):
        data_update = request.json
        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        user_service.update(uid, data_update)

        return ''
