import os
import sqlite3
import sys
from BringLog import GetLog as Log
import datetime
from sqlite3 import Error
import inspect


class SQL_Syntax:
    db_conn = None

    def __init__(self, db_conn):
        self.db_conn = db_conn

    def Try_Except(self, db_cursor, method, sql):
        try:
            db_cursor.execute(sql)
            rows = db_cursor.fetchall()
            db_cursor.close()
            return rows
        except Error as e:
            print(method, end=' /Error is ')
            print(e)

    def setCreateTable(self, sql_syntax):
        try:
            c = self.db_conn.cursor()
            c.execute(sql_syntax)

        except Error as e:
            print(e)

    def get_All_data(self):
        sql = "SELECT * FROM temp"
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
        sql_syntax = "SELECT logtime FROM temp"
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
