from PySide6.QtWidgets import QWidget,QVBoxLayout, QSpacerItem,QSizePolicy
from app.components import Logger,Dashboard

class Main(QWidget):
    def __init__(self)->None:
        super().__init__()
        self.setup()
        self.build()
    
    def setup(self)->None:
        self.resize(700,500)
            
    def build(self)->None:
        self.layout = QVBoxLayout()
        
        self.dashboard = Dashboard()
        self.logger = Logger()

        self.layout.addWidget(self.dashboard)
        self.layout.addItem(QSpacerItem(0,30,QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        self.layout.addWidget(self.logger)

        self.setLayout(self.layout)