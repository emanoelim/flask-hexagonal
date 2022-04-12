import sqlite3


class ItemModel:
    TABLE_NAME = 'items'

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return ItemModel(*row)

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        connection.close()
        if row:
            return ItemModel(*row)

    @classmethod
    def find_all(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table}".format(table=cls.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append(ItemModel(*row))
        connection.close()
        if row:
            return items

    @classmethod
    def insert(cls, name, price):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (name, price))
        connection.commit()
        connection.close()
        return ItemModel.find_by_name(name)

    def update(self, name, price):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE {table} SET price=? WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (price, self.name))
        connection.commit()
        connection.close()
        return ItemModel.find_by_name(name)

    def delete(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (self.name,))
        connection.commit()
        connection.close()
