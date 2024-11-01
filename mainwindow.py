import sys
from PySide6.QtWidgets import QMainWindow,QWidget,QMessageBox,QPushButton,QListWidget
from PySide6.QtCore import Signal
sys.path.append("ui\\uic")
from generated_ui.Ui_mainwindow import Ui_MainWindow
from custom_classes.spiderMgr import SpiderMgr
from ui_controllers.uservedioinfo import UserVedioInfo
from ui_controllers.settingsWidget import SettingsWidget
import asyncio
class QMainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.settingWidget = SettingsWidget()
        self.spiderMgr = SpiderMgr()
        self.ui.setupUi(self)
        self.spiderMgr.set_configs(self.settingWidget.configs)
        self.ui.find_btn.clicked.connect(self.find_btn_clicked)
        self.ui.tabWidget.currentChanged.connect(self.conn)
        self.ui.down_setting.clicked.connect(lambda:self.settingWidget.show())
        self.settingWidget.configsChanged.connect(self.spiderMgr.set_configs)

    def find_btn_clicked(self): 
        # 在这里获取文本框的内容，并调用 set_user_url 方法  
        if self.ui.url_edit.text() == "":
            return
        res = self.spiderMgr.addTask(user_url=self.ui.url_edit.text()) 
        if res:
            self.add_tab(self.spiderMgr.tasks[-1].nikename,self.spiderMgr.tasks[-1].titles,self.spiderMgr.tasks[-1].vedio_addrs,self.ui.url_edit.text())
            
        else:
            QMessageBox.question(self, 'eror',  
                                     "链接解析失败", QMessageBox.Cancel , QMessageBox.Cancel)  


    def add_tab(self,title_name,titles,vedio_addrs,user_url):
        download_widget = UserVedioInfo()  
        download_widget.set_title(title_name)
        download_widget.add_down_list(titles,vedio_addrs,user_url)
        self.ui.tabWidget.addTab(download_widget, title_name)  # 使用更有意义的标签名  

    def conn(self,index):
        if index >= 2:
            currentWidget = self.ui.tabWidget.currentWidget()
            down_btn = currentWidget.findChild(QPushButton, "down_btn")
            down_btn.clicked.connect(self.get_select_indexs)

    def get_select_indexs(self): 
        index = self.ui.tabWidget.currentIndex()
        currentWidget = self.ui.tabWidget.currentWidget()
        listWidget = currentWidget.findChild(QListWidget, "listWidget")
        count = listWidget.count()  
        cb_list = [listWidget.itemWidget(listWidget.item(i)) for i in range(count)]  
        length = len(cb_list)
        chooses = []  
        vedio_addrs = currentWidget.ui.vedio_addrs
        titles = currentWidget.ui.titles
        user_url = currentWidget.ui.user_url
        nikename = self.ui.tabWidget.tabText(index)
        for i in range(length):  
            if cb_list[i].isChecked():  
                chooses.append(i)  
        asyncio.run(self.spiderMgr.down_vedio(nikename,titles,vedio_addrs,chooses,user_url))
