import sqlite3
import sys
import os
from parsing import getLog as Log
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

    def parsing(self, conn, log_list):
        c = conn.cursor()
        if 'TouchSensor' in log_list:
            c.execute("INSERT INTO temp3(name,temperature) VALUES('TouchSensor',?)",(log_list['TouchSensor'],))
        elif 'TempSensor' in log_list:
            c.execute("INSERT INTO temp3(name,temperature) VALUES('TempSensor',?)", (log_list['TempSensor'],))
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
        sql_create_table = """ CREATE TABLE IF NOT EXISTS temp3(
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        temperature text
                                    ); """
        path = os.getcwd() + "\\testing.db"
        # print(path)
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