from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price
