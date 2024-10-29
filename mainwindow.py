import sys
from PySide6.QtWidgets import QMainWindow
sys.path.append("ui\\uic")
from Ui_mainwindow import Ui_MainWindow
from spiderMgr import SpiderMgr
class QMainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.spiderMgr = SpiderMgr()
        self.ui.setupUi(self)
        self.spiderMgr.user_url = self.ui.url_edit.text()
        self.ui.find_btn.clicked.connect(self.on_find_btn_clicked)
    def on_find_btn_clicked(self):  
        # 在这里获取文本框的内容，并调用 set_user_url 方法  
        self.spiderMgr.set_user_url(user_url=self.ui.url_edit.text()) 
        self.spiderMgr.get_media_url()