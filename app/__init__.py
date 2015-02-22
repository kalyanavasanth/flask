#!usr/bin/python3
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.mail import Mail

app = Flask(__name__)

app.config.from_object('config')

app.config.update( DEBUG=True,
MAIL_SERVER='smtp.gmail.com', MAIL_PORT=587, 
MAIL_USE_SSL=False, MAIL_USE_TLS=True, 
MAIL_USERNAME = 'whirlhammer@gmail.com', MAIL_PASSWORD = '@ustrali@' )

db = MongoEngine(app)
mail = Mail(app)

from app import views, models