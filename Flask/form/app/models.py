from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login

from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # awnsers = db.relationship('Awnser', backref='authored', lazy='dynamic')
    posts = db.relationship('Awnser', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    type = db.Column(db.String(50))

    def __repr__(self):
        return f'<Question {self.body}>'


class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer)
    body = db.Column(db.String(140))

    def __repr__(self):
        return f'<Choices {self.body}>'


class Awnser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # choice_id = db.Column(db.Integer, db.ForeignKey('Choice.id'))

    def __repr__(self):
        return f'<Awnser {self.body}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
