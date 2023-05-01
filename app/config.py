class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRE_MINUTES = 30
    TOKEN_EXPIRE_DAYS = 130

    JWT_SECRET = 'random_secret'
    JWT_ALGORITHM = 'HS256'
    HASH_NAME = 'sha256'
    HASH_SALT = 'secret here'
    HASH_ITERATIONS = 100_000

    ITEMS_PER_PAGE = 12
   