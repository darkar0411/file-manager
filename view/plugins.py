from core import Base
from core.components import Table

class Plugins(Base):

    URL: str = "https://raw.githubusercontent.com/luisdanielta/file-manager-plugins/main/plugins.json"

    def __init__(self):
        super().__init__()
        self.title("Plugins")
    
        
