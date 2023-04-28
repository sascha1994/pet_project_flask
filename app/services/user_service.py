import base64
import hashlib
import hmac

import jwt
from flask import abort, current_app

from app.dao.user_dao import UserDAO
from app.services.excepetions import ItemNotFound, WrongPasswords


class UsersService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    @staticmethod
    def token_decode(data):
        token = data.split("Bearer ")[-1]
        try:
            token = jwt.decode(token, key=current_app.config['JWT_SECRET'],
                               algorithms=current_app.config['JWT_ALGORITHM'])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return token

    def get_item(self, pk: int):
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    def partial_update(self, uid: int, data):
        user = self.get_item(uid)

        if data.get('name'):
            user.name = data.get('name')
        if data.get('surname'):
            user.surname = data.get('surname')
        if data.get('favourite_genre'):
            user.favourite_genre = data.get('favourite_genre')

        self.dao.update(user)

    @staticmethod
    def get_hash(password: str) -> str:
        hash_digest = hashlib.pbkdf2_hmac(
            hash_name=current_app.config['HASH_NAME'],
            salt=current_app.config['HASH_SALT'].encode('utf-8'),
            iterations=current_app.config['HASH_ITERATIONS'],
            password=password.encode('utf-8'),
        )

        return base64.b64encode(hash_digest).decode('utf-8')

    def update(self, uid, data):
        user = self.get_item(uid)

        new_password = data.get('new_password')
        old_password = data.get('old_password')

        new_password_hash = self.get_hash(password=new_password)
        print(f"новый сгенерированный хеш {new_password_hash}")
        print(f"cтарый хеш лежащий у пользователя {user.password_hash}")
        print(f"старый пароль который будет генерироваться в хеш и сравниватся с хешем юсера {old_password}")

        if not self.__compare_passwords(user.password_hash, old_password):
            raise WrongPasswords

        user.password_hash = new_password_hash

        self.dao.update(user)

    @staticmethod
    def __compare_passwords(password_hash: str, old_password: str) -> bool:
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            hash_name=current_app.config['HASH_NAME'],
            salt=current_app.config['HASH_SALT'].encode('utf-8'),
            iterations=current_app.config['HASH_ITERATIONS'],
            password=old_password.encode('utf-8'),
        )

        return hmac.compare_digest(decoded_digest, hash_digest)
