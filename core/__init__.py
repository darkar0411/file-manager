from os.path import dirname, basename, isfile
import glob
from tkinter import Tk, IntVar
import webbrowser
import json

modules = glob.glob(dirname(__file__) + "/*.py")

__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


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
        self.STATE = IntVar()


    def send_about(self):
        webbrowser.open(self.ABOUT)

    def get_info(self, file):
        try:
            with open(f'./conf/{file}.json', 'r') as f:
                read = json.load(f)
            return read

        except Exception as e:
            print('Error: ', e)
