from unittest.mock import patch

import pytest

from app.dao.model.user import User
from app.services.auth_service import AuthService


@pytest.fixture()
@patch('app.dao.AuthDAO')
def auth_dao_mock(dao_mock):
    dao = dao_mock()
    dao.create.return_value = User(
        id=1,
        email='email',
        password='oQ5/DDziBrr0IXIwhoXFJfR/6fA7nqVzWTLDKUyYcJk='
    )
    dao.get_by_email.return_value = User(
        id=1,
        email='email',
        password='oQ5/DDziBrr0IXIwhoXFJfR/6fA7nqVzWTLDKUyYcJk=',
        name='test_name',
        surname='test_surname',
        favourite_genre=1
    )
    return dao


class TestAuthService:
    @pytest.fixture(autouse=True)
    def auth_service(self, auth_dao_mock):
        self.auth_service = AuthService(dao=auth_dao_mock)

    def test_register(self, app):
        email = 'email'
        password = 'password'
        new_user = self.auth_service.register(email=email, password=password)

        assert new_user is not None

    def test_login(self, app):
        email = 'email'
        password = 'password'
        tokens = self.auth_service.login(email=email, password=password)

        assert tokens is not None
