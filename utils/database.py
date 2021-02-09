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

    def select(self, id, name):
        sql = f'SELECT Records FROM {self.table} WHERE ID=\'{id}\' AND Name=\'{name}\';'
        print(sql)

        try:
            if not hasattr(self, 'conn') or not self.conn.is_connected():
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(sql)
            record = cursor.fetchone()[0]
            return record

        except Error as e:
            print('Failed:', e)
            return -1

    def update(self, id, name, records):
        sql = f'UPDATE {self.table} SET Records=\'{records}\' WHERE ID=\'{id}\' AND Name=\'{name}\';'
        print(sql)

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

    def insert(self, id, name, records):
        sql = f'INSERT INTO {self.table} (ID, Name, Records) VALUES (\'{id}\', \'{name}\', \'{records}\');'
        print(sql)

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

    def delete(self, id, name):
        sql = f'DELETE FROM {self.table} WHERE ID=\'{id}\' AND Name=\'{name}\';'
        print(sql)

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

    def add_record(self, id, name, record):
        raw = self.select(id, name)
        records = json.loads(raw)

        records.append(record)
        records = json.dumps(records)
        self.update(id, name, records)
