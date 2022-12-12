from os.path import dirname, basename, isfile
import glob
from tkinter import Tk, IntVar, filedialog, messagebox
import webbrowser
import json
import time
import shutil
import os

modules = glob.glob(dirname(__file__) + "/*.py")

__all__ = [basename(f)[:-3] for f in modules if isfile(f)
           and not f.endswith('__init__.py')]


class Base(Tk):
    OS: str
    PATH: str
    SEND: str
    ABOUT: str = 'https://github.com/luisdanielta'

    BUTTONS: list
    LABELS: list

    def __init__(self):
        super().__init__()
        self.BUTTONS = self.get_info('files')
        self.LABELS = self.get_info('files').keys()
        self.STATE = IntVar
        self.OP_BTNS = True if self.__get_config(
            'OP_BTNS') == 'True' else False

        # key bindings - exit ESC
        self.bind('<Escape>', lambda e: self.destroy())

    def send_about(self):
        webbrowser.open(self.ABOUT)

    def get_info(self, file):
        try:
            with open(f'./conf/{file}.json', 'r') as f:
                read = json.load(f)
            return read

        except Exception as e:
            print('Error: ', e)

    def __get_config(self, opt):
        try:
            with open('./config.conf', 'r') as f:
                read = f.read()

                # parse config
                for line in read.split('\n'):
                    if line.startswith(opt):
                        return str(line.split('=')[1])
        except Exception as e:
            print('Error: ', e)

    def open_folder(self):
        self.PATH = filedialog.askdirectory()

    def find_subf(self):
        try:
            folders = []
            for folder in glob.glob(self.PATH + '/**/*', recursive=True):
                if os.path.isdir(folder):
                    folders.append(folder)
            return folders
        except Exception as e:
            messagebox.showerror('Error', e)

    def move_file(self, file, path, type_btn, ext):
        try:
            if file.endswith(tuple(ext)):
                shutil.move(f'{path}/{file}', f'{self.PATH}/{type_btn}/{file}')
        except Exception as e:
            print(e)

    def copy_file(self, file, path, type_btn, ext):
        try:
            if file.endswith(tuple(ext)):
                shutil.copy(f'{path}/{file}', f'{self.PATH}/{type_btn}')
        except Exception as e:
            print(e)

    def warning_msg(self, active=None, msg=None):
        if active is not None:
            messagebox.showwarning('Warning', msg)
        else:
            messagebox.showwarning('Warning', msg)

    def error_msg(self, active=None, msg=None):
        if active is not None:
            messagebox.showerror('Error', msg)
        else:
            messagebox.showerror('Error', msg)

    def info_msg(self, active=None, msg=None):
        if active is not None:
            messagebox.showinfo('Info', msg)
        else:
            messagebox.showinfo('Info', msg)
