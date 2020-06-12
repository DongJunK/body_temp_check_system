import os
import sqlite3
import sys
from BringLog import GetLog as Log
from ConnectionDB import Connection as ConnDB
import datetime
from sqlite3 import Error
import inspect


class SQL_Syntax:
    db_conn = None

    def __init__(self, path):
        db_conn = ConnDB(path)
        self.db_conn = db_conn.set_create_connection()

    def Try_Except(self, db_cursor, method, sql):
        try:
            db_cursor.execute(sql)
            rows = db_cursor.fetchall()
            db_cursor.close()
            return rows
        except Error as e:
            print(method, end=' /Error is ')
            print(e)

    def setCreateTable(self, sql_initTable_syntax, sql_studentTable_syntax, sql_raspberryTable_syntax):
        try:
            c = self.db_conn.cursor()
            c.execute(sql_initTable_syntax)
            c.execute(sql_studentTable_syntax)
            c.execute(sql_raspberryTable_syntax)
            c.close()
        except Error as e:
            print(e)

    def get_All_data(self):
        sql = "SELECT * FROM log"
        db_cursor = self.db_conn.cursor()
        return self.Try_Except(db_cursor, inspect.stack()[0][3], sql) # inspect.stack()[0][3] is method name

    def get_data_by_SQL(self, sql_syntax):
        db_cursor = self.db_conn.cursor()
        return self.Try_Except(db_cursor, inspect.stack()[0][3], sql_syntax)

    def get_data_about_temperature_upper(self, temp):
        db_cursor = self.db_conn.cursor()
        sql_syntax = "SELECT * FROM temp3 WHERE temp >= " + temp
        return self.Try_Except(db_cursor, inspect.stack()[0][3], sql_syntax)

    def get_last_log_timestamp(self):
        sql_syntax = "SELECT logtime FROM log"
        db_cursor = self.db_conn.cursor()
        db_datetime_list = self.Try_Except(db_cursor, inspect.stack()[0][3], sql_syntax)
        if db_datetime_list is None:
            return None
        else:
            latest = None
            for date_time in db_datetime_list:
                time = datetime.datetime.strptime(''.join(date_time), '%Y-%m-%d %H:%M:%S.%f')
                if latest is None or latest < time:
                    latest = time
            return latest

    def get_student_data(self, student_id):
        sql_syntax = "SELECT * FROM student1 WHERE student_id={}".format(int(student_id))
        db_cursor = self.db_conn.cursor()
        return self.Try_Except(db_cursor, inspect.stack()[0][3], sql_syntax)

    def __del__(self):
        self.db_conn.close()

    def insert_tempTable(self, list):
        db_cursor = self.db_conn.cursor()
        try:
            try:
                int(list[1])
            except ValueError:
                list[1] = int(0)
            db_cursor.execute("INSERT INTO log(raspberry_pi_serial_number, student_number, temperature, logtime) "
                      "VALUES(?,?,?,?)", (list[0], list[1], list[2], list[3]))
            self.db_conn.commit()
            return True
        except Error as e:
            print(e)
            return False
        finally:
            db_cursor.close()

    def get_join_data(self):
        db_cursor = self.db_conn.cursor()
        sql_syntax = "SELECT A.build_name, A.student_number, S.student_name, A.temperature, A.logtime  " \
                     "FROM (log  as L JOIN raspberry AS R)AS A JOIN student1 AS S  ON L.raspberry_pi_serial_number = R.raspberry_number AND A.student_number = S.student_id" \
                     " ORDER BY A.logtime DESC"
        return self.Try_Except(db_cursor, inspect.stack()[0][3], sql_syntax)


    # def convert_to_csv(self):
    #     com_te = ""
    #     data = self.bring_All_data()
    #     print(data)
    #     for row in data:
    #         for m in range(1, 9):
    #             com_te = com_te + str(row[m]) + ","
    #         com_te = com_te + "\n"
    #     f = open("addr.csv", "w")
    #     f.write(com_te)
    #     f.close
    #     self.db_conn.close()
    #     print("CSV file export done.")
