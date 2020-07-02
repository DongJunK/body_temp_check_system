import sqlite3
from sqlite3 import Error

class Connection:
    path = None
    db_conn = None

    def __init__(self, path):
        self.path = path

    def set_create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.path)
        except Error as e:
            print(e)
        finally:
            if conn:
                return conn


    def __del__(self):
        if self.db_conn is not None:
            self.db_conn.close()