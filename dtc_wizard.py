from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from state import state

from app import Main,ConnectionPage

from app.components import StatusBar



debug = False

class DTCResetter(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.resize(700,500)
        self.setWindowIcon(QIcon("assets/icon.svg"))
        self.setWindowTitle("DTC WIZARD")
        self.build()
  
        
    def build(self):

        self.main = Main()
        self.connection_page = ConnectionPage(cb=self.connection_cb)
        self.status_bar = StatusBar()
        
        self.setStatusBar(self.status_bar)

        
        if state.obd_ok() or debug:
            self.setCentralWidget(self.main)
        else:
            self.setCentralWidget(self.connection_page)  
            
        
  
    def connection_cb(self):
        central_widget = self.centralWidget()
        if state.obd_ok():
            if central_widget == self.connection_page: # ? bug
                self.setCentralWidget(self.main)
        else:
            if central_widget != self.connection_page:
                self.setCentralWidget(self.connection_page)





if __name__ == "__main__":
    import sys
    app = QApplication()
    win = DTCResetter()
    win.show()
    sys.exit(app.exec())