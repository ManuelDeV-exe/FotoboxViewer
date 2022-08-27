import sys, os
import PyQt6, PySide6
import pathlib
from screeninfo import get_monitors
import PySide6.QtCore as QtCore
import threading
import keyboard
import signal

import configobj
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PIL import Image

logo_Pfad = str(pathlib.Path('data\\icon.png').absolute())
global windowIcon # Define Var vor icon

prozent_grosses_bild = 0.45
prozent_kleines_bild = 0.17

for m in get_monitors():
    monitor_info = {}
    monitor_info['x'] = m.x
    monitor_info['y'] = m.y
    monitor_info['width'] = m.width
    monitor_info['heigth'] = m.width

from ui_Window import Ui_FotoboxViewer

class MainWindow(QFrame):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_FotoboxViewer()
        self.ui.setupUi(self)
        # self.setWindowIcon(windowIcon)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint , True)

        self.setGeometry(monitor_info['x'], monitor_info['y'], monitor_info['width'], monitor_info['heigth'])
        self.showMaximized()

        self.ui.hintergrund.setGeometry(monitor_info['x'], monitor_info['y'], monitor_info['width'], monitor_info['heigth'])

        last_image_names = get_files_in_folder()
        aktueller_pfad = bilder_speicherplatz + "\\" + last_image_names[len(last_image_names)-1]
        im = Image.open(aktueller_pfad)
        img_width, img_height = im.size
    
        self.ui.bild_Gross.setGeometry(monitor_info['width']/2-monitor_info['width']/2, monitor_info['heigth']*0.008, monitor_info['width'], img_height * (monitor_info['width']*prozent_grosses_bild/img_width))

        self.ui.bild_1.setGeometry(monitor_info['width']/6*0.7, monitor_info['heigth']*0.222, img_width * prozent_kleines_bild, img_height * prozent_kleines_bild)
        self.ui.bild_2.setGeometry(monitor_info['width']/6*1.9, monitor_info['heigth']*0.222, img_width * prozent_kleines_bild, img_height * prozent_kleines_bild)
        self.ui.bild_3.setGeometry(monitor_info['width']/6*3.1, monitor_info['heigth']*0.222, img_width * prozent_kleines_bild, img_height * prozent_kleines_bild)
        self.ui.bild_4.setGeometry(monitor_info['width']/6*4.3, monitor_info['heigth']*0.222, img_width * prozent_kleines_bild, img_height * prozent_kleines_bild)
       
        self.ui.bild_5.setGeometry(monitor_info['width']/6*0.7, monitor_info['heigth']*0.35, img_width * prozent_kleines_bild, img_height * prozent_kleines_bild)
        self.ui.bild_6.setGeometry(monitor_info['width']/6*1.9, monitor_info['heigth']*0.35, img_width * prozent_kleines_bild, img_height * prozent_kleines_bild)
        self.ui.bild_7.setGeometry(monitor_info['width']/6*3.1, monitor_info['heigth']*0.35, img_width * prozent_kleines_bild, img_height * prozent_kleines_bild)
        self.ui.bild_8.setGeometry(monitor_info['width']/6*4.3, monitor_info['heigth']*0.35, img_width * prozent_kleines_bild, img_height * prozent_kleines_bild)


def aktuallisiere_bilder():
    while True:
        last_image_names = []
        last_image_names = get_files_in_folder()
        change_big_images(last_image_names)
        change_little_iamges(last_image_names)
    
def keywatcher():
    while True:
        if keyboard.is_pressed('q'):
            print('kill all')
            PID = os.getpid()
            os.kill(PID, signal.SIGTERM)

def change_big_images(last_image_names):
    aktueller_pfad = bilder_speicherplatz + "\\" + last_image_names[len(last_image_names)-1]
    im = Image.open(aktueller_pfad)
    img_width, img_height = im.size
    pixmap = QPixmap(aktueller_pfad)
    pixmap = pixmap.scaled(monitor_info['width']*prozent_grosses_bild, img_height * (monitor_info['width']*prozent_grosses_bild/img_width))
    MainWindow.ui.bild_Gross.setPixmap(pixmap)

def change_little_iamges(last_image_names):
    for i in range(len(last_image_names)-2):
        aktueller_pfad = bilder_speicherplatz + "\\" + last_image_names[len(last_image_names)-1-i]
        im = Image.open(aktueller_pfad)
        img_width, img_height = im.size
        pixmap = QPixmap(aktueller_pfad)
        pixmap = pixmap.scaled(monitor_info['width']*prozent_kleines_bild, img_height * (monitor_info['width']*prozent_kleines_bild/img_width))
        if i == 1 : MainWindow.ui.bild_1.setPixmap(pixmap)
        if i == 2 : MainWindow.ui.bild_2.setPixmap(pixmap)
        if i == 3 : MainWindow.ui.bild_3.setPixmap(pixmap)
        if i == 4 : MainWindow.ui.bild_4.setPixmap(pixmap)
        if i == 5 : MainWindow.ui.bild_5.setPixmap(pixmap)
        if i == 6 : MainWindow.ui.bild_6.setPixmap(pixmap)
        if i == 7 : MainWindow.ui.bild_7.setPixmap(pixmap)
        if i == 8 : MainWindow.ui.bild_8.setPixmap(pixmap)

def get_files_in_folder():
    pfad = []
    for images in os.listdir(bilder_speicherplatz):
        # check if the image ends with png
        if (images.endswith(".JPG")):
            pfad.append(images)
    return pfad
            
def read_config():
    config_file = configobj.ConfigObj("config.cfg")
    config_file.encoding = "utf-8"

    global bilder_speicherplatz
    bilder_speicherplatz = str(pathlib.Path(config_file["Pfade"]["bilder_pfad"]))


def create_config():
    config_file = configobj.ConfigObj()
    config_file.filename = "config.cfg"
    config_file.encoding = "utf-8"

    config_file["Pfade"] = {}
    config_file["Pfade"]["bilder_pfad"] = ""

    config_file.write()
    

if __name__ == '__main__':
    t1 = threading.Thread(target=aktuallisiere_bilder)
    t2 = threading.Thread(target=keywatcher)

    read_config()

    app = QApplication(sys.argv)
    windowIcon = QIcon(str(logo_Pfad)) # Define Window Icon

    MainWindow = MainWindow()

    t1.start()
    t2.start()

    MainWindow.show()
    sys.exit(app.exec()) # alles beenden