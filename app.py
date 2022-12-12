from core import Base, glob, time, shutil, os
from core.components import Button, Container, CheckButton, Table, AppMenu, MenuButton, Text
from tkinter import messagebox
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
        }, command=self.handle_sf_btn)

        # btn select file
        self.stf_btn = Container(self, 'Select of types file', {  # container type file
            'row': 2, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        })

        # btn´s select types - position
        self.p_btn = self.get_info('position')['buttons']
        for btn in self.p_btn.keys():
            row = self.p_btn[btn][0]
            column = self.p_btn[btn][1]
            grid = {
                'row': row, 'column': column, 'sticky': 'nsew',
                'padx': 3, 'pady': 3
            }

            globals()[btn] = Button(self.stf_btn, btn, grid=grid,
                                    state='disabled',
                                    command=lambda btn=btn: self.handle_stf_btn(btn)) if self.OP_BTNS else MenuButton(
                self.stf_btn, btn, grid=grid, options=self.BUTTONS[btn],
                state='disabled', command=lambda btn=self.BUTTONS[btn]: self.handle_stf_btn(btn))

        # container btn check
        self.ct_btn_check = Container(self, 'Tools', {
            'row': 3, 'column': 0, 'sticky': 'nsew',
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
            'row': 4, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        }, [190, 60], height=5)

        # container buttons table
        self.ct_btn = Container(self, 'Actions', {
            'row': 5, 'column': 0, 'sticky': 'nsew',
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
            'padx': 10, 'pady': 5
        })

    # handle events

    def handle_sf_btn(self):
        self.open_folder()
        if self.PATH:
            self.txt_path = Text(self, self.PATH, {
                'row': 1, 'column': 0, 'sticky': 'nsew',
                'padx': 5, 'pady': 5
            }, anchor='center')
            for btn in self.p_btn.keys():
                globals()[btn].config(state='normal')

    def handle_stf_btn(self, type_btn):
        # get copy - move - subfolders
        t_init = time.time()
        copy = self.copy_btn.get_state()
        move = self.move_btn.get_state()
        subf = self.subf_btn.get_state()

        # messagebox, copy - move one select
        if copy and move:
            messagebox.showerror('Error', 'Select one option')
            return

        if not copy and not move:
            messagebox.showerror('Error', 'Select move or copy')
            return

        types = self.get_info('files')
        file = os.listdir(self.PATH)
        try:
            # add extension .upper()
            ext = types[type_btn]
            for i in range(len(ext)):
                ext.append(ext[i].upper())

        except KeyError:
            ext = [type_btn, type_btn.upper()]
            type_btn = type_btn.split('.')[1]

        if not os.path.exists(f'{self.PATH}/{type_btn}'):  # if folder not exists
            os.mkdir(f'{self.PATH}/{type_btn}')
        try:
            for file in file:
                if file.endswith(tuple(ext)):
                    if copy:
                        shutil.copy(os.path.join(self.PATH, file),
                                    f'{self.PATH}/{type_btn}')
                    elif move:
                        shutil.move(os.path.join(self.PATH, file),
                                    f'{self.PATH}/{type_btn}')
        except Exception as e:
            messagebox.showerror('Error', e)
            return

        t_end = time.time()
        messagebox.showinfo('Info',
                            f'Files {type_btn} {"copied" if copy else "moved"} in {round(t_end - t_init, 3)} seconds')


if __name__ == "__main__":
    app = App()
    app.mainloop()
