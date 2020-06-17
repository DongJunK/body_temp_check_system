import datetime
import sqlite3
from sqlite3 import Error
import inspect
import os




class Raspberry:
    conn = None
    # path = os.getcwd() + "\\database.db"
    sql_create_raspberry_table = """ CREATE TABLE IF NOT EXISTS raspberry(
                                                                id integer PRIMARY KEY,
                                                                raspberry_number text NOT NULL UNIQUE,
                                                                build_name text NOT NULL
                                                                ); """
    source = [['rasp1','공과대학'], ['rasp2','사회대학']
              ,['rasp3','인문대학'], ['rasp4','대학원']
              ,['rasp5','사회과학대학'], ['rasp6','본관']
              ,['rasp7','간호학과']]


    def __init__(self, conn):

        try:
            self.conn = conn
        except Error as e:
            print(e)

        finally:
            if self.conn is not None:
                c = self.conn.cursor()
                c.execute(self.sql_create_raspberry_table)
                for i in self.source:
                    try:
                        c.execute("INSERT INTO raspberry(raspberry_number, build_name) "
                                  "VALUES(?,?)", (i[0], i[1]))
                        self.conn.commit()
                    except sqlite3.IntegrityError:
                        # print(i, end='')
                        # print('Already have it')
                        continue
                c.close()
    #
    # def __del__(self):
    #     self.conn.close()

#
# if __name__ == '__main__':
#     a = Raspberry()
#     del a