# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'downinfo.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_DownInfo(object):
    def setupUi(self, DownInfo):
        if not DownInfo.objectName():
            DownInfo.setObjectName(u"DownInfo")
        DownInfo.resize(795, 480)
        self.verticalLayout = QVBoxLayout(DownInfo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(DownInfo)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.total_down = QLabel(self.widget_2)
        self.total_down.setObjectName(u"total_down")
        self.total_down.setEnabled(False)
        self.total_down.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.total_down)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(False)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.downloading = QLabel(self.widget_2)
        self.downloading.setObjectName(u"downloading")
        self.downloading.setEnabled(False)
        self.downloading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.downloading)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.down_pasue = QLabel(self.widget_2)
        self.down_pasue.setObjectName(u"down_pasue")
        self.down_pasue.setEnabled(False)
        self.down_pasue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.down_pasue)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(False)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.down_finish = QLabel(self.widget_2)
        self.down_finish.setObjectName(u"down_finish")
        self.down_finish.setEnabled(False)
        self.down_finish.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.down_finish)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(False)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.down_queue = QLabel(self.widget_2)
        self.down_queue.setObjectName(u"down_queue")
        self.down_queue.setEnabled(False)
        self.down_queue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.down_queue)

        self.all_continue = QPushButton(self.widget_2)
        self.all_continue.setObjectName(u"all_continue")

        self.horizontalLayout_3.addWidget(self.all_continue)

        self.all_stop_btn = QPushButton(self.widget_2)
        self.all_stop_btn.setObjectName(u"all_stop_btn")

        self.horizontalLayout_3.addWidget(self.all_stop_btn)

        self.all_del_btn = QPushButton(self.widget_2)
        self.all_del_btn.setObjectName(u"all_del_btn")

        self.horizontalLayout_3.addWidget(self.all_del_btn)

        self.del_finish_btn = QPushButton(self.widget_2)
        self.del_finish_btn.setObjectName(u"del_finish_btn")

        self.horizontalLayout_3.addWidget(self.del_finish_btn)


        self.verticalLayout.addWidget(self.widget_2)

        self.listWidget = QListWidget(DownInfo)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.retranslateUi(DownInfo)

        QMetaObject.connectSlotsByName(DownInfo)
    # setupUi

    def retranslateUi(self, DownInfo):
        DownInfo.setWindowTitle(QCoreApplication.translate("DownInfo", u"Form", None))
        self.label.setText(QCoreApplication.translate("DownInfo", u"\u603b\u8ba1\uff1a", None))
        self.total_down.setText(QCoreApplication.translate("DownInfo", u"0", None))
        self.label_3.setText(QCoreApplication.translate("DownInfo", u"\u4e0b\u8f7d\u4e2d\uff1a", None))
        self.downloading.setText(QCoreApplication.translate("DownInfo", u"0", None))
        self.label_5.setText(QCoreApplication.translate("DownInfo", u"\u6682\u505c\uff1a", None))
        self.down_pasue.setText(QCoreApplication.translate("DownInfo", u"0", None))
        self.label_7.setText(QCoreApplication.translate("DownInfo", u"\u4e0b\u8f7d\u5b8c\uff1a", None))
        self.down_finish.setText(QCoreApplication.translate("DownInfo", u"0", None))
        self.label_9.setText(QCoreApplication.translate("DownInfo", u"\u961f\u5217\u4e2d\uff1a", None))
        self.down_queue.setText(QCoreApplication.translate("DownInfo", u"0", None))
        self.all_continue.setText(QCoreApplication.translate("DownInfo", u"\u5168\u90e8\u7ee7\u7eed", None))
        self.all_stop_btn.setText(QCoreApplication.translate("DownInfo", u"\u5168\u90e8\u6682\u505c", None))
        self.all_del_btn.setText(QCoreApplication.translate("DownInfo", u"\u5168\u90e8\u5220\u9664", None))
        self.del_finish_btn.setText(QCoreApplication.translate("DownInfo", u"\u5220\u9664\u5df2\u5b8c\u6210", None))
    # retranslateUi

