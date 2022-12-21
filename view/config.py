from core import Base
from core.components import Button, Text, CheckButton, Container

class Config(Base):

    def __init__(self):
        super().__init__()
        self.title('config - app')
        
        self.container = Container(self, text='types style-options' ,grid={
            'row': 0, 'column': 0, 'sticky': 'nsew', 'padx': 10, 'pady': 10
        })
        self.button = Button(self.container, text='change style', grid={
            'row': 0, 'column': 0, 'sticky': 'nsew', 'padx': 10, 'pady': 10
        })

