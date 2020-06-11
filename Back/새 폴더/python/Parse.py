import os
from BringLog import GetLog as Log
from CreateDB import Create as ConnDB
from SQL import SQL_Syntax
import datetime
import time


class Parsing:

    def db_insert(self, conn, par_form):
        parse = par_form.split("_")
        if len(parse) != 4: # Data Form Checking
            if len(parse) < 4:
                print("Omission Error ", end="")
                print(parse)
            elif len(parse) > 4:
                print("Format Error ", end="")
                print(parse)
        else:
            c = conn.cursor()
            print(parse)
            c.execute("INSERT INTO temp(raspberry_pi_serial_number, student_number, temperature, logtime) "
                      "VALUES(?,?,?,?)", (parse[0], parse[1], parse[2], parse[3]))
            conn.commit()
            c.close()

    def data_normalization(self, conn, log):
        del log[0]
        latest = None
        if len(log) != 0:
            for dic in log:
                log_time = dic.get('occDt')
                log_data = dic.get('attributes').get('test')
                if log_time is not None and log_data is not None:
                    self.db_insert(conn, log_data + '_' + log_time)
                    log_datetime = datetime.datetime.strptime(log_time, '%Y-%m-%d %H:%M:%S.%f')
                    if latest is None or latest < log_datetime:
                        latest = log_datetime

                else:
                    print("Omission ; Log Time Stamp is {}, Data is {}".format(log_time, log_data))

        else:
            print("Latest Version")

        return latest
