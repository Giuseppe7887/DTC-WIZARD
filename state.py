from PySide6.QtCore import QObject,Signal
import obd as obd_lib

class _State(QObject):
    scanning_signal = Signal(bool)
    cleaning_signal = Signal(bool)
    obd_loading = Signal(bool)
    results_signal = Signal(list)
    obd_connection_signal = Signal(obd_lib.OBD)

    def __init__(self):
        super().__init__()
        self._scanning = False
        self._cleaning = False
        self._obd_connecting = True
        self._results = []
        self._obd = None
    

    @property
    def scanning(self):
        return self._scanning

    @scanning.setter
    def scanning(self,value:bool):
        if value != self._scanning:
            self._scanning = value
            self.scanning_signal.emit(value)

    @property
    def cleaning(self):
        return self._cleaning

    @cleaning.setter
    def cleaning(self,value:bool):
        if value != self._cleaning:
            self._cleaning = value
            self.cleaning_signal.emit(value)
    
    @property
    def results(self):
        return self._results

    @results.setter
    def results(self,value:list):
        # if value != self._results:
            self._results = value
            self.results_signal.emit(value)

    
    @property
    def obd(self):
        return self._obd

    @obd.setter
    def obd(self,value:obd_lib.OBD):
        if value != self._obd:
            self._obd = value
            self.obd_connection_signal.emit(value)

        
    @property
    def obd_connecting(self):
        return self._obd_connecting

    @obd_connecting.setter
    def obd_connecting(self,value:obd_lib.OBD):
        if value != self._obd_connecting:
            self._obd_connecting = value
            self.obd_connection_signal.emit(value)

    
    
    def obd_ok(self)->bool:
        if self._obd == None :return False
        return self.obd.is_connected()
      
    



state = _State()