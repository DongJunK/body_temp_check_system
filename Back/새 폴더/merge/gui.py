import sqlite3
from tkinter import *
from tkcalendar import *
from tkinter import ttk
from SQL import SQL_Syntax as Sql
import datetime
import os

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

    def __init__(self, master):
        self.master = master

        # 데이터베이스 테이블
        self.table_frame = Frame(self.master)
        self.table_frame.place(x=30, y=60)

        self.scrollbar = ttk.Scrollbar(self.table_frame)
        self.treeview = ttk.Treeview(self.table_frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.treeview.yview)
        self.attribute()
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.pack()

        # [달력] 날짜
        self.calendar_frame = Frame(self.master)
        self.calendar_frame.place(x=30, y=25)

        self.calendar_img = PhotoImage(file='83-calendar-icon.png')
        self.calendar_label = Label(self.calendar_frame, image=self.calendar_img)
        self.calendar_label.grid(row=0, column=0)

        self.calendar = DateEntry(self.calendar_frame, width=10, bg="darkblue", fg="white", date_pattern='yyyy-mm-dd', justify=CENTER)
        self.calendar.grid(row=0, column=1)

        # ['전체목록', '의심환자'] 조회
        self.search_frame = Frame(self.master)
        self.combobox = ttk.Combobox(self.calendar_frame, width=10,  height=2) # postcommand, justify=CENTER
        self.combobox['values'] = (' 전체목록', ' 의심환자')
        self.combobox.set(' 전체목록') # 선택
        self.search_button = Button(self.search_frame, text='Q 조회', command=self.click_search)
        self.combobox.grid(row=0, column=2)
        self.search_button.grid(row=0, column=1)
        self.search_frame.place(x=780, y=30)

        self.combobox.current(0) # Add

        # treeview click
        self.treeview.bind("<Double-1>", self.OnDoubleClick)

        # 마지막 수정 시간
        self.time_frame = Frame(self.master)
        self.time_frame.place(x=610, y=290)
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
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        conn = Sql(path)
        if '선택' != self.combobox.get():
            self.allData = conn.get_join_data()
            if ' 전체목록' == self.combobox.get():
                for row in self.allData:
                    self.treeview.insert("", END, values=row)
            if ' 의심환자' == self.combobox.get():
                for row in self.allData:
                    try:
                        if float(row[3]) > 38.0:
                            self.treeview.insert("", END, values=row)
                    except ValueError as v:
                        print(v)
            del conn

            # 조회 버튼 클릭시 마지막 수정 시간 출력
            last_time = str(datetime.datetime.today())
            self.time_label.configure(text=last_time[:19])

    def OnDoubleClick(self, event):
        item = self.treeview.selection()[0]
        num = int(item[1:], 16) # 16진수를 10진수로 변경
        info = self.allData[num-1]

        # select_student_number = self.treeview.item(item).get('values')[0]
        # print(select_student_number)

        info_window = Toplevel()
        info_window.title('학사 정보')
        info_window.geometry('300x300')
        info_window.resizable(False, False)

        info_id = Label(info_window, text='학번')
        student_id = Label(info_window, text=info[1])
        info_id.grid(row=0, column=0)
        student_id.grid(row=0, column=1)
        info_name = Label(info_window, text='성명')
        student_name = Label(info_window, text=info[2])
        info_name.grid(row=0, column=2)
        student_name.grid(row=0, column=3)
        info_major = Label(info_window, text='소속전공')
        student_major = Label(info_window, text=info[6])
        info_major.grid(row=1, column=0)
        student_major.grid(row=1, column=1)
        info_phone = Label(info_window, text='전화번호')
        student_phone = Label(info_window, text=info[5])
        info_phone.grid(row=2, column=0)
        student_phone.grid(row=2, column=1)

        info_window.mainloop()

window = Tk()
window.title('교내 출입 기록')
window.geometry("870x350")
window.resizable(False, False)
MyApp(window)

window.mainloop()


