import sqlite3
from tkinter import *
from tkcalendar import *
from tkinter import ttk
from SQL import SQL_Syntax as Sql
import datetime
import os

path = os.getcwd() + "\\database.db"

class MyApp:
    def __init__(self, master):
        self.master = master

        # 데이터베이스 테이블
        self.table_frame = Frame(self.master)
        self.table_frame.place(x=45, y=60)

        self.scrollbar = ttk.Scrollbar(self.table_frame)
        self.treeview = ttk.Treeview(self.table_frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.treeview.yview)
        self.attribute()
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.pack()

        # [달력] 날짜
        self.calendar_frame = Frame(self.master)
        self.calendar_frame.place(x=45, y=25)

        self.calendar_img = PhotoImage(file='83-calendar-icon.png')
        self.calendar_label = Label(self.calendar_frame, image=self.calendar_img)
        self.calendar_label.grid(row=0, column=0)

        self.calendar = DateEntry(self.calendar_frame, width=10, bg="darkblue", fg="white", date_pattern='yyyy-mm-dd', justify=CENTER)
        self.calendar.grid(row=0, column=1)

        # ['전체목록', '의심환자'] 조회
        self.search_frame = Frame(self.master)
        self.combobox = ttk.Combobox(self.calendar_frame, width=10,  height=2) # postcommand, justify=CENTER
        self.combobox['values'] = (' 전체목록', ' 의심환자')
        self.combobox.set(' 선택')
        self.search_button = Button(self.search_frame, text='Q 조회', command=self.click_search)
        self.combobox.grid(row=0, column=2)

        self.combobox.current(0) # Add

        self.search_button.grid(row=0, column=1)
        self.search_frame.place(x=700, y=30)


        #Treeview click
        self.treeview.bind("<Double-1>", self.OnDoubleClick)

        # 마지막 수정 시간
        self.time_frame = Frame(self.master)
        self.text_label = Label(self.time_frame, text='마지막 수정 시간')
        self.time_label = Label(self.time_frame)

    def OnDoubleClick(self,event):
        item = self.treeview.selection()[0]
        select_student_number = self.treeview.item(item).get('values')[2]
        print(select_student_number)
        sql = Sql(path)
        print(sql.get_student_data(select_student_number))
        #i = Sql.get_student_data(select_student_number)



    def attribute(self):
        self.treeview['columns'] = ['1', '2', '3', '4', '5']
        self.treeview['show'] = 'headings'
        self.treeview.column('1', anchor='c', width=90)  # anchor='c' 가운데 정렬
        self.treeview.column('2', anchor='c', width=140)
        self.treeview.column('3', anchor='c', width=140)
        self.treeview.column('4', anchor='c')
        self.treeview.column('5', anchor='c', width=130)
        self.treeview.heading('1', text="id")
        self.treeview.heading('2', text='serial num')
        self.treeview.heading('3', text='student num')
        self.treeview.heading('4', text='log time')
        self.treeview.heading('5', text='temperature')

    def click_search(self):
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        conn = sqlite3.connect('database.db')  # 파일과 연결
        c = conn.cursor()  # 커서 설정

        if '선택' != self.combobox.get():
            if ' 전체목록' == self.combobox.get():
                c.execute("SELECT * FROM temp")  # temp 테이블 조회
                tuples = c.fetchall()
                for row in tuples:
                    self.treeview.insert("", END, values=row)
            if ' 의심환자' == self.combobox.get():
                c.execute("SELECT * FROM temp WHERE temperature>38")
                tuples = c.fetchall()
                for row in tuples:
                    self.treeview.insert("", END, values=row)

            # 조회 버튼 클릭시 마지막 수정 시간 출력
            self.time_label.configure(text=datetime.datetime.today())
            self.time_frame.place(x=570, y=290)
            self.text_label.pack()
            self.time_label.pack()


window = Tk()
window.title('교내 출입 기록')
window.geometry("800x350")
window.resizable(False, False)
MyApp(window)

window.mainloop()


