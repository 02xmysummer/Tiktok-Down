from PySide6.QtWidgets import QWidget  
 
from PySide6.QtWidgets import QFileDialog
# 假设 Ui_Form 是从您的 .ui 文件通过 pyuic 生成的  
from generated_ui.Ui_settings import Ui_Settingvs  # 确保这里的路径是正确的  
import json
class SettingsWidget(QWidget):  
    def __init__(self, parent=None):  
        super(SettingsWidget, self).__init__(parent)  
        self.ui = Ui_Settingvs() 
        self.ui.setupUi(self)  
        self.get_configs_and_init()
        self.filedialog = QFileDialog()
        self.ui.select_btn.clicked.connect(self.select_folder)

    def get_configs_and_init(self):
        with open('config.json',mode='r',encoding='utf-8') as f:
            self.configs = json.load(f)
            self.ui.cookies.setText(self.configs['cookies'])
            self.ui.down_addr.setText(self.configs['down_addr'])

    def select_folder(self):  
        # 使用QFileDialog.getExistingDirectory来打开文件夹选择对话框  
        folder = self.filedialog.getExistingDirectory(self, "选择文件夹")  
        if folder:  
            print(f"你选择的文件夹是: {folder}")
            self.configs['down_addr'] = folder
            with open('config.json', mode='w', encoding='utf-8') as f:  
                json.dump(self.configs, f, ensure_ascii=False, indent=4)
            self.ui.down_addr.setText(folder)
              