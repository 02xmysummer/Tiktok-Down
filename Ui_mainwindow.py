# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.home_tab = QWidget()
        self.home_tab.setObjectName(u"home_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.home_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.home_tab)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.url_edit = QLineEdit(self.widget)
        self.url_edit.setObjectName(u"url_edit")

        self.horizontalLayout.addWidget(self.url_edit)

        self.find_btn = QPushButton(self.widget)
        self.find_btn.setObjectName(u"find_btn")

        self.horizontalLayout.addWidget(self.find_btn)

        self.next_btn = QPushButton(self.widget)
        self.next_btn.setObjectName(u"next_btn")

        self.horizontalLayout.addWidget(self.next_btn)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.horizontalLayout_2.addWidget(self.widget)

        self.tabWidget.addTab(self.home_tab, "")
        self.down_tab = QWidget()
        self.down_tab.setObjectName(u"down_tab")
        self.verticalLayout_2 = QVBoxLayout(self.down_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.down_tab)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.down_tab)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_2.addWidget(self.widget_3)

        self.tabWidget.addTab(self.down_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tiktok Down", None))
#if QT_CONFIG(tooltip)
        self.home_tab.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.find_btn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u627e", None))
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6211\u7684\u6536\u85cf\u5939", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u603b\u8ba1\uff1a0/\u4e0b\u8f7d\u4e2d\uff1a0\u6682\u505c\uff1a0\u4e0b\u8f7d\u5b8c\uff1a0\u961f\u5217\u4e2d\uff1a0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u7ee7\u7eed", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u6682\u505c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u5220\u9664", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5df2\u5b8c\u6210", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.down_tab), QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u9875", None))
    # retranslateUi

