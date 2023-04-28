from app.config import Config
from app.helpers.create_data import create_data
from app.server import create_app

app = create_app(Config())

if __name__ == '__main__':
    create_data()
    app.run()
