from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login

from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Integer, default=lambda: 0)
    cart = db.relationship('CartItem', backref='user', lazy='dynamic')
    cupons = db.relationship('UserCupon', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.admin == 1

    def __repr__(self):
        return f'<User {self.email}>'


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    body = db.Column(db.String(500))
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"<Item {self.body}>"


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    amount = db.Column(db.Integer)

    def get_item(self):
        return Item.query.filter_by(id=self.item_id).first()

    def __repr__(self):
        return f"<CartItem {self.id}>"

class Cupon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    procent = db.Column(db.Integer)
    name = db.Column(db.String(100))
    max_uses = db.Column(db.Integer)
    cupons = db.relationship('UserCupon', backref='cupon', lazy='dynamic')

    def __repr__(self):
        return f"<Cupon {self.name}>"

class UserCupon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cupon_id = db.Column(db.Integer, db.ForeignKey('cupon.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer)

    def __repr__(self):
        return f"<UserCupon {self.cupon_id}.{self.status}>"



@login.user_loader
def load_user(id):
    return User.query.get(int(id))
