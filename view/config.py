from core import Base
from core.components import Button, Text, CheckButton, Container


class Config(Base):
    FILE: str = 'config'

    def __init__(self):
        super().__init__()
        self.title('config - app')
        self.geometry('400x400')

        self.ec_ctn = Container(self, text='UI - exchange', grid={
            'row': 0, 'column': 0, 'sticky': 'nsew', 'padx': 10, 'pady': 10
        })
        self.cg_btn = Button(self.ec_ctn, text='change btn', grid={
            'row': 0, 'column': 0, 'sticky': 'nsew', 'padx': 5, 'pady': 5
        }, command=self.handle_cg_btn)

    def handle_cg_btn(self):
        print(self.read_json(file=self.FILE)['btn-opt-style'])
