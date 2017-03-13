from . import db
import time

class UserProfile(db.Model):
    userid = db.Column(db.String(13), primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(6))
    biography = db.Column(db.String(127))
    created_on = db.Column(db.Date)

    def __init__(self, userid, firstname, lastname, username, age, gender, biography, created_on):
        self.userid = userid
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.age = age
        self.gender = gender
        self.biography = biography
        self.created_on = created_on

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
