import os
from BringLog import GetLog as Log
from CreateDB import Create as ConnDB
from SQL import SQL_Syntax

path = os.getcwd() + "\\database.db"
sql_create_table = """ CREATE TABLE IF NOT EXISTS temp(
                                                    id integer PRIMARY KEY,
                                                    raspberry_pi_serial_number text NOT NULL,
                                                    student_number text NOT NULL,
                                                    temperature text NOT NULL,
                                                    logtime date INTEGER NOT NULL,
                                                    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                                                ); """


class Main:

    def parsing(self, conn, log_list):
        if log_list is  not None:
            c = conn.cursor()
            if 'TouchSensor' in log_list:
                #c.execute("INSERT INTO temp(name,temperature) VALUES('TempSensor',?)", (log_list['TouchSensor'],))
                print(type(log_list['TouchSensor']))
                # c.execute("INSERT INTO temp(raspberry_pi_serial_number, student_number, temperature, logtime) "
                #           "VALUES('TouchSensor',?)", (log_list['TouchSensor'],))
            elif 'TempSensor' in log_list:
                #c.execute("INSERT INTO temp(name,temperature) VALUES('TempSensor',?)", (log_list['TempSensor'],))
                print(type(log_list['TempSensor']))
            conn.commit()
        else :
            print("Log is Empty")
    def data_insertion(self, conn):
        get_log_class = Log()
        log_list = get_log_class.get_log_list()
        for dic in log_list:
            sensor_dic = dic.get('attributes')
            self.parsing(conn, sensor_dic)


if __name__ == '__main__':
    main_class = Main()
    database = ConnDB(path, sql_create_table)  # Initialization(Constructor)
    db_conn = database.set_create_connection()  # DataBase Connection

    db_query = SQL_Syntax(db_conn)  # Initialization(Constructor)
    db_query.setCreateTable(sql_create_table) # Table Create

    get_log_class = Log()
    log_list = get_log_class.get_log_list()

    print(log_list)
    main_class.data_insertion(db_conn)
    print(db_query.bring_All_data()) # Current Table print

    del db_conn  # DataBase Connection Close (destructor)
