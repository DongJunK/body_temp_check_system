import datetime
import sqlite3
from sqlite3 import Error
import inspect
import os




class Raspberry:
    conn = None
    path = os.getcwd() + "\\database.db"
    sql_create_raspberry_table = """ CREATE TABLE IF NOT EXISTS raspberry(
                                                                id integer PRIMARY KEY,
                                                                raspberry_number text NOT NULL,
                                                                build_name text NOT NULL
                                                                ); """
    source = [['rasp1','공과대학']]


    def __init__(self):

        try:
            self.conn = sqlite3.connect(self.path)
        except Error as e:
            print(e)
        finally:
            if self.conn is not None:
                c = self.conn.cursor()
                c.execute(self.sql_create_raspberry_table)
                for i in self.source:
                    c.execute("INSERT INTO raspberry(raspberry_number, build_name) "
                              "VALUES(?,?)", (i[0], i[1]))
                    self.conn.commit()

                c.close()

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    a = Raspberry()
    del a