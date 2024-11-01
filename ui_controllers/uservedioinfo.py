from PySide6.QtCore import Qt  
 
from PySide6.QtWidgets import QCheckBox,QListWidgetItem,QWidget
# 假设 Ui_Form 是从您的 .ui 文件通过 pyuic 生成的  
from generated_ui.Ui_uservedioinfo import Ui_Form  # 确保这里的路径是正确的  
  
class UserVedioInfo(QWidget):  
    def __init__(self, parent=None):  
        super(UserVedioInfo, self).__init__(parent)  
        self.ui = Ui_Form()  
        self.ui.setupUi(self)  
          
        self.ui.select_all.clicked.connect(self.select_all)

   
    def add_down_list(self, titles, video_addrs, user_url):  
        self.ui.vedio_addrs = video_addrs  # 注意：这里我们直接访问了 ui 的属性，但这通常不是好的做法  
        self.ui.user_url = user_url  
        self.ui.titles = titles
        for title in titles:  
            box = QCheckBox(text=title)  
            item = QListWidgetItem()  
            self.ui.listWidget.addItem(item)  
            self.ui.listWidget.setItemWidget(item, box)  
  
    def set_title(self, name):  
        self.ui.title_label.setText(name + '的视频列表')  
  

    def select_all(self):
        listWidget = self.ui.listWidget
        count = listWidget.count()
        for index in range(count):  
            item = listWidget.item(index)  
            checkbox = listWidget.itemWidget(item)  
            if isinstance(checkbox, QCheckBox):  
                checkbox.setCheckState(Qt.Checked)  
        
