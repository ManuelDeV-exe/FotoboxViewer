# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import Resourcen_rc

class Ui_FotoboxViewer(object):
    def setupUi(self, FotoboxViewer):
        if not FotoboxViewer.objectName():
            FotoboxViewer.setObjectName(u"FotoboxViewer")
        FotoboxViewer.resize(1508, 963)
        FotoboxViewer.setStyleSheet(u"background-image: url(:/BG/data/BG_1.jpg);")
        self.verticalLayout_2 = QVBoxLayout(FotoboxViewer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.logo_links = QLabel(FotoboxViewer)
        self.logo_links.setObjectName(u"logo_links")
        self.logo_links.setPixmap(QPixmap(u":/Stock/data/Logo.png"))
        self.logo_links.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.logo_links)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.bild_Gross = QLabel(FotoboxViewer)
        self.bild_Gross.setObjectName(u"bild_Gross")
        self.bild_Gross.setEnabled(True)
        self.bild_Gross.setMinimumSize(QSize(780, 520))
        self.bild_Gross.setStyleSheet(u"")
        self.bild_Gross.setPixmap(QPixmap(u":/Stock/data/780x520.png"))
        self.bild_Gross.setScaledContents(False)
        self.bild_Gross.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.bild_Gross)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.logo_rechts = QLabel(FotoboxViewer)
        self.logo_rechts.setObjectName(u"logo_rechts")
        self.logo_rechts.setPixmap(QPixmap(u":/Stock/data/Logo.png"))
        self.logo_rechts.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.logo_rechts)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.bild_1 = QLabel(FotoboxViewer)
        self.bild_1.setObjectName(u"bild_1")
        self.bild_1.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.bild_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.bild_1)

        self.bild_2 = QLabel(FotoboxViewer)
        self.bild_2.setObjectName(u"bild_2")
        self.bild_2.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.bild_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.bild_2)

        self.bild_3 = QLabel(FotoboxViewer)
        self.bild_3.setObjectName(u"bild_3")
        self.bild_3.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.bild_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.bild_3)

        self.bild_4 = QLabel(FotoboxViewer)
        self.bild_4.setObjectName(u"bild_4")
        self.bild_4.setPixmap(QPixmap(u":/Stock/data/222x148.png"))
        self.bild_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.bild_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_8 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_7 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)


        self.retranslateUi(FotoboxViewer)

        QMetaObject.connectSlotsByName(FotoboxViewer)
    # setupUi

    def retranslateUi(self, FotoboxViewer):
        FotoboxViewer.setWindowTitle(QCoreApplication.translate("FotoboxViewer", u"FotoboxViewer", None))
        self.logo_links.setText("")
        self.bild_Gross.setText("")
        self.logo_rechts.setText("")
        self.bild_1.setText("")
        self.bild_2.setText("")
        self.bild_3.setText("")
        self.bild_4.setText("")
    # retranslateUi

