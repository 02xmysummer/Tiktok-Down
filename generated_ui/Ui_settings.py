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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Settingvs(object):
    def setupUi(self, Settingvs):
        if not Settingvs.objectName():
            Settingvs.setObjectName(u"Settingvs")
        Settingvs.resize(623, 405)
        self.verticalLayout = QVBoxLayout(Settingvs)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Settingvs)
        self.widget.setObjectName(u"widget")
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


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Settingvs)
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


        self.retranslateUi(Settingvs)

        QMetaObject.connectSlotsByName(Settingvs)
    # setupUi

    def retranslateUi(self, Settingvs):
        Settingvs.setWindowTitle(QCoreApplication.translate("Settingvs", u"Form", None))
        self.label.setText(QCoreApplication.translate("Settingvs", u"\u4e0b\u8f7d\u5730\u5740", None))
        self.select_btn.setText(QCoreApplication.translate("Settingvs", u"\u9009\u62e9", None))
        self.label_2.setText(QCoreApplication.translate("Settingvs", u"Cookies\u5730\u5740", None))
    # retranslateUi

