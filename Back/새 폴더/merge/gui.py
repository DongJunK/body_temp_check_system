import sqlite3
from tkinter import *
from tkcalendar import *
from tkinter import ttk
from SQL import SQL_Syntax as Sql
from Parse import Parsing
from BringLog import GetLog as Log
from ThreadTimer import perpetualTimer as threadTimer
import datetime
import os
from re import search
import sys
from tkinter import messagebox as tmb

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


class MyApp:
    allData = None
    tem = 37.5

    def __init__(self, master):

        self.master = master

        # 데이터베이스 테이블
        self.table_frame = Frame(self.master)
        self.table_frame.place(x=30, y=50)

        self.scrollbar = ttk.Scrollbar(self.table_frame)
        self.treeview = ttk.Treeview(self.table_frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.treeview.yview)
        self.attribute()
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.pack()

        # [달력] 날짜
        self.calendar_img = PhotoImage(file='calendar_resize.png')
        self.calendar_label = Label(self.master, image=self.calendar_img)
        self.calendar_label.place(x=30, y=15)

        self.calendar = DateEntry(self.master, width=10, bg="darkblue", fg="white", date_pattern='yyyy-mm-dd', justify=CENTER)
        self.calendar.place(x=63, y=23)

        # ['전체목록', '의심환자'] 조회
        self.combobox = ttk.Combobox(self.master, width=8,  height=2) # postcommand, justify=CENTER
        self.combobox['values'] = (' 전체목록', ' 의심환자')
        self.combobox.set(' 전체목록') # 선택
        self.magnifier = PhotoImage(file='magnifier.png')
        self.search_button = Button(self.master, image=self.magnifier, text='조회', command=self.click_search, compound=LEFT)
        self.combobox.place(x=697, y=23)
        self.search_button.place(x=780, y=20)

        self.combobox.current(0) # Add

        # treeview click
        # self.treeview.bind("<Double-1>", self.OnDoubleClick)
        self.treeview.bind("<<TreeviewSelect>>", self.OnDoubleClick)

        # 마지막 수정 시간
        self.time_frame = Frame(self.master)
        self.time_frame.place(x=610, y=280)
        self.text_label = Label(self.time_frame, text='마지막 수정 시간')
        self.time_label = Label(self.time_frame, text='-')
        self.text_label.grid(row=0, column=0)
        self.time_label.grid(row=0, column=1)

        # 최근 로그 시간 get_last_log_timestamp()
        conn = Sql(path)
        log_time = str(conn.get_last_log_timestamp())
        if conn.get_last_log_timestamp() is None:
            log_time = '-'
        del conn

        self.logText_label = Label(self.time_frame, text='최근 로그 시간')
        self.logTime_Label = Label(self.time_frame, text=log_time[:19])
        self.logText_label.grid(row=1, column=0)
        self.logTime_Label.grid(row=1, column=1)

        

        # Auto Updating
        self.autoUpdate()
        self.click_search()

    def attribute(self):
        self.treeview['columns'] = ['1', '2', '3', '4', '5']
        self.treeview['show'] = 'headings'
        self.treeview.column('1', anchor='c', width=150)  # anchor='c' 가운데 정렬
        self.treeview.heading('1', text="출입 장소")
        self.treeview.column('2', anchor='c', width=150)
        self.treeview.heading('2', text='학번')
        self.treeview.column('3', anchor='c', width=150)
        self.treeview.heading('3', text='성명')
        self.treeview.column('4', anchor='c', width=150)
        self.treeview.heading('4', text='체온')
        self.treeview.column('5', anchor='c')
        self.treeview.heading('5', text='출입 시간')

    def click_search(self):
        data = []
        for i in self.allData:
            if search(self.calendar.get(), i[4][:10]):
                data.append(i)

        for row in self.treeview.get_children():
            self.treeview.delete(row)

        self.style = ttk.Style()
        self.style.map('Treeview', foreground=self.fixed_map('foreground'), background=self.fixed_map('background'))
        self.treeview.tag_configure('P', background='#ffcbc4') # 의심환자 background color
        if '선택' != self.combobox.get():
            if ' 전체목록' == self.combobox.get():
                for row in data:
                    try:
                        if float(row[3]) > self.tem:
                            self.treeview.insert("", END, values=row, tags='P')
                        else:
                            self.treeview.insert("", END, values=row)
                    except ValueError as v:
                        print(v)

            if ' 의심환자' == self.combobox.get():
                for row in data:
                    try:
                        if float(row[3]) > self.tem:
                            self.treeview.insert("", END, values=row)
                    except ValueError as v:
                        print(v)

            # 조회 버튼 클릭시 마지막 수정 시간 출력
            last_time = str(datetime.datetime.today())
            self.time_label.configure(text=last_time[:19])

    def fixed_map(self, option):
        # Fix for setting text colour for Tkinter 8.6.9
        # From: https://core.tcl.tk/tk/info/509cafafae
        #
        # Returns the style map for 'option' with any styles starting with
        # ('!disabled', '!selected', ...) filtered out.

        # style.map() returns an empty list for missing options, so this
        # should be future-safe.
        return [elm for elm in self.style.map('Treeview', query_opt=option) if
                elm[:2] != ('!disabled', '!selected')]

    def OnDoubleClick(self, event):
        item = self.treeview.selection()[0]
        select_student_number = self.treeview.item(item).get('values')[1]

        sql = Sql(path)
        info = sql.get_student_data(select_student_number)
        del sql
        
        info_window = Toplevel()
        info_window.title('학사 정보')
        info_window.geometry('272x105')
        info_window.resizable(False, False)

        info_id = Label(info_window, text='학   번', width=15, bg='#bdbdbd')
        student_id = Label(info_window, text=info[0][0], width=20, bg='white')
        info_id.place(x=5, y=5)
        student_id.place(x=120, y=5)
        info_name = Label(info_window, text='성   명', width=15, bg='#bdbdbd')
        student_name = Label(info_window, text=info[0][1], width=20, bg='white')
        info_name.place(x=5, y=30)
        student_name.place(x=120, y=30)
        info_major = Label(info_window, text='소속전공', width=15, bg='#bdbdbd')
        student_major = Label(info_window, text=info[0][3], width=20, bg='white')
        info_major.place(x=5, y=55)
        student_major.place(x=120, y=55)
        info_phone = Label(info_window, text='전화번호', width=15, bg='#bdbdbd')
        student_phone = Label(info_window, text=info[0][2], width=20, bg='white')
        info_phone.place(x=5, y=80)
        student_phone.place(x=120, y=80)

        info_window.mainloop()

    def getData(self):
        db_query = Sql(path)  # Initialization(Constructor)
        db_query.setCreateTable(sql_create_init_table)  # Table Create
        dbData = db_query.get_join_data()
        last_update = db_query.get_last_log_timestamp()  # Get latest log datetime in Table return type is datetime

        log = Log(last_update)  # Bring log to IoT Makers parameter is start date
        log_list = log.get_log_list()  # Bring log return type is list
        par = Parsing(path)
        data = par.db_insert(log_list)

        del db_query

        if self.allData is None:
            self.allData = dbData
        else:
            if len(self.allData) == len(dbData):
                return None
            else:
                sub = len(dbData) - len(self.allData)
                self.allData = dbData
                return dbData[0:sub]

    def autoUpdate(self):
        new_data = self.getData()
        if new_data is not None:
            for item in new_data:
                if self.combobox.get() == " 의심환자":
                    if 37.5 < float(item[3]) and search(self.calendar.get(), item[4][:10]):
                        self.treeview.insert("", 0, values=item)
                elif search(self.calendar.get(), item[4][:10]):
                    self.treeview.insert("", 0, values=item)


if __name__ == '__main__':
    window = Tk()
    window.title('교내 출입 기록')
    window.geometry("870x340")
    window.resizable(False, False)
    my_App = MyApp(window)
    timer = threadTimer(5, lambda : my_App.autoUpdate())
    timer.start()

    window.mainloop()


