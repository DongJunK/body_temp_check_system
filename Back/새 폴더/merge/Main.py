import os
from BringLog import GetLog as Log
from ConnectionDB import Connection as ConnDB
from Parse import Parsing
from SQL import SQL_Syntax
from ThreadTimer import perpetualTimer as threadTimer
from datetime import datetime

import datetime
import time

path = os.getcwd() + "\\database.db"
sql_create_init_table = """ CREATE TABLE IF NOT EXISTS log(
                                                    id integer PRIMARY KEY,
                                                    raspberry_pi_serial_number text NOT NULL,
                                                    student_number INTEGER NOT NULL,
                                                    temperature text NOT NULL,
                                                    logtime date INTEGER NOT NULL,
                                                    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                                                ); """
sql_create_student_table = """ CREATE TABLE IF NOT EXISTS student1(
                                                            student_id integer PRIMARY KEY,
                                                            student_name text NOT NULL,
                                                            student_phone text,
                                                            student_major text NOT NULL
                                                            ); """

sql_create_raspberry_table = """ CREATE TABLE IF NOT EXISTS raspberry(
                                                            id integer PRIMARY KEY,
                                                            raspberry_number text NOT NULL,
                                                            build_name text NOT NULL
                                                            ); """


def getData():
    db_query = SQL_Syntax(path)  # Initialization(Constructor)
    db_query.setCreateTable(sql_create_init_table, sql_create_student_table, sql_create_raspberry_table)  # Table Create

    last_update = db_query.get_last_log_timestamp()  # Get latest log datetime in Table return type is datetime
    get_log_class = Log(last_update)  # Bring log to IoT Makers parameter is start date
    log_list = get_log_class.get_log_list()  # Bring log return type is list

    print(log_list)
    del db_query

if __name__ == '__main__':
    # timer = threadTimer(5, getData)
    # start_time = timer.start()
    getData()
    # if (datetime.datetime.now().timestamp() - start_time)/60 > 1 :
    #     timer.cancel()
