import os
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
MONGODB_SETTINGS = {
    'db': 'exception_logger',
    'host': '127.0.0.1',
    'port': 27017
}

basedir = os.path.abspath(os.path.dirname(__file__))