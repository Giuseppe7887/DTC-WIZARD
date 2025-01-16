from PySide6.QtWidgets import QStatusBar
from app.components import Loader



class StatusBar(QStatusBar):
    def __init__(self):
        super().__init__()
        self.build()
    

    def build(self):
        self.loader = Loader()
        self.addWidget(self.loader, stretch=1)
    