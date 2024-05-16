import tkinter as tk
from tkinter import ttk
import controller


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self['background'] = '#EBEBEB'
        self.conf = {'padx': 20, 'pady': 20}
        self.bold_font = 'Helvetica 13 bold'
        self.attributes('-fullscreen', True)
        self.put_frames()
        self.put_menu()

    def put_frames(self):
        self.frame_info = FrameInfo()
        self.frame_info.place(relx=0, rely=0, relwidth=1, relheight=0.25)
        self.frame_list = FrameList()
        self.frame_list.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

    def refresh(self):
        all_frames = [f for f in self.children]
        for frame in all_frames:
            self.nametowidget(frame).destroy()
        self.put_frames()
        self.put_menu()

    def put_menu(self):
       self.config(menu=MainMenu())
class MainMenu(tk.Menu):
    def __init__(self):
        super().__init__()


        self.add_cascade(label="Добавить", command=lambda: AddForm())
        self.add_cascade(label="Поиск", command=lambda: SearchForm())
        self.add_cascade(label="Удалить", command=lambda: FrameDeletion())

class AddForm(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self['background'] = self.master['background']
        self.put_widgets()
    def put_widgets(self):
        self.l_name = ttk.Label(self, text="Введите имя")
        self.l_course = ttk.Label(self, text="Введите курс")
        self.l_group = ttk.Label(self, text="Введите группу")
        self.l_total_number_of_works = ttk.Label(self, text="Введите общее число работ")
        self.l_number_of_completed_works = ttk.Label(self, text="Введите количество выполненных работ")
        self.l_programming_language = ttk.Label(self, text="Введите язык программирования")
        self.r_name = ttk.Entry(self, justify=tk.RIGHT)
        self.r_course = ttk.Entry(self, justify=tk.RIGHT)
        self.r_group = ttk.Entry(self, justify=tk.RIGHT)
        self.r_total_number_of_works = ttk.Entry(self, justify=tk.RIGHT)
        self.r_number_of_completed_works = ttk.Entry(self, justify=tk.RIGHT)
        self.r_programming_language = ttk.Combobox(self, values=controller.open_languages_file())
        self.btn_submit = ttk.Button(self, text='Добавить', command=self.form_submit)

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        self.l_name.grid(row=0, column=0, sticky='w', cnf=self.master.conf)
        self.l_course.grid(row=1, column=0, sticky='w', cnf=self.master.conf)
        self.l_group.grid(row=2, column=0, sticky='w', cnf=self.master.conf)
        self.l_total_number_of_works.grid(row=3, column=0, sticky='w', cnf=self.master.conf)
        self.l_number_of_completed_works.grid(row=4, column=0, sticky='w', cnf=self.master.conf)
        self.l_programming_language.grid(row=5, column=0, sticky='w', cnf=self.master.conf)
        self.r_name.grid(row=0, column=1, sticky='w', cnf=self.master.conf)
        self.r_course.grid(row=1, column=1, sticky='w', cnf=self.master.conf)
        self.r_group.grid(row=2, column=1, sticky='w', cnf=self.master.conf)
        self.r_total_number_of_works.grid(row=3, column=1, sticky='w', cnf=self.master.conf)
        self.r_number_of_completed_works.grid(row=4, column=1, sticky='w', cnf=self.master.conf)
        self.r_programming_language.grid(row=5, column=1, sticky='w', cnf=self.master.conf)
        self.btn_submit.grid(row=6, column=0, sticky='n', cnf=self.master.conf)

    def form_submit(self):
        name = self.r_name.get()
        course = int(self.r_course.get())
        group = int(self.r_group.get())
        total_number_of_works = int(self.r_total_number_of_works.get())
        number_of_completed_works = int(self.r_number_of_completed_works.get())
        programming_language = self.r_programming_language.get()
        controller.save_student_file(name, course, group, total_number_of_works, number_of_completed_works,
                                     programming_language)
        self.master.refresh()


class SearchForm(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        self.l_name = ttk.Label(self, text="Введите имя")
        self.l_course = ttk.Label(self, text="Введите курс")
        self.l_group = ttk.Label(self, text="Введите группу")
        self.l_total_number_of_works = ttk.Label(self, text="Введите общее число работ")
        self.l_number_of_completed_works = ttk.Label(self, text="Введите количество выполненных работ")
        self.l_programming_language = ttk.Label(self, text="Введите язык программирования")
        self.r_name = ttk.Entry(self, justify=tk.RIGHT)
        self.r_course = ttk.Entry(self, justify=tk.RIGHT)
        self.r_group = ttk.Entry(self, justify=tk.RIGHT)
        self.r_total_number_of_works = ttk.Entry(self, justify=tk.RIGHT)
        self.r_number_of_completed_works = ttk.Entry(self, justify=tk.RIGHT)
        self.r_programming_language = ttk.Combobox(self, values=controller.open_languages_file())
        self.btn_submit = ttk.Button(self, text='Поиск', command=self.form_find)

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        self.l_name.grid(row=0, column=0, sticky='w', cnf=self.master.conf)
        self.l_course.grid(row=1, column=0, sticky='w', cnf=self.master.conf)
        self.l_group.grid(row=2, column=0, sticky='w', cnf=self.master.conf)
        self.l_total_number_of_works.grid(row=3, column=0, sticky='w', cnf=self.master.conf)
        self.l_number_of_completed_works.grid(row=4, column=0, sticky='w', cnf=self.master.conf)
        self.l_programming_language.grid(row=5, column=0, sticky='w', cnf=self.master.conf)
        self.r_name.grid(row=0, column=1, sticky='w', cnf=self.master.conf)
        self.r_course.grid(row=1, column=1, sticky='w', cnf=self.master.conf)
        self.r_group.grid(row=2, column=1, sticky='w', cnf=self.master.conf)
        self.r_total_number_of_works.grid(row=3, column=1, sticky='w', cnf=self.master.conf)
        self.r_number_of_completed_works.grid(row=4, column=1, sticky='w', cnf=self.master.conf)
        self.r_programming_language.grid(row=5, column=1, sticky='w', cnf=self.master.conf)
        self.btn_submit.grid(row=6, column=0, sticky='n', cnf=self.master.conf)

    def form_find(self):
        name = self.r_name.get()
        course = self.r_course.get()
        group = self.r_group.get()
        total_number_of_works = self.r_total_number_of_works.get()
        number_of_completed_works = self.r_number_of_completed_works.get()
        programming_language = self.r_programming_language.get()
        print(name, course, group, total_number_of_works,
                                        number_of_completed_works, programming_language)
        controller.find_student_in_file(name, course, group, total_number_of_works,
                                        number_of_completed_works, programming_language)
        self.master.refresh()

class FrameDeletion(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        self.l_name = ttk.Label(self, text="Введите имя")
        self.l_course = ttk.Label(self, text="Введите курс")
        self.l_group = ttk.Label(self, text="Введите группу")
        self.l_total_number_of_works = ttk.Label(self, text="Введите общее число работ")
        self.l_number_of_completed_works = ttk.Label(self, text="Введите количество выполненных работ")
        self.l_programming_language = ttk.Label(self, text="Введите язык программирования")
        self.r_name = ttk.Entry(self, justify=tk.RIGHT)
        self.r_course = ttk.Entry(self, justify=tk.RIGHT)
        self.r_group = ttk.Entry(self, justify=tk.RIGHT)
        self.r_total_number_of_works = ttk.Entry(self, justify=tk.RIGHT)
        self.r_number_of_completed_works = ttk.Entry(self, justify=tk.RIGHT)
        self.r_programming_language = ttk.Combobox(self, values=controller.open_languages_file())
        self.btn_submit = ttk.Button(self, text='Поиск', command=self.form_dell)

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        self.l_name.grid(row=0, column=0, sticky='w', cnf=self.master.conf)
        self.l_course.grid(row=1, column=0, sticky='w', cnf=self.master.conf)
        self.l_group.grid(row=2, column=0, sticky='w', cnf=self.master.conf)
        self.l_total_number_of_works.grid(row=3, column=0, sticky='w', cnf=self.master.conf)
        self.l_number_of_completed_works.grid(row=4, column=0, sticky='w', cnf=self.master.conf)
        self.l_programming_language.grid(row=5, column=0, sticky='w', cnf=self.master.conf)
        self.r_name.grid(row=0, column=1, sticky='w', cnf=self.master.conf)
        self.r_course.grid(row=1, column=1, sticky='w', cnf=self.master.conf)
        self.r_group.grid(row=2, column=1, sticky='w', cnf=self.master.conf)
        self.r_total_number_of_works.grid(row=3, column=1, sticky='w', cnf=self.master.conf)
        self.r_number_of_completed_works.grid(row=4, column=1, sticky='w', cnf=self.master.conf)
        self.r_programming_language.grid(row=5, column=1, sticky='w', cnf=self.master.conf)
        self.btn_submit.grid(row=6, column=0, sticky='n', cnf=self.master.conf)

    def form_dell(self):
        name = self.r_name.get()
        course = self.r_course.get()
        group = self.r_group.get()
        total_number_of_works = self.r_total_number_of_works.get()
        number_of_completed_works = self.r_number_of_completed_works.get()
        programming_language = self.r_programming_language.get()
        print(name, course, group, total_number_of_works,
              number_of_completed_works, programming_language)
        controller.dell_student_in_file(name, course, group, total_number_of_works,
                                        number_of_completed_works, programming_language)
        self.master.refresh()


class FrameList(tk.Frame):
    def __init__(self,):
        super().__init__()
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        heads = ['ФИО', 'Курс', 'Группа', 'Общее число работ', 'Количество выполненных работ', 'Язык программирования']
        table = ttk.Treeview(self, show='headings')
        table['columns'] = heads

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')

        for row in controller.open_student_file("/EXAMPLE/example.xml"):
            table.insert('', tk.END, values=row)

        scroll_pane = ttk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


class FrameInfo(tk.Frame):
    def __init__(self,):
        super().__init__()
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        heads = ['ФИО', 'Курс', 'Группа', 'Общее число работ', 'Количество выполненных работ', 'Язык программирования']
        table = ttk.Treeview(self, show='headings')
        table['columns'] = heads

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')

        for row in controller.open_student_file("/INFO/info.xml"):
            table.insert('', tk.END, values=row)

        scroll_pane = ttk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


view = View()
view.mainloop()