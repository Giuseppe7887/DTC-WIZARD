from PySide6.QtWidgets import QLabel,QWidget, QHBoxLayout
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt
from state import state



class Loader(QWidget):
    def __init__(self):
        super().__init__()
        self.build()
        self.events()
    

    def build(self):
        lay = QHBoxLayout()
        lab = QLabel("")
        lab.setFixedHeight(10)
        self.mov = QMovie("assets/loading2.gif")
        lab.setMovie(self.mov)
        lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lay.addStretch()
        lay.addWidget(lab)
        lay.addStretch()
        self.setLayout(lay)
        self.show()
        self.mov.start()
    
    def events(self):
        def changed(val:bool):
            if val:
                self.show()
                self.mov.start()
            else:
                self.mov.stop()
                self.hide()


        state.obd_connection_signal.connect(changed)
        state.scanning_signal.connect(changed)
        state.cleaning_signal.connect(changed)


        
