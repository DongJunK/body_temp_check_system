import os
from BringLog import GetLog as Log
from SQL import SQL_Syntax
import datetime
import time



class Parsing:
    path = None

    def __init__(self,path):
        self.path = path

    def db_insert(self, par_form):
        parse = par_form.split("_")
        if len(parse) != 4: # Data Form Checking
            if len(parse) < 4:
                print("Omission Error ", end="")
                print(parse)
            elif len(parse) > 4:
                print("Format Error ", end="")
                print(parse)
        else:
            print(parse)
            insert = SQL_Syntax(self.path)
            if insert.insert_tempTable(parse):
                print("SUCCESS")
            else:
                print("ERROR")
            del insert

    def data_normalization(self, log):
        del log[0]
        latest = None
        if len(log) != 0:
            for dic in log:
                log_time = dic.get('occDt')
                log_data = dic.get('attributes').get('test')
                if log_time is not None and log_data is not None:
                    self.db_insert(log_data + '_' + log_time)
                    log_datetime = datetime.datetime.strptime(log_time, '%Y-%m-%d %H:%M:%S.%f')
                    if latest is None or latest < log_datetime:
                        latest = log_datetime

                else:
                    print("Omission ; Log Time Stamp is {}, Data is {}".format(log_time, log_data))

        else:
            print("Latest Version")

        return latest
