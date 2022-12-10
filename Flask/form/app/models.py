from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login

from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Integer, default=lambda: 0)
    awnsers = db.relationship('Awnser', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.admin == 1

    def __repr__(self):
        return f'<User {self.email}>'


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    type = db.Column(db.String(50))
    awnsers = db.relationship('Awnser', backref='question', lazy='dynamic')
    choices = db.relationship('Choice', backref='question', lazy='dynamic')

    def __repr__(self):
        return f'<Question {self.body}>'

    @staticmethod
    def count_awnsers():
        questions = {}
        for q in Question.query.all():
            awnsers = {}
            for c in q.choices.all():
                awnsers[c.body] = 0
            for a in q.awnsers.all():
                if a.body not in awnsers:
                    awnsers[a.body] = 0
                awnsers[a.body] += 1

            for k, v in awnsers.items():
                if (count := q.awnsers.count()) != 0:
                    awnsers[k] = round(v/count, 2)
                else:
                    awnsers[k] = 0

            questions[q] = awnsers

        return questions


class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    body = db.Column(db.String(256))

    def __repr__(self):
        return f'<Choice {self.body}>'


class Awnser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        q = Question.query.filter_by(id=self.question_id).first().body
        a = self.body 
        return f'<Awnser {a}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
