import datetime
import sqlite3
from sqlite3 import Error
import inspect
import os




class Student:
    conn = None
    # path = os.getcwd() + "\\database.db"
    sql_create_student_table = """ CREATE TABLE IF NOT EXISTS student1(
                                                                student_id integer PRIMARY KEY,
                                                                student_name text NOT NULL,
                                                                student_phone text,
                                                                student_major text NOT NULL
                                                                ); """
    source = [[5293550,'박찬섭','010-9423-1475','컴퓨터공학과'], [5360123,'이강희','010-3331-4081','컴퓨터공학과']
              ,[5293291,'김동준','010-9224-1427','컴퓨터공학과'], [5416212,'김영란','010-2672-4188','컴퓨터공학과']
              ,[5293490,'박성연','010-1234-5678','경제학과'], [5293520,'박수진','010-1111-2222','디자인학과']
              ,[5293690,'오승철','010-6666-1123','실용음악과'], [5293715,'윤주현','010-4434-1345','경영학과']
              ,[5294053,'황재현','010-7777-8888','화학공학과'], [5293794,'이성윤','010-4444-5555','심리학과']]


    def __init__(self, conn):
        try:
            self.conn = conn
            #self.conn = sqlite3.connect(conn)
        except Error as e:
            print(e)
        finally:
            if self.conn is not None:
                c = self.conn.cursor()
                c.execute(self.sql_create_student_table)

                for i in self.source:
                    try:
                        c.execute("INSERT INTO student1(student_id, student_name, student_phone, student_major) "
                                  "VALUES(?,?,?,?)", (i[0], i[1], i[2], i[3]))
                        self.conn.commit()
                    except sqlite3.IntegrityError:
                        # print(i,end='')
                        # print(' Already have it')
                        continue
                c.close()

    # def __del__(self):
    #     self.conn.close()


# if __name__ == '__main__':
#     a = Student(os.getcwd() + "\\database.db")