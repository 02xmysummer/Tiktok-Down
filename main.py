import sys
from PySide6.QtWidgets import QApplication, QMainWindow
sys.path.append("ui\\uic")
from Ui_mainwindow import Ui_MainWindow
from index import get_media_url
class QMainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.find_btn.clicked.connect(lambda : get_media_url(self.ui.url_edit.text()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    
    sys.exit(app.exec())
