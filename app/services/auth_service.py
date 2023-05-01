import base64
import hashlib

import hmac
from datetime import datetime, timedelta

from flask import current_app
import jwt

from app.dao.auth_dao import AuthDAO
from app.dao.serialization.auth import AuthUserSchema
from app.services.excepetions import UserNotFound, WrongPassword


class AuthService:

    def __init__(self, dao: AuthDAO):
        self.dao = dao

    @staticmethod
    def get_hash(password: str) -> str:
        hash_digest = hashlib.pbkdf2_hmac(
            hash_name=current_app.config['HASH_NAME'],
            salt=current_app.config['HASH_SALT'].encode('utf-8'),
            iterations=current_app.config['HASH_ITERATIONS'],
            password=password.encode('utf-8'),
        )

        return base64.b64encode(hash_digest).decode('utf-8')

    @staticmethod
    def compare_password(password_1: str, password_2: str):
        return hmac.compare_digest(password_1, password_2)

    @staticmethod
    def generate_tokens(user):
        payload = {
            'email': user['email'],
            'id': user['id'],
            'exp': datetime.utcnow() + timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
        }

        access_token = jwt.encode(
            payload=payload,
            key=current_app.config['JWT_SECRET'],
            algorithm=current_app.config['JWT_ALGORITHM'],
        )

        payload['exp'] = datetime.utcnow() + timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])

        refresh_token = jwt.encode(
            payload=payload,
            key=current_app.config['JWT_SECRET'],
            algorithm=current_app.config['JWT_ALGORITHM'],
        )

        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }

    def register(self, email: str, password: str):
        password_hash = self.get_hash(password=password)
        new_user = self.dao.create(email=email, password_hash=password_hash)
        return AuthUserSchema().dump(new_user)

    def login(self, email: str, password: str):
        lg = self.dao.get_by_email(email)
        user = AuthUserSchema().dump(lg)

        if user is None:
            raise UserNotFound

        password_hash = self.get_hash(password)

        if not self.compare_password(user['password'], password_hash):
            raise WrongPassword

        return self.generate_tokens(user)
