# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Core.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QWidget)
import Resourcen_rc

class Ui_Core(object):
    def setupUi(self, Core):
        if not Core.objectName():
            Core.setObjectName(u"Core")
        Core.resize(560, 340)
        Core.setMinimumSize(QSize(560, 340))
        Core.setMaximumSize(QSize(560, 340))
        icon = QIcon()
        icon.addFile(u":/Stock/data/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Core.setWindowIcon(icon)
        self.centralwidget = QWidget(Core)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(15, 10, 386, 16))
        self.path_kamera_folder = QLineEdit(self.centralwidget)
        self.path_kamera_folder.setObjectName(u"path_kamera_folder")
        self.path_kamera_folder.setGeometry(QRect(15, 30, 526, 22))
        self.Upload_Radio = QRadioButton(self.centralwidget)
        self.Upload_Radio.setObjectName(u"Upload_Radio")
        self.Upload_Radio.setGeometry(QRect(405, 5, 89, 20))
        self.save_BTN = QPushButton(self.centralwidget)
        self.save_BTN.setObjectName(u"save_BTN")
        self.save_BTN.setGeometry(QRect(380, 290, 75, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(15, 55, 386, 16))
        self.upload_folder = QLineEdit(self.centralwidget)
        self.upload_folder.setObjectName(u"upload_folder")
        self.upload_folder.setGeometry(QRect(15, 75, 526, 22))
        self.prozent_kleines_bild = QLineEdit(self.centralwidget)
        self.prozent_kleines_bild.setObjectName(u"prozent_kleines_bild")
        self.prozent_kleines_bild.setGeometry(QRect(120, 260, 106, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 235, 116, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 235, 116, 16))
        self.prozent_grosses_bild = QLineEdit(self.centralwidget)
        self.prozent_grosses_bild.setObjectName(u"prozent_grosses_bild")
        self.prozent_grosses_bild.setGeometry(QRect(230, 260, 106, 22))
        self.background = QSpinBox(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(355, 260, 60, 22))
        self.background.setMinimum(1)
        self.background.setMaximum(7)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 235, 81, 16))
        self.start_viewer_BTN = QPushButton(self.centralwidget)
        self.start_viewer_BTN.setObjectName(u"start_viewer_BTN")
        self.start_viewer_BTN.setGeometry(QRect(455, 290, 101, 24))
        self.viewer_path = QLineEdit(self.centralwidget)
        self.viewer_path.setObjectName(u"viewer_path")
        self.viewer_path.setGeometry(QRect(15, 120, 526, 22))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(15, 100, 386, 16))
        self.upload_path = QLineEdit(self.centralwidget)
        self.upload_path.setObjectName(u"upload_path")
        self.upload_path.setGeometry(QRect(15, 210, 526, 22))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(15, 190, 386, 16))
        self.Upload_folder_name = QLineEdit(self.centralwidget)
        self.Upload_folder_name.setObjectName(u"Upload_folder_name")
        self.Upload_folder_name.setGeometry(QRect(95, 290, 176, 22))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 295, 101, 16))
        self.full_size_folder = QLineEdit(self.centralwidget)
        self.full_size_folder.setObjectName(u"full_size_folder")
        self.full_size_folder.setGeometry(QRect(15, 165, 526, 22))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(15, 145, 386, 16))
        self.compressed_width = QLineEdit(self.centralwidget)
        self.compressed_width.setObjectName(u"compressed_width")
        self.compressed_width.setGeometry(QRect(430, 260, 106, 22))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(430, 235, 116, 16))
        self.start_BTN = QPushButton(self.centralwidget)
        self.start_BTN.setObjectName(u"start_BTN")
        self.start_BTN.setGeometry(QRect(280, 290, 46, 24))
        self.stop_BTN = QPushButton(self.centralwidget)
        self.stop_BTN.setObjectName(u"stop_BTN")
        self.stop_BTN.setGeometry(QRect(330, 290, 46, 24))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(100, 320, 400, 16))
        self.label_12.setAlignment(Qt.AlignCenter)
        self.prozent_werbung = QLineEdit(self.centralwidget)
        self.prozent_werbung.setObjectName(u"prozent_werbung")
        self.prozent_werbung.setGeometry(QRect(10, 260, 106, 22))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 235, 116, 16))
        Core.setCentralWidget(self.centralwidget)

        self.retranslateUi(Core)

        QMetaObject.connectSlotsByName(Core)
    # setupUi

    def retranslateUi(self, Core):
        Core.setWindowTitle(QCoreApplication.translate("Core", u"Core", None))
        self.label.setText(QCoreApplication.translate("Core", u"Kamera Import Ordner", None))
        self.Upload_Radio.setText(QCoreApplication.translate("Core", u"Upload?", None))
        self.save_BTN.setText(QCoreApplication.translate("Core", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("Core", u"Upload Ornder", None))
        self.label_4.setText(QCoreApplication.translate("Core", u"prozent_kleines_bild", None))
        self.label_5.setText(QCoreApplication.translate("Core", u"prozent_grosses_bild", None))
        self.label_6.setText(QCoreApplication.translate("Core", u"Hintergrund?", None))
        self.start_viewer_BTN.setText(QCoreApplication.translate("Core", u"start Viewer", None))
        self.label_7.setText(QCoreApplication.translate("Core", u"viewer.exe", None))
        self.label_8.setText(QCoreApplication.translate("Core", u"FTP-Upload.exe", None))
        self.label_9.setText(QCoreApplication.translate("Core", u"Upload Ordner", None))
        self.label_10.setText(QCoreApplication.translate("Core", u"Original Qualit\u00e4t Ordner", None))
        self.label_11.setText(QCoreApplication.translate("Core", u"Comprimieren Breite", None))
        self.start_BTN.setText(QCoreApplication.translate("Core", u"Start", None))
        self.stop_BTN.setText(QCoreApplication.translate("Core", u"Stop", None))
        self.label_12.setText(QCoreApplication.translate("Core", u"V1.5.0 - (c) 2024 B\u00fccherl Manuel", None))
        self.label_13.setText(QCoreApplication.translate("Core", u"Werbung-%", None))
    # retranslateUi

