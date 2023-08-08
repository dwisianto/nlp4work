#
#
#
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app.extensions import db
from app.extensions import login

from datetime import datetime


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    #posts = db.relationship('Post', backref='author', lazy='dynamic')
    tales = db.relationship('Tale', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
        }


#
#
#
#class Post(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    body = db.Column(db.String(140))
#    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#    def __repr__(self):
#        return '<Post {}>'.format(self.body)
#
#    def to_dict(self):
#        return {
#            'post_id': self.id,
#            'user_id': self.user_id,
#            'body': self.body,
#            'post_timestamp': self.timestamp,
#        }


#
# Tale, Narration, Narrative
class Tale(db.Model):
    tale_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #tale_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    tale_narrative = db.Column(db.String(260))
    tale_narrative_id = db.Column(db.Integer)
    tale_narrative_submission_date = db.Column(db.DateTime)
    tale_narrative_correctness = db.Column(db.String(10))

    def __repr__(self):
        return '<Tale id:{}>'.format(self.tale_id)

    def to_dict(self):
        #            'tale_timestamp': self.tale_timestamp,
        return {
            'tale_id': self.tale_id,
            'user_id': self.user_id,
            'tale_narrative': self.tale_narrative,
            'tale_narrative_id': self.tale_narrative_id,
            'tale_narrative_submission_date': self.tale_narrative_submission_date,
            'tale_narrative_correctness': self.tale_narrative_correctness,
        }
