from PySide6.QtWidgets import QWidget  
 
from PySide6.QtWidgets import QCheckBox,QListWidgetItem
# 假设 Ui_Form 是从您的 .ui 文件通过 pyuic 生成的  
from generated_ui.Ui_download import Ui_Form  # 确保这里的路径是正确的  
  
class DownloadWidget(QWidget):  
    def __init__(self, parent=None):  
        super(DownloadWidget, self).__init__(parent)  
        self.ui = Ui_Form()  
        self.ui.setupUi(self)  
          
        # 初始化额外的属性  
        self.chooses = []  # 这通常不应该在 Ui_Form 中  
        # 注意：vedio_addrs 和 user_url 应该在需要时通过方法设置，而不是作为实例变量  
  
        # 连接信号和槽（如果有的话）  
        # 例如：self.ui.someButton.clicked.connect(self.some_method)  
  
    # 添加您的方法  
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
  
    # 其他方法...  
  
# 使用 DownloadForm 类  
# 例如，在您的主窗口中：  
# self.download_form = DownloadForm()  
# self.tabWidget.addTab(self.download_form, "Download")