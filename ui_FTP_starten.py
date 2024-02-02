# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FTP_starten.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import Resourcen_rc

class Ui_FTP_starten(object):
    def setupUi(self, FTP_starten):
        if not FTP_starten.objectName():
            FTP_starten.setObjectName(u"FTP_starten")
        FTP_starten.resize(200, 60)
        FTP_starten.setMinimumSize(QSize(200, 60))
        FTP_starten.setMaximumSize(QSize(200, 60))
        icon = QIcon()
        icon.addFile(u":/Stock/data/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        FTP_starten.setWindowIcon(icon)
        self.centralwidget = QWidget(FTP_starten)
        self.centralwidget.setObjectName(u"centralwidget")
        self.start_BTN = QPushButton(self.centralwidget)
        self.start_BTN.setObjectName(u"start_BTN")
        self.start_BTN.setGeometry(QRect(45, 30, 46, 24))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(65, 10, 81, 16))
        self.stop_BTN = QPushButton(self.centralwidget)
        self.stop_BTN.setObjectName(u"stop_BTN")
        self.stop_BTN.setGeometry(QRect(100, 30, 46, 24))
        FTP_starten.setCentralWidget(self.centralwidget)

        self.retranslateUi(FTP_starten)

        QMetaObject.connectSlotsByName(FTP_starten)
    # setupUi

    def retranslateUi(self, FTP_starten):
        FTP_starten.setWindowTitle(QCoreApplication.translate("FTP_starten", u"FTP_starten", None))
        self.start_BTN.setText(QCoreApplication.translate("FTP_starten", u"Start", None))
        self.label_6.setText(QCoreApplication.translate("FTP_starten", u"FTP_Starten", None))
        self.stop_BTN.setText(QCoreApplication.translate("FTP_starten", u"Stop", None))
    # retranslateUi

