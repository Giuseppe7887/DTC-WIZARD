from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
from state import state

class Logger(QTableWidget):
    
    def __init__(self):
        super().__init__()
        self.events()
        self.build()
    
    def build(self):
        cols = ["Code", "Description"]

        self.setColumnCount(2)
        self.setRowCount(0)
        self.setHorizontalHeaderLabels(cols)


        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.resizeRowsToContents()
        self.resizeColumnsToContents()


    def events(self):
        def cb(res:list):
            lun = len(res)
            self.setRowCount(lun)

            def build_item(text:str,color)->QTableWidgetItem:
                item = QTableWidgetItem(text)
                item.setForeground(color)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                return item



            for i, row in enumerate(res):
                color = row[2]
                code =build_item(row[0],color)
                name =build_item(row[1],color)
                
                self.setItem(i,0,code)
                self.setItem(i,1,name)

        state.results_signal.connect(cb)