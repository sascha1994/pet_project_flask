from flask_restx import Namespace, Resource
from flask import request

from app.container import auth_service
from app.dao.serialization.auth import AuthRegisterRequest

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class RegisterView(Resource):
    @staticmethod
    def post():
        data = request.json
        validated_data = AuthRegisterRequest().load(data)
        auth_service.register(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return '', 200


@auth_ns.route('/login/')
class LoginView(Resource):
    @staticmethod
    def post():
        data = request.json
        validated_data = AuthRegisterRequest().load(data)

        tokens = auth_service.login(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return tokens, 200
