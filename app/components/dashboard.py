from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton,QMessageBox
from PySide6.QtCore import Qt
from state import state
from func import Scan, Clear


def show_error_box(err):
    msg = QMessageBox()
    state.cleaning = False
    state.scanning = False

    # Imposta l'icona come 'Critical' per rappresentare un errore
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setText("An error occurred")
    msg.setInformativeText(err)
    msg.setWindowTitle("Error")
    msg.exec()  # Mostra il dialog



class Dashboard(QWidget):

    def __init__(self):
        super().__init__()
        self.setup()
        self.build()
        self.bindings()
        self.scan_thread = None

    def setup(self):
        self.setFixedHeight(100)


    def build(self):

        
        self.layout = QHBoxLayout()

        self.scan_dtc_btn = QPushButton("Start scanning")
        self.clear_dtc_btn = QPushButton("Reset DTC")
        self.scan_dtc_btn.setStyleSheet("padding: 15 0 15 0")
        self.clear_dtc_btn.setStyleSheet("padding: 15 0 15 0")
        # self.clear_dtc_btn.setDisabled(True)

        self.layout.addWidget(self.scan_dtc_btn)
        self.layout.addWidget(self.clear_dtc_btn)

        self.setLayout(self.layout)
    
    def bindings(self):

        def start_dtc_scan():
            state.results = []
            state.scanning = True
            self.scan_dtc_btn.setDisabled(True)
            self.clear_dtc_btn.setDisabled(True)

            def cb(res:list): # RES VIENE GESTITO DIRETTAMENTE NEL THREAD
                state.scanning = False
                self.scan_dtc_btn.setDisabled(False)

                if len(res) > 0:
                    self.clear_dtc_btn.setDisabled(False)
                

                state.results = res

            
            self.thread = Scan()
            self.thread.start()
            self.thread.result_signal.connect(cb)
            self.thread.error_signal.connect(show_error_box)
            
            

        def clear_dtc():
            state.cleaning = True
            self.scan_dtc_btn.setDisabled(True)
            self.clear_dtc_btn.setDisabled(True)

            def cb(res:bool): # RES VIENE GESTITO DIRETTAMENTE NEL THREAD
                state.cleaning = False
                self.scan_dtc_btn.setDisabled(False)
                if res:
                    # ! changing table item color from red to green
                    old_list = state.results # [ [] ]
                    new_list = []

                    for x in old_list:
                        x.pop()
                        x.append(Qt.GlobalColor.green)
                        new_list.append(x)

                    state.results = new_list          

                
            self.thread = Clear()
            self.thread.start()
            self.thread.result_signal.connect(cb)
            self.thread.error_signal.connect(show_error_box)

        def update(val):
            self.scan_dtc_btn.setText("Scanning.." if val else "Start scanning")

        state.scanning_signal.connect(update)
        self.scan_dtc_btn.clicked.connect(start_dtc_scan)
        self.clear_dtc_btn.clicked.connect(clear_dtc)

    

    
        
    
