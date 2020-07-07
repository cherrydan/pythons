#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  pymysql import *

import tkinter as tk

import tkinter.ttk as ttk

class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show='headings', selectmode='browse')
        table['columns'] = headings
        table['displaycolumns'] = headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)

data = tuple()

con = connect('localhost', 'root', '', 'base')

with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM country_pop')
    data = (row for row in cur.fetchall())

root = tk.Tk()
table = Table(root, headings=('Id', 'Country', 'Year', 'Population'), rows=data)
table.pack(expand=tk.YES, fill = tk.BOTH)
root.mainloop()
