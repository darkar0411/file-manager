from core import Base
from core.components import Button, Container, CheckButton, Table, AppMenu, MenuButton
from view.config import Config
from view.plugins import Plugins


class App(Base):

    def __init__(self):
        super().__init__()
        self.title("File Manager")
        self.resizable(False, False)

        # menu
        self.menu = AppMenu(self, {
            'Config': Config,
            'Plugins': Plugins,
            'About': self.send_about,
            'Exit': self.destroy
        })

        # btn select folder
        self.sf_btn = Button(self, 'Select Folder', {
            'row': 0, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        })

        # btn select file
        self.stf_btn = Container(self, 'Select of types file', {  # container type file
            'row': 1, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        })

        # btn´s select types - position
        p_btn = self.get_info('position')['buttons']
        for btn in p_btn.keys():
            row = p_btn[btn][0]
            column = p_btn[btn][1]
            grid = {
                'row': row, 'column': column, 'sticky': 'nsew',
                'padx': 3, 'pady': 3
            }
            globals()[btn] = Button(self.stf_btn, btn, grid=grid,
                                    state='disabled') if self.OP_BTNS else MenuButton(
                self.stf_btn, btn, grid=grid, options=self.BUTTONS[btn], state='disabled')

        # container btn check
        self.ct_btn_check = Container(self, 'Tools', {
            'row': 2, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        })

        # btn check subfolders
        self.subf_btn = CheckButton(self.ct_btn_check, 'Include subfolders', {
            'row': 2, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        }, variable=self.STATE)

        # btn check copy
        self.copy_btn = CheckButton(self.ct_btn_check, 'Copy files', {
            'row': 2, 'column': 1, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        }, variable=self.STATE)

        # btn check move
        self.move_btn = CheckButton(self.ct_btn_check, 'Move files', {
            'row': 2, 'column': 2, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        }, variable=self.STATE)

        # table routes recents
        self.table = Table(self, ('Route', 'Date'), {
            'row': 3, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        }, [190, 60], height=5)

        # container buttons table
        self.ct_btn = Container(self, 'Actions', {
            'row': 4, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        })

        self.ct_btn.columnconfigure(0, weight=1)
        self.ct_btn.columnconfigure(1, weight=1)

        # btn select route
        self.sr_btn = Button(self.ct_btn, 'Select Route', {
            'row': 0, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        })

        # btn delete route
        self.dr_btn = Button(self.ct_btn, 'Delete Route', {
            'row': 0, 'column': 1, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        })


if __name__ == "__main__":
    app = App()
    app.mainloop()
