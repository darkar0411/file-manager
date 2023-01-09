from core import Base
from core.components import Button, Text, CheckButton, Container
import json


class Config(Base):
    FILE: str = 'config'


    def __init__(self):
        super().__init__()
        self.title('config - app')

        self.opn_btn = Button(self, 'change type btn', {
            'row': 0, 'column': 0
        }, command=self.handle_opn_btn)
        
    def handle_opn_btn(self):
        inf = self.read_json(file=self.FILE)
        inf['btn-opt-style'] = 'true' if inf['btn-opt-style'] == 'false' else 'false'
        with open('./config.json', 'w') as f:
            json.dump(inf, f, indent=4)
        
        self.info_msg('please restart the app')
        