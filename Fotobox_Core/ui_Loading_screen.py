# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Loading_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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

class Ui_Loading_screen(object):
    def setupUi(self, Loading_screen):
        if not Loading_screen.objectName():
            Loading_screen.setObjectName(u"Loading_screen")
        Loading_screen.resize(400, 400)
        Loading_screen.setMinimumSize(QSize(400, 400))
        Loading_screen.setMaximumSize(QSize(400, 400))
        self.Loading_screen_gif = QLabel(Loading_screen)
        self.Loading_screen_gif.setObjectName(u"Loading_screen_gif")
        self.Loading_screen_gif.setGeometry(QRect(0, 0, 400, 400))
        self.Loading_screen_gif.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Loading_screen)

        QMetaObject.connectSlotsByName(Loading_screen)
    # setupUi

    def retranslateUi(self, Loading_screen):
        Loading_screen.setWindowTitle(QCoreApplication.translate("Loading_screen", u"Loading_screen", None))
        self.Loading_screen_gif.setText(QCoreApplication.translate("Loading_screen", u"TextLabel", None))
    # retranslateUi

