import sys, os
import reg_config
import time

myimages_schlüssel =('big_1', 'little_1', 'little_2', 'little_3', 'little_4')
mypaths_schlüssel =('upload_folder', 'kamera_folder', 'viewer_path', 'upload_path', 'full_size_folder')
mysettings_schlüssel =('upload', 'prozent_grosses_bild', 'prozent_kleines_bild', 'prozent_werbung', 'background_img', 'compressed_width')

MyImages = reg_config.My_Config('Images', myimages_schlüssel)
MyPaths = reg_config.My_Config('Paths', mypaths_schlüssel)
MySettings = reg_config.My_Config('Settings', mysettings_schlüssel)

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6.QtWebEngineCore
from PySide6.QtWebEngineWidgets import *

monitor_size_width, monitor_size_heigth = 1920, 1080
logo_Pfad = os.path.abspath('data/icon.png')

hintergrundliste = ['data/BG_0.jpg','data/BG_1.jpg','data/BG_2.jpg','data/BG_3.jpg','data/BG_4.jpg','data/BG_5.jpg','data/BG_6.jpg']

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QIcon(str(logo_Pfad)))
        
        self.browser = QWebEngineView()
        self.loadPage()

        self.setContentsMargins(0,0,0,0)
        self.setWindowFlag(Qt.FramelessWindowHint , True)
        self.setCentralWidget(self.browser)

        close_btn = QPushButton('', self)
        close_btn.setStyleSheet("background-color: rgba(0,0,0,0);")
        close_btn.setStyleSheet("background-color: rgba(0,0,0,0);")
        close_btn.setGeometry(0, 0, 500, 3000)
        close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        close_btn.clicked.connect(self.close)
        
        self.showMaximized()

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.reloadPage())
        self.timer.start(500)

    def loadPage(self):
        with open('index.html', 'r') as f:
            html = f.read()
            f.close()

        prozent_werbung = float(MySettings.config['prozent_werbung'])
        prozent_grosses_bild = float(MySettings.config['prozent_grosses_bild'])
        prozent_kleines_bild = float(MySettings.config['prozent_kleines_bild'])

        html = html.replace('##logo_breite##', f'{prozent_werbung}%')
        html = html.replace('##breite##', f'{monitor_size_width*prozent_werbung}px')
        html = html.replace('##big_img_width##', f'{prozent_grosses_bild}%')
        html = html.replace('##breite_small##', f'{prozent_kleines_bild}%')

        html = html.replace('##werbung_links##', 'data/logo_links.png')
        html = html.replace('##werbung_rechts##', 'data/logo_rechts.png')
        html = html.replace('##big##', MyImages.config['big_1'])

        bg = hintergrundliste[int(MySettings.config['background_img'])]
        html = html.replace('##hintergrund_img##', bg)

        html = html.replace('##img_1##', MyImages.config['little_1'])
        html = html.replace('##img_2##', MyImages.config['little_2'])
        html = html.replace('##img_3##', MyImages.config['little_3'])
        html = html.replace('##img_4##', MyImages.config['little_4'])

        
        self.browser.setHtml(html, QUrl('file://'))

    def reloadPage(self):
        old_path = []
        old_path.append(MyImages.config['big_1'])
        old_path.append(MyImages.config['little_1'])
        old_path.append(MyImages.config['little_2'])
        old_path.append(MyImages.config['little_3'])
        old_path.append(MyImages.config['little_4'])

        MySettings.read_new()
        MyImages.read_new()

        new_path = []
        new_path.append(MyImages.config['big_1'])
        new_path.append(MyImages.config['little_1'])
        new_path.append(MyImages.config['little_2'])
        new_path.append(MyImages.config['little_3'])
        new_path.append(MyImages.config['little_4'])

        for index, new in enumerate(new_path):
            if new != old_path[index] :
                self.loadPage()

if __name__ == '__main__':

    sys.argv.append("--disable-web-security")
    app = QApplication(sys.argv)

    MainWindow = MainWindow()

    sys.exit(app.exec())