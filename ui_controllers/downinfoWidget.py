from PySide6.QtWidgets import QWidget,QFileDialog,QMessageBox
from PySide6.QtCore import Signal,Qt
# 假设 Ui_Form 是从您的 .ui 文件通过 pyuic 生成的  
from generated_ui.Ui_downinfo import Ui_DownInfo  # 确保这里的路径是正确的  
import json
class DownInfoWidget(QWidget):  
    def __init__(self, parent=None):  
        super(DownInfoWidget, self).__init__(parent)  
        self.ui = Ui_DownInfo() 
        self.ui.setupUi(self)  
        self.total_down = 0
        self.downloading = 0
        self.down_pasue = 0
        self.down_finish = 0
        self.down_queue = 0
        self.total_downChanged.connect(lambda x:self.ui.total_down.setText(str(x)))
        self.downloadingChanged.connect(lambda x:self.ui.downloading.setText(x))
        self.down_pasueChanged.connect(lambda x:self.ui.down_pasue.setText(x))
        self.down_finishChanged.connect(lambda x:self.ui.down_finish.setText(str(self.down_finish)))
        self.down_queueChanged.connect(lambda x:self.ui.down_queue.setText(str(x)))

    total_downChanged = Signal(int)
    downloadingChanged = Signal(int)
    down_pasueChanged = Signal(int)
    down_finishChanged = Signal()
    down_queueChanged = Signal(int)


    def push_total_down(self,new_total_down):
        self.total_down += new_total_down
        self.total_downChanged.emit(self.total_down)

    def set_downloading(self,new_downloading):
        if self.downloading == new_downloading:
            return
        self.downloading = new_downloading
        self.downloadingChanged.emit(self.downloading)

    def set_down_pasue(self,new_down_pasue):
        if self.down_pasue == new_down_pasue:
            return
        self.down_pasue = new_down_pasue
        self.down_pasueChanged.emit(self.down_pasue)

    def add_down_finish(self):
        self.down_finish += 1
        self.down_finishChanged.emit()

    def set_down_queue(self,new_down_queue):
        if self.down_queue == new_down_queue:
            return
        self.down_queue = new_down_queue
        self.down_queueChanged.emit(self.down_queue)

    