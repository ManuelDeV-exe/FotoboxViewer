# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)
import Resourcen_rc
import Resourcen_rc

class Ui_FotoboxViewer(object):
    def setupUi(self, FotoboxViewer):
        if not FotoboxViewer.objectName():
            FotoboxViewer.setObjectName(u"FotoboxViewer")
        FotoboxViewer.resize(1126, 872)
        FotoboxViewer.setStyleSheet(u"")
        self.bild_Gross = QLabel(FotoboxViewer)
        self.bild_Gross.setObjectName(u"bild_Gross")
        self.bild_Gross.setGeometry(QRect(50, 20, 780, 520))
        self.bild_Gross.setPixmap(QPixmap(u":/Stock/data/780x520.png"))
        self.bild_Gross.setAlignment(Qt.AlignCenter)
        self.bild_2 = QLabel(FotoboxViewer)
        self.bild_2.setObjectName(u"bild_2")
        self.bild_2.setGeometry(QRect(282, 574, 222, 148))
        self.bild_2.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.bild_8 = QLabel(FotoboxViewer)
        self.bild_8.setObjectName(u"bild_8")
        self.bild_8.setGeometry(QRect(738, 730, 222, 148))
        self.bild_8.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.bild_5 = QLabel(FotoboxViewer)
        self.bild_5.setObjectName(u"bild_5")
        self.bild_5.setGeometry(QRect(54, 730, 222, 148))
        self.bild_5.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.bild_1 = QLabel(FotoboxViewer)
        self.bild_1.setObjectName(u"bild_1")
        self.bild_1.setGeometry(QRect(54, 574, 222, 148))
        self.bild_1.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.bild_6 = QLabel(FotoboxViewer)
        self.bild_6.setObjectName(u"bild_6")
        self.bild_6.setGeometry(QRect(282, 730, 222, 148))
        self.bild_6.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.bild_4 = QLabel(FotoboxViewer)
        self.bild_4.setObjectName(u"bild_4")
        self.bild_4.setGeometry(QRect(738, 574, 222, 148))
        self.bild_4.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.bild_3 = QLabel(FotoboxViewer)
        self.bild_3.setObjectName(u"bild_3")
        self.bild_3.setGeometry(QRect(510, 574, 222, 148))
        self.bild_3.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.bild_7 = QLabel(FotoboxViewer)
        self.bild_7.setObjectName(u"bild_7")
        self.bild_7.setGeometry(QRect(510, 730, 222, 148))
        self.bild_7.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.hintergrund = QFrame(FotoboxViewer)
        self.hintergrund.setObjectName(u"hintergrund")
        self.hintergrund.setGeometry(QRect(900, 405, 120, 80))
        self.hintergrund.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.hintergrund.setFrameShape(QFrame.StyledPanel)
        self.hintergrund.setFrameShadow(QFrame.Raised)
        self.hintergrund.raise_()
        self.bild_Gross.raise_()
        self.bild_2.raise_()
        self.bild_8.raise_()
        self.bild_5.raise_()
        self.bild_1.raise_()
        self.bild_6.raise_()
        self.bild_4.raise_()
        self.bild_3.raise_()
        self.bild_7.raise_()

        self.retranslateUi(FotoboxViewer)

        QMetaObject.connectSlotsByName(FotoboxViewer)
    # setupUi

    def retranslateUi(self, FotoboxViewer):
        FotoboxViewer.setWindowTitle(QCoreApplication.translate("FotoboxViewer", u"Frame", None))
        self.bild_Gross.setText("")
        self.bild_2.setText("")
        self.bild_8.setText("")
        self.bild_5.setText("")
        self.bild_1.setText("")
        self.bild_6.setText("")
        self.bild_4.setText("")
        self.bild_3.setText("")
        self.bild_7.setText("")
    # retranslateUi

