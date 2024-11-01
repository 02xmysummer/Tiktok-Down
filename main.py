from PySide6.QtWidgets import QApplication, QMainWindow
from ui_controllers.mainwindow import QMainWindow
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    
    sys.exit(app.exec())
