import sqlite3
from sqlite3 import Error

class Create:
    path = None
    db_conn = None

    def __init__(self, path):
        self.path = path
        self.db_conn = self.create_connection(self.path)
        self.create_table(self.path, self.db_conn, self.sql_create_table)
        return self.db_conn

    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        finally:
            if conn:
                return conn

    def create_table(self, conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)

        except Error as e:
            print(e)

    def __del__(self):
        if self.db_conn is not None:
            self.db_conn.close()