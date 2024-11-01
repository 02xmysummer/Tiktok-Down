from PySide6.QtWidgets import QWidget,QFileDialog,QMessageBox
from PySide6.QtCore import Signal,Qt
from PySide6.QtGui import QCloseEvent
from fake_useragent import UserAgent
# 假设 Ui_Form 是从您的 .ui 文件通过 pyuic 生成的  
from generated_ui.Ui_settings import Ui_Settings  # 确保这里的路径是正确的  
import json
class SettingsWidget(QWidget):  
    def __init__(self, parent=None):  
        super(SettingsWidget, self).__init__(parent)  
        self.ui = Ui_Settings() 
        self.ui.setupUi(self)  
        self.get_configs_and_init()
        self.ui.select_btn.clicked.connect(self.set_down_folder)
        self.ui.proxies_ip.textChanged.connect(self.set_proxies_ip)    
        self.ui.proxies_port.textChanged.connect(self.set_proxies_port)    
        self.ui.cookies.textChanged.connect(self.set_cookies)
        self.ui.use_proxies_box.checkStateChanged.connect(self.set_use_proxies)

    configsChanged = Signal(dict)

    def closeEvent(self, event: QCloseEvent):  
        # 在这里添加关闭窗口前的处理逻辑  
        reply = QMessageBox.question(self, '确认退出',  
                                     "你确定要关闭设置窗口吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  
  
        if reply == QMessageBox.Yes:  
            # 执行一些清理操作或保存设置（如果需要）  
            self.set_configs()  
            # 然后允许窗口关闭  
            event.accept()  
        else:  
            event.ignore()  

    def get_configs_and_init(self):
        with open('config.json',mode='r',encoding='utf-8') as f:
            self.configs = json.load(f)
            self.ui.cookies.setText(self.configs['cookies'])
            self.ui.down_addr.setText(self.configs['down_addr'])
            self.ui.proxies_ip.setText(self.configs['proxies']['http']['ip'])
            self.ui.proxies_port.setText(self.configs['proxies']['http']['port'])
            #随机生成user_agent
        user_agent = UserAgent().random
        self.configs['user-agent'] = user_agent
        self.ui.use_proxies_box.setChecked(self.configs['use_proxies'])


    def set_down_folder(self):  
        folder = QFileDialog().getExistingDirectory(self, "选择文件夹")  
        if folder:  
            print(f"你选择的文件夹是: {folder}")
            self.configs['down_addr'] = folder
            self.ui.down_addr.setText(folder)

    def set_proxies_ip(self,ip):
        self.configs['proxies']['http']['ip'] = ip

    def set_proxies_port(self,port):
        self.configs['proxies']['http']['port'] = port

    def set_cookies(self,cookies):
        self.configs['cookies'] = cookies

    def set_use_proxies(self, state):
        def setenable(b):
            self.configs['use_proxies'] = b
            self.ui.proxies_ip.setEnabled(b)
            self.ui.proxies_port.setEnabled(b)

        if state == Qt.Checked:  
            setenable(True)
        elif state == Qt.Unchecked:  
            # 执行未选中时的操作  
            setenable(False)



    def set_configs(self):
        with open('config.json', mode='w', encoding='utf-8') as f:  
            json.dump(self.configs, f, ensure_ascii=False, indent=4) 
        self.configsChanged.emit(self.configs)