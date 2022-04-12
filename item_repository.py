import sqlite3


class ItemRepository:
    TABLE_NAME = 'items'

    def find_by_name(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    def find_all(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.close()

        if row:
            return items

    def insert(self, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO {table} VALUES(?, ?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    def update(self, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE {table} SET price=? WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (item['price'], item['name']))
        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
