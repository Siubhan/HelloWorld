from tkinter import *
from tkinter import ttk
import sqlite3


class Table(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.sw = parent.winfo_screenwidth()
        self.sh = parent.winfo_screenheight()
        self.centerWindow()
        self.initUI()
        self.db = db
        self.view_records()

    def initUI(self):
        self.parent.title("Table")
        self.pack(fill=BOTH, expand=1)
        self.x = 0
        self.y = 0
        exit_button = Button(self, text="Выйти", command=self.quit)
        exit_button.place(x=20, y=320)
        start_button = Button(self, text="Удалить", command=self.rem_data)  # сommand
        start_button.place(x=200, y=320)
        add_button = Button(self, text="Добавить", command=self.open_dialog)
        add_button.place(x=300, y=320)
        self.tree = ttk.Treeview(self, columns=('subject'), height=13, show='headings')
        self.tree.column('subject', width=150, anchor=CENTER)
        self.tree.heading('subject', text='Предмет')
        self.tree.pack()



    def centerWindow(self):
        w = 400
        h = 350
        x = (self.sw - w) / 2
        y = (self.sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def records(self, subj):
        self.db.insert_data(subj)
        self.view_records()

    def rem_data(self):
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item)['values'][0]
        self.db.del_data(values)
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT subject FROM subjects''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()


class Child(Toplevel):
    def __init__(self):
        super().__init__()
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить предмет')
        self.geometry('350x150+400+300')
        self.resizable(False, False)
        self.label_subj = Label(self, text="Предмет")
        self.label_subj.place(x=20, y=40)
        self.entry_subj = Entry(self)
        self.entry_subj.place(x=100, y=40)
        self.btn_cencer = Button(self, text="Закрыть", command=self.destroy)
        self.btn_cencer.place(x=210, y=100)
        self.btn_add = Button(self, text="Добавить")
        self.btn_add.place(x=100, y=100)
        self.btn_add.bind("<Button-1>",
                          lambda event: self.view.records(self.entry_subj.get()))
        self.grab_set()
        self.focus_set()


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('table.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS subjects (id int AUTO_INCREMENT primary key,subject text)''')
        self.conn.commit()

    def insert_data(self, sub):
        self.c.execute('''INSERT INTO subjects(subject) VALUES (?)''',
                       (sub,))
        self.conn.commit()

    def del_data(self, sub):
        self.c.execute(''' delete from subjects where  subject = ?''',
                       (sub,))
        self.conn.commit()


if __name__ == '__main__':
    root = Tk()
    db = DB()
    app = Table(root)
    root.resizable(False, False)
    root.mainloop()
