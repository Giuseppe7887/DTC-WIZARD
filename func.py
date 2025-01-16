from PySide6.QtCore import QThread, Signal, Qt,QTimer
import obd


# connection = obd.OBD() # auto-connects to USB or RF port

# clear_cmd = obd.commands.CLEAR_DTC # select an OBD command (sensor)
# get_cmd = obd.commands.GET_DTC


# x = obd.commands.RPM

# res = connection.query(clear_cmd)


# print(res)



# # [('P2002', 'Particulate Trap Efficiency Below Threshold'), ('P2002', 'Particulate Trap Efficiency Below Threshold')]



    


class Scan(QThread):
    
    result_signal = Signal(list)
    error_signal = Signal(str)

    def __init__(self):
        super().__init__()
      
        self.result = []

    
    def run(self):

        conn = obd.OBD()
        
        if conn.is_connected():
            res = conn.query(obd.commands.GET_DTC)
            res = [list(x) for x in res.value]
            
            for x in res:
                x.append(Qt.GlobalColor.red)
            self.result_signal.emit(res)
        else:
            self.error_signal.emit("No connection, please check your obd adapter")
            self.result_signal.emit([])


class Clear(QThread):

    result_signal = Signal(bool)
    error_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.result = False
    
    def run(self):
        conn = obd.OBD()
        self.result_signal.emit(True)
        
        if conn.is_connected():
            conn.query(obd.commands.CLEAR_DTC)
            read_res = conn.query(obd.commands.GET_DTC)

            no_dtc = len(read_res.value) == 0
            self.result_signal.emit(no_dtc)

        else:

            self.error_signal.emit("No connection, please check your obd adapter")
            self.result_signal.emit([])




class TestObdConnection(QThread):

    connection_signal = Signal(obd.OBD)

    def __init__(self):
        super().__init__()
        self.connection = None

    
    def run(self):
        self.connection = obd.OBD()
        self.connection_signal.emit(self.connection)

        