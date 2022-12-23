from core import Base, glob
import os
import shutil
import time
from core.components import Button, Container, CheckButton
from core.components import Table, AppMenu, MenuButton, Text
from view.config import Config
from view.plugins import Plugins


class App(Base):

    def __init__(self):
        super().__init__()
        self.txt_path = None
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
        self.p_btn = self.CONFIG['btn-position']
        for btn in self.LABELS:
            grid = {
                'row': self.p_btn[btn][0], 'column': self.p_btn[btn][1],
                'sticky': 'nsew', 'padx': 3, 'pady': 3
            }
            if self.OP_BTNS:
                globals()[btn] = Button(self.stf_btn, btn, grid=grid, state='disabled',
                                        command=lambda btn=btn: self.handle_stf_btn(btn))
            else:
                globals()[btn] = MenuButton(self.stf_btn, btn, grid=grid,
                                            options=self.BUTTONS[btn], state='disabled',
                                            command=lambda btn=self.BUTTONS[btn]: self.handle_stf_btn(btn))

        # container btn´s check´s
        self.ct_btn_check = Container(self, 'Tools', {
            'row': 3, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        })

        # btn check subfolders
        # msg_sbf = 'This option can take a long time, depending on the number of files and size.'
        self.subf_btn = CheckButton(self.ct_btn_check, 'Include subfolders', {
            'row': 2, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        }, variable=self.STATE)

        # btn check copy
        # msg_cp = 'Copying files can take a long time, depending on the number of files and size.'
        self.copy_btn = CheckButton(self.ct_btn_check, 'Copy files', {
            'row': 2, 'column': 1, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        }, variable=self.STATE)

        # btn check move
        self.move_btn = CheckButton(self.ct_btn_check, 'Move files', {
            'row': 2, 'column': 2, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        }, variable=self.STATE)

        # table routes Accion´s
        self.table = Table(self, ('Route', 'Accions', 'File'), {
            'row': 4, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        }, [150, 15, 15], height=5)
        self.__update_table()

        # container button´s table
        self.ct_btn = Container(self, 'Actions', {
            'row': 5, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        })

        self.ct_btn.columnconfigure(0, weight=1)
        self.ct_btn.columnconfigure(1, weight=1)

        # btn select accion
        self.sa_btn = Button(self.ct_btn, 'Select', {
            'row': 0, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        }, command=lambda: self.__select_accion())

        # btn delete accion
        self.da_btn = Button(self.ct_btn, 'Delete', {
            'row': 0, 'column': 1, 'sticky': 'nsew',
            'padx': 10, 'pady': 5
        })

    # handle event´s
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
            self.error_msg(msg='Select only one option (copy or move)')
            return

        if not copy and not move:
            self.error_msg(msg='Select one option (copy or move)')
            return

        types = self.read_json('/data', 'files')
        files = os.listdir(self.PATH)

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

        if subf == 1:
            for subfolder in self.__find_subf():
                files = os.listdir(subfolder)
                for file in files:
                    if move:
                        self.__move_file(file, subfolder, type_btn, ext)
                    elif copy:
                        self.__copy_file(file, subfolder, type_btn, ext)

        for file in files:
            if move:
                self.__move_file(file, self.PATH, type_btn, ext)
            elif copy:
                self.__copy_file(file, self.PATH, type_btn, ext)

        t_end = time.time()
        t = round(t_end - t_init, 2)

        # messagebox, process completed
        self.info_msg(msg=f'Process completed in {t} seconds.')
        # self.__save_accion()

    # more functions for handle events
    def __find_subf(self):
        try:
            folders = []
            for folder in glob.glob(self.PATH + '/**/*', recursive=True):
                if os.path.isdir(folder):
                    folders.append(folder)
            return folders
        except Exception as e:
            self.error_msg(msg=e)

    def __move_file(self, file, path, type_btn, ext):
        try:
            if file.endswith(tuple(ext)):
                shutil.move(f'{path}/{file}', f'{self.PATH}/{type_btn}/{file}')
        except Exception as e:
            print(e)

    def __copy_file(self, file, path, type_btn, ext):
        try:
            if file.endswith(tuple(ext)):
                shutil.copy(f'{path}/{file}', f'{self.PATH}/{type_btn}')
        except Exception as e:
            print(e)

    def __save_accion(self, type_btn):
        accion = "copy" if self.copy_btn.get_state() else "move"

        self.save_json('/data', 'recents', {
            'route': self.PATH,
            'accion': accion,
            'file': type_btn
        })
        self.__update_table()

    def __update_table(self):
        self.table.delete(*self.table.get_children())
        data = self.read_json('/data', 'recents')
        route = data['route'][::-1]  # reverse list
        accion = data['accion'][::-1]
        file = data['file'][::-1]

        for i in range(0, 5):
            try:
                self.table.insert('', 'end', text=i, values=(
                    route[i], accion[i], file[i]))
            except IndexError:
                pass

    def __select_accion(self):
        item = self.table.selection()[0]
        route = self.table.item(item, 'values')[0]
        accion = self.table.item(item, 'values')[1]
        file = self.table.item(item, 'values')[2]

        if accion == 'Copy':
            self.copy_btn.set_state(1)
            self.move_btn.set_state(0)

        else:
            self.copy_btn.set_state(0)
            self.move_btn.set_state(1)

        self.PATH = route

        self.handle_stf_btn(file)


if __name__ == "__main__":
    app = App()
    app.mainloop()
