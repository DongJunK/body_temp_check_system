import sqlite3
import sys
import os
from sqlite3 import Error

class Sqlite:
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

    def data_insertion(self, conn):
        c = conn.cursor()
        c.execute("INSERT INTO temp(name,update_time) VALUES('yes',CURRENT_TIMESTAMP)")
        conn.commit()

    def data_selection(self, conn):
        c = conn.cursor()
        c.execute("SELECT * FROM temp")
        rows = c.fetchall()

        return rows


    def main(self):
        sql_create_table = """ CREATE TABLE IF NOT EXISTS temp(
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        update_time datetime
                                    ); """
        path = os.getcwd() + "\\testing.db"
        print(path)
        conn = self.create_connection(path)

        if conn is not None:
            self.create_table(self, conn, sql_create_table)
            try:
                self.data_insertion(self, conn)
            except Error as e:
                print(e)

            #self.data_selection(self, conn)
        else:
            print("Error, cannot create the database connection")

        list = self.data_selection(self, conn)

        print(list)

        conn.close()

if __name__ == '__main__':
    Sqlite.main(Sqlite)