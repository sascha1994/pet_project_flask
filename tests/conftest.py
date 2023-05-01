import pytest

from app.config import Config
from app.server import create_app


@pytest.fixture(scope='module')
def app():
    app = create_app(Config)
    with app.app_context():
        yield app
