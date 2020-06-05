import sqlite3
import sys
import os
from parsing import getLog as Log
from CreateDB import Create as ConnDB
from sqlite3 import Error
from SQL import SQL_Syntax

path = os.getcwd() + "\\database.db"
sql_create_table = """ CREATE TABLE IF NOT EXISTS temp(
                                                    id integer PRIMARY KEY,
                                                    name text NOT NULL,
                                                    temperature text
                                                ); """

class Sqlite:

    def parsing(self, conn, log_list):
        c = conn.cursor()
        if 'TouchSensor' in log_list:
            c.execute("INSERT INTO temp(name,temperature) VALUES('TouchSensor',?)",(log_list['TouchSensor'],))
        elif 'TempSensor' in log_list:
            c.execute("INSERT INTO temp(name,temperature) VALUES('TempSensor',?)", (log_list['TempSensor'],))
        conn.commit()

    def data_insertion(self,conn):
        getLogClass = Log()
        log_list = getLogClass.get_log_list()
        for dic in log_list:
            sensor_dic = dic.get('attributes')
            self.parsing(self, conn, sensor_dic)

    def data_selection(self, conn):
        c = conn.cursor()
        c.execute("SELECT * FROM temp")
        rows = c.fetchall()

        return rows


    def main(self):

        db_conn = ConnDB(path)

        Bring = SQL_Syntax(db_conn)

        print(Bring.bring_All_data())

        #del db_conn

if __name__ == '__main__':
    Sqlite.main(Sqlite)