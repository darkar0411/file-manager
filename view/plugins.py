from core import Base
from core.components import Table, Text, Button
import git, os


class Plugins(Base):
    URL: str = "https://raw.githubusercontent.com/luisdanielta/file-manager-plugins/main/plugins.json"
    DATA: list

    def __init__(self):
        super().__init__()
        self.title("Plugins")

        self.DATA = self.fetch(self.URL)

        self.table = Table(self, ("Name", "Author", "Description", "Version"), {
            'row': 0, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5, 'columnspan': 2
        })
        self.__update_table()

        self.install = Button(self, "Install", {
            'row': 1, 'column': 0, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        }, command=self.__handle_install)

        self.uninstall = Button(self, "Uninstall", {
            'row': 1, 'column': 1, 'sticky': 'nsew',
            'padx': 5, 'pady': 5
        })

    def __update_table(self):
        self.table.delete(*self.table.get_children())
        for plugin in self.DATA:
            self.table.insert('', 'end', values=(
                plugin['name'], plugin['author'], plugin['description'], plugin['version']))

    def __handle_install(self):
        item_id = self.table.selection()[0]
        item = self.table.item(item_id, 'values')
        name = item[0]

        if self.__validate_install(name):
            self.error_msg(msg="Plugin already installed")
            return

        plugin = next((p for p in self.DATA if p['name'] == name), None)
        if plugin is None:
            self.error_msg(msg="Plugin not found")
            return

        try:
            git.Git().clone(plugin['url'], f"plugins/{name}")
            self.info_msg(msg="Plugin installed successfully")
        except Exception as e:
            self.error_msg(msg=e)

    def __handle_uninstall(self):
        pass

    def __validate_install(self, name: str):
        return os.path.exists(f"plugins/{name}")

