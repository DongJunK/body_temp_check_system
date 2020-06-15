import datetime
import sqlite3
from sqlite3 import Error
import inspect
import os




class Student:
    conn = None
    path = os.getcwd() + "\\database.db"
    sql_create_student_table = """ CREATE TABLE IF NOT EXISTS student1(
                                                                student_id integer PRIMARY KEY,
                                                                student_name text NOT NULL,
                                                                student_phone text,
                                                                student_major text NOT NULL
                                                                ); """
    source = [[5293550,'박찬섭','010-9423-1475','컴퓨터공학과'], [5360123,'이강희','010-3331-4081','컴퓨터공학과']
              ,[5293291,'김동준','010-9224-1427','컴퓨터공학과'], [5416212,'김영란','010-2672-4188','컴퓨터공학과']]


    def __init__(self):

        try:
            self.conn = sqlite3.connect(self.path)
        except Error as e:
            print(e)
        finally:
            if self.conn is not None:
                c = self.conn.cursor()
                c.execute(self.sql_create_student_table)
                for i in self.source:
                    c.execute("INSERT INTO student1(student_id, student_name, student_phone, student_major) "
                              "VALUES(?,?,?,?)", (i[0], i[1], i[2], i[3]))
                    self.conn.commit()

                c.close()

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    a = Student()
    del a