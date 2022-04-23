from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))
    image = db.Column(db.String())

    def __init__(self, name, price, image=None):
        self.name = name
        self.price = price
        self.image = image
