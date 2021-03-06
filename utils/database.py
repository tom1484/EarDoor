import mysql.connector
from mysql.connector import Error
import json


class Database:

    def __init__(self, host, database, user, password, table):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.table = table

    def connect(self):
        while True:
            try:
                self.conn = mysql.connector.connect(host=self.host, database=self.database,
                                                    user=self.user, password=self.password)
                return
            except Error as e:
                print('Failed:', e)

    def select_records(self, name):
        sql = f'SELECT Records FROM {self.table} WHERE Name=\'{name}\';'
        # print(sql)

        try:
            if not hasattr(self, 'conn') or not self.conn.is_connected():
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(sql)
            raw = cursor.fetchone()[0]
            return json.loads(raw)

        except Error as e:
            print('Failed:', e)
            return -1

    def select_image(self, name):
        sql = f'SELECT Image FROM {self.table} WHERE Name=\'{name}\';'
        # print(sql)

        try:
            if not hasattr(self, 'conn') or not self.conn.is_connected():
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(sql)
            return cursor.fetchone()[0]

        except Error as e:
            print('Failed:', e)
            return -1

    def update_records(self, name, records):
        sql = f'UPDATE {self.table} SET Records=\'{records}\' WHERE Name=\'{name}\';'
        # print(sql)

        try:
            if not hasattr(self, 'conn') or not self.conn.is_connected():
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return 1

        except Error as e:
            print('Failed:', e)
            return -1

    def update_image(self, name, image):
        sql = f'UPDATE {self.table} SET Image=\'{image}\' WHERE Name=\'{name}\';'
        # print(sql)

        try:
            if not hasattr(self, 'conn') or not self.conn.is_connected():
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return 1

        except Error as e:
            print('Failed:', e)
            return -1

    def insert(self, name):
        sql = f'INSERT INTO {self.table} (Name, Records) VALUES (\'{name}\', \'[]\');'
        # print(sql)

        try:
            if not hasattr(self, 'conn') or not self.conn.is_connected():
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return 1

        except Error as e:
            print('Failed:', e)
            return -1

    def delete(self, name):
        sql = f'DELETE FROM {self.table} WHERE Name=\'{name}\';'
        # print(sql)

        try:
            if not hasattr(self, 'conn') or not self.conn.is_connected():
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return 1

        except Error as e:
            print('Failed:', e)
            return -1

    def add_record(self, name, record):
        records = self.select_records(name)

        records.append(record)
        records = json.dumps(records)
        self.update_records(name, records)
