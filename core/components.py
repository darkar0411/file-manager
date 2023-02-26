from tkinter import ttk, Menu
from tkinter import *
import os


class Button(ttk.Button):

    def __init__(self, master, text='This is Button..!', grid: dict = None, state: str = None, command=None):
        super().__init__(master, text=text, state=state, command=command)
        self.grid(**grid)


class CheckButton(ttk.Checkbutton):

    def __init__(self, master, text, grid, variable=None, event=None):
        self.btn_state = variable()
        super().__init__(master, text=text, variable=self.btn_state)
        self.grid(**grid)

    def get_state(self):
        return self.btn_state.get()

    def set_state(self, state):
        self.btn_state.set(state)


class Container(ttk.LabelFrame):

    def __init__(self, master, text: str = None, grid: dict = None):
        super().__init__(master, text=text)
        self.grid(**grid)


class Table(ttk.Treeview):

    def __init__(self, master, columns=None, grid: dict = None, width=False, **kwargs):
        super().__init__(master, columns=columns, show='headings')
        self.grid(**grid)
        self.config(**kwargs)

        for column in columns:
            self.heading(column, text=column)
            self.column(
                column, width=width[columns.index(column)] if width else 100)


class AppMenu(Menu):

    def __init__(self, master, commands):
        super().__init__(master)
        self.commands = commands

        for command in self.commands.keys():
            self.add_command(label=command, command=self.commands[command])

        master.config(menu=self)


class MenuButton(ttk.Menubutton):

    def __init__(self, master, text='This is Menubutton..!', grid=None, options=None, state=None, command=None):
        super().__init__(master, text=text, state=state)
        self.grid(**grid)
        self.menu = Menu(self, tearoff=0)
        self['menu'] = self.menu

        for option in options:
            self.menu.add_command(
                label=option, command=lambda text=option: command(text))


class Text(ttk.Label):

    def __init__(self, master, text='This is Label..!', grid=None, **kwargs):
        super().__init__(master, text=text)
        self.grid(**grid)
        self.config(**kwargs)


class Image:
    pass