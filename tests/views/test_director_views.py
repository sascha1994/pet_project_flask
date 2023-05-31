import json

from unittest.mock import patch

import pytest

from app.dao.model.director import Director


@pytest.fixture()
@patch('app.dao.DirectorDAO')
def director_dao_mock(dao_mock):
    dao = dao_mock()
    dao.get_by_id.return_value = Director(id=1, name='test_director_1')
    dao.get_all.return_value = [
        Director(id=1, name='test_director_1'),
        Director(id=2, name='test_director_2'),
    ]
    return dao


def test_director_view_get_all(client):
    response = client.get('/directors/')
    assert response.status_code == 200
    assert len(json.loads(response.data)) != 0


def test_director_view_get_one(client):
    response = client.get('/directors/1/')
    assert response.status_code == 200
    assert json.loads(response.data) == {"id": 1, "name": "s Шеридан"}
