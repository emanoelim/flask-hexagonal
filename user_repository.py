import sqlite3


class User():
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


class UserRepository:
    TABLE_NAME = 'users'

    def find_by_username(self, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE username=?".format(table=self.TABLE_NAME)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = User(*row)
        else:
            user = None
        connection.close()
        return user

    def find_by_id(self, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE id=?".format(table=self.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = User(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def insert(cls, username, password):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (username, password))
        connection.commit()
        connection.close()
