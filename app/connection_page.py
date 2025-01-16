from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt
from func import TestObdConnection
import obd
from state import state


class ConnectionPage(QWidget):
    def __init__(self,cb):
        super().__init__()
        self.conn = None
        self.err = ""
        self.cb = cb
        self.build()

    def build(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Connecton in progress..",self)

        self.layout.addWidget(self.label,alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.layout)
        self.try_connect()

        if self.err != "":
            self.err_orccurred()
            state.obd_connecting = False
        

    
    def try_connect(self):
        state.obd_connecting = True
        self.label.setText("Connecton in progress..")
        try:self.button.hide()
        except AttributeError: pass

        def cb(conn:obd.OBD):
            if conn.is_connected():
                self.err = ""
                state.obd = conn
                self.cb()
            else:
                self.err = conn.status()
                self.err_orccurred()

            state.obd_connecting = False
            
                
        self.conn = TestObdConnection()
        self.conn.connection_signal.connect(cb)
        self.conn.start()

    def err_orccurred(self):
            self.button = QPushButton("Retry",self)
            self.button.clicked.connect(self.try_connect)
            
            self.label.setText("An error occurred, please retry")
            self.layout.addWidget(self.button)
    

