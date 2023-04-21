from os.path import dirname, basename, isfile
import glob
from tkinter import Tk, IntVar, filedialog, messagebox
import webbrowser
import json
import requests


class Base(Tk):
    OS: str
    PATH: str
    ABOUT: str = 'https://github.com/luisdanielta'

    def __init__(self):
        super().__init__()
        self.BUTTONS = self.read_json('/data', 'files')
        self.LABELS = self.BUTTONS.keys()
        self.STATE = IntVar
        self.CONFIG = self.read_json(file='config')

        # key bindings - exit ESC
        self.bind('<Escape>', lambda e: self.destroy())

    def send_about(self):
        webbrowser.open(self.ABOUT)

    def read_json(self, folder='/', file=None):
        try:
            with open(f'.{folder}/{file}.json', 'r') as f:
                read = json.load(f)
            return read

        except Exception as e:
            print('Error: ', e)

    def save_json(self, folder='/', file=None, data=None):
        old_data = self.read_json(folder, file)
        labels = old_data.keys()

        for label in labels:
            old_data[label].append(data[label])

        with open(f'.{folder}/{file}.json', 'w') as f:
            json.dump(old_data, f, indent=4)

    def delete_json(self, folder, file, item):
        pass

    def open_folder(self):
        self.PATH = filedialog.askdirectory()

    # msg
    def warning_msg(self, msg=None):
        messagebox.showwarning('Warning', msg)

    def error_msg(self, msg=None):
        messagebox.showerror('Error', msg)

    def info_msg(self, msg=None):
        messagebox.showinfo('Info', msg)

    # requests
    def fetch(self, url: str):
        try:
            r = requests.get(url)
            return r.json()
        except Exception as e:
            print(e)


modules = glob.glob(dirname(__file__) + "/*.py")

__all__ = [basename(f)[:-3] for f in modules if isfile(f)
           and not f.endswith('__init__.py')]
