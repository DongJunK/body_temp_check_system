import sqlite3
from sqlite3 import Error

class Create:
    path = None
    db_conn = None
    sql_create_syntax = None

    def __init__(self, path, sql_create_syntax):
        self.path = path
        self.sql_create_syntax = sql_create_syntax

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