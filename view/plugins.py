from core import Base
from core.components import Table, Text, Button


class Plugins(Base):

    URL: str = "https://raw.githubusercontent.com/luisdanielta/file-manager-plugins/main/plugins.json"
    DATA: list

    def __init__(self):
        super().__init__()
        self.title("Plugins")

        self.DATA = self.fetch(self.URL)

        self.table = Table(self, ["name", "author", "last update"], {
            "row":0, "column":0
        })

        self.btn_install = Button(self, "Install", {
            "row":1, "column":0
        })