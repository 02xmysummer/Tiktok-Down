import sys
from PySide6.QtWidgets import QMainWindow,QWidget,QMessageBox
sys.path.append("ui\\uic")
from Ui_mainwindow import Ui_MainWindow
from spiderMgr import SpiderMgr
from Ui_download import Ui_Form
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
        res = self.spiderMgr.addTask(user_url=self.ui.url_edit.text()) 
        if res:
            download_widget = QWidget()  
            download_ui = Ui_Form()  
            download_ui.setupUi(download_widget)  # 设置 Ui_Form 的布局到新的 QWidget 实例上  

                # 将新的 QWidget 实例添加到 tabWidget 中  
            self.ui.tabWidget.addTab(download_widget, self.spiderMgr.tasks[-1].nikename + "的视频列表")  # 使用更有意义的标签名  
            download_ui.add_down_list(self.spiderMgr.tasks[-1].titles)

                
