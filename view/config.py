from core import Base

class Config(Base):

    def __init__(self):
        super().__init__()
        self.title("Config")
        self.geometry("500x500")