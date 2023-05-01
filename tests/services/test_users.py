from unittest.mock import patch

import pytest

from app.dao.model.user import User
from app.services.user_service import UsersService


@pytest.fixture()
@patch('app.dao.UserDAO')
def users_dao_mock(dao_mock):
    dao = dao_mock()
    dao.get_by_id.return_value = User(
        id=1,
        email='email',
        password='oQ5/DDziBrr0IXIwhoXFJfR/6fA7nqVzWTLDKUyYcJk=',
        name='test_name',
        surname='test_surname',
        favourite_genre=1
    )
    dao.update.return_value = User(
        id=1,
        email='email',
        password='oQ5/DDziBrr0IXIwhoXFJfR/6fA7nqVzWTLDKUyYcJk=',
        name='user_name',
        surname='user_surname',
        favourite_genre=1

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


class TestUsersService:
    @pytest.fixture(autouse=True)
    def users_service(self, users_dao_mock):
        self.users_service = UsersService(dao=users_dao_mock)

    def test_get_item(self):
        new_user = self.users_service.get_item(pk=1)

        assert new_user is not None

    def test_partial_update(self):
        data = {
            'name': 'user_name',
            'surname': 'user_surname',
            'favourite_genre': 1,
        }
        self.users_service.partial_update(uid=1, data=data)

    def test_update(self):
        data = {
            'new_password': 'new_password',
            'old_password': 'password',
        }
        self.users_service.update(uid=1, data=data)

