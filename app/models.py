from app import db
from flask.ext.mongoengine.wtf import model_form

class User(db.Document):
    name = db.StringField(required=True)
    username = db.StringField(max_length=50)
    email = db.StringField(max_length=50)
    password = db.StringField(max_length=50)
    
class KeysTable(db.Document):
    name = db.StringField(required=True)
    username = db.StringField(max_length=50)
    email = db.StringField(max_length=50)
    password = db.StringField(max_length=50)
    key = db.StringField(max_length=25)
    
    #def __repr__(self):
    #    return '<User %r>' % (self.username)