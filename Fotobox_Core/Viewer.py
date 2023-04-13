import sys, os
import reg_config

myimages_schlüssel =('big_1', 'little_1', 'little_2', 'little_3', 'little_4')
mypaths_schlüssel =('upload_folder', 'kamera_folder', 'viewer_path', 'upload_path', 'full_size_folder')
mysettings_schlüssel =('upload', 'prozent_grosses_bild', 'prozent_kleines_bild', 'prozent_werbung', 'background_img', 'compressed_width')

MyImages = reg_config.My_Config('Images', myimages_schlüssel)
MyPaths = reg_config.My_Config('Paths', mypaths_schlüssel)
MySettings = reg_config.My_Config('Settings', mysettings_schlüssel)

from PySide6.QtGui import *
from PySide6.QtWidgets import *
import PySide6.QtCore as QtCore

monitor_size_width, monitor_size_heigth = 1920, 1080
logo_Pfad = os.path.abspath('../data/icon.png')

prozent_werbung = float(MySettings.config['prozent_werbung'])
prozent_grosses_bild = float(MySettings.config['prozent_grosses_bild'])
prozent_kleines_bild = float(MySettings.config['prozent_kleines_bild'])

from ui_Window import Ui_FotoboxViewer

class MainWindow(QFrame):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_FotoboxViewer()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(logo_Pfad))

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint , True)

        self.setGeometry(0, 0, monitor_size_width, monitor_size_heigth)
        pixmap_logo_links = QPixmap("data/logo_links.png")
        pixmap_logo_links = pixmap_logo_links.scaledToWidth(monitor_size_width*prozent_werbung, mode=QtCore.Qt.TransformationMode.SmoothTransformation)
        self.ui.logo_links.setPixmap(pixmap_logo_links)
        self.ui.logo_links.mousePressEvent = self.kill

        pixmap_logo_rechts = QPixmap("data/logo_rechts.png")
        pixmap_logo_rechts = pixmap_logo_rechts.scaledToWidth(monitor_size_width*prozent_werbung, mode=QtCore.Qt.TransformationMode.SmoothTransformation)
        self.ui.logo_rechts.setPixmap(pixmap_logo_rechts)

        bg = int(MySettings.config['background_img'])-1
        self.setStyleSheet(f'background-image: url(:/BG/data/BG_{bg}.jpg);')

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.setTime())
        self.timer.start(1000)

        pixmap = QPixmap(r'data/780x520.png')
        pixmap = pixmap.scaledToHeight(int(monitor_size_heigth * prozent_grosses_bild), mode=QtCore.Qt.TransformationMode.SmoothTransformation)
        self.ui.bild_Gross.setPixmap(pixmap)

        pixmap = QPixmap(r'data/222x148.png')
        pixmap = pixmap.scaledToHeight(int(monitor_size_heigth * prozent_kleines_bild), mode=QtCore.Qt.TransformationMode.SmoothTransformation)
        self.ui.bild_1.setPixmap(pixmap)

        pixmap = QPixmap(r'data/222x148.png')
        pixmap = pixmap.scaledToHeight(int(monitor_size_heigth * prozent_kleines_bild), mode=QtCore.Qt.TransformationMode.SmoothTransformation)
        self.ui.bild_2.setPixmap(pixmap)

        pixmap = QPixmap(r'data/222x148.png')
        pixmap = pixmap.scaledToHeight(int(monitor_size_heigth * prozent_kleines_bild), mode=QtCore.Qt.TransformationMode.SmoothTransformation)
        self.ui.bild_3.setPixmap(pixmap)

        pixmap = QPixmap(r'data/222x148.png')
        pixmap = pixmap.scaledToHeight(int(monitor_size_heigth * prozent_kleines_bild), mode=QtCore.Qt.TransformationMode.SmoothTransformation)
        self.ui.bild_4.setPixmap(pixmap)

        self.showMaximized()

    def setTime(self):
        pixmap = QPixmap(MyImages.config['big_1'])

        pixmap = pixmap.scaledToHeight(int(monitor_size_width * prozent_grosses_bild), mode=QtCore.Qt.TransformationMode.SmoothTransformation)
        
        # Löschen Sie die alte QPixmap-Instanz, um den Cache freizugeben
        old_pixmap = MainWindow.ui.bild_Gross.pixmap()
        if old_pixmap is not None:
            del old_pixmap
        MainWindow.ui.bild_Gross.setPixmap(pixmap)    

        liste = [MainWindow.ui.bild_1, MainWindow.ui.bild_2, MainWindow.ui.bild_3, MainWindow.ui.bild_4]
        for i in range(4):
            try:
                mypixmap = QPixmap(MyImages.config[f'little_{i+1}'])
                mypixmap = mypixmap.scaledToHeight(int(monitor_size_width * prozent_kleines_bild), mode=QtCore.Qt.TransformationMode.SmoothTransformation)
                # Löschen Sie die alte QPixmap-Instanz, um den Cache freizugeben
                old_pixmap = liste[i].pixmap()
                if old_pixmap is not None:
                    del old_pixmap
                liste[i].setPixmap(mypixmap)     
            except Exception as ex: print(ex)
        
    def kill(self, event):
        self.close()
    
if __name__ == '__main__':

    app = QApplication(sys.argv)

    MainWindow = MainWindow()

    sys.exit(app.exec())