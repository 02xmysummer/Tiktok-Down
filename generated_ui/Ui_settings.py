# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(623, 405)
        icon = QIcon()
        icon.addFile(u"../icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Settings.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Settings)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 0))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.down_addr = QLineEdit(self.widget)
        self.down_addr.setObjectName(u"down_addr")

        self.horizontalLayout.addWidget(self.down_addr)

        self.select_btn = QPushButton(self.widget)
        self.select_btn.setObjectName(u"select_btn")

        self.horizontalLayout.addWidget(self.select_btn)

        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Settings)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cookies = QLineEdit(self.widget_2)
        self.cookies.setObjectName(u"cookies")

        self.horizontalLayout_2.addWidget(self.cookies)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(Settings)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.use_proxies_box = QCheckBox(self.widget_3)
        self.use_proxies_box.setObjectName(u"use_proxies_box")

        self.horizontalLayout_3.addWidget(self.use_proxies_box)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.proxies_ip = QLineEdit(self.widget_3)
        self.proxies_ip.setObjectName(u"proxies_ip")

        self.horizontalLayout_3.addWidget(self.proxies_ip)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.proxies_port = QLineEdit(self.widget_3)
        self.proxies_port.setObjectName(u"proxies_port")

        self.horizontalLayout_3.addWidget(self.proxies_port)


        self.verticalLayout.addWidget(self.widget_3)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Form", None))
        self.label.setText(QCoreApplication.translate("Settings", u"\u4e0b\u8f7d\u5730\u5740", None))
        self.select_btn.setText(QCoreApplication.translate("Settings", u"\u9009\u62e9", None))
        self.checkBox.setText(QCoreApplication.translate("Settings", u"2", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Cookies\u5730\u5740", None))
        self.label_3.setText("")
        self.use_proxies_box.setText(QCoreApplication.translate("Settings", u"\u4ee3\u7406", None))
        self.label_4.setText(QCoreApplication.translate("Settings", u"\u4ee3\u7406\u5730\u5740", None))
        self.label_5.setText(QCoreApplication.translate("Settings", u"\uff1a", None))
    # retranslateUi

