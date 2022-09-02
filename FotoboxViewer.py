from ast import arg
import shutil
import sys, os
import time
import PyQt6, PySide6
import pathlib
from screeninfo import get_monitors
import PySide6.QtCore as QtCore
import threading
import keyboard
import signal
import ftplib

import configobj
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logo_Pfad = str(pathlib.Path('data\\icon.png').absolute())
global windowIcon # Define Var vor icon

global tressor_data
tressor_data = {}

global hochladen_ftp
hochladen_ftp = []

prozent_grosses_bild = 0.445
prozent_kleines_bild = 0.16

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

        self.ui.logo_ffwprosdorf.setGeometry(monitor_info['x'] + 40, monitor_info['y'] + 40,140,178)
        self.ui.logo_3ddruck.setGeometry(monitor_info['x'] + monitor_info['width'] - 40 - 175, monitor_info['y'] + 40,175,109)

        self.ui.bild_Gross.setVisible(False)
        self.ui.bild_1.setVisible(False)
        self.ui.bild_2.setVisible(False)
        self.ui.bild_3.setVisible(False)
        self.ui.bild_4.setVisible(False)
        self.ui.bild_5.setVisible(False)
        self.ui.bild_6.setVisible(False)
        self.ui.bild_7.setVisible(False)
        self.ui.bild_8.setVisible(False)
   
class MyEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        add_to_list(event.src_path)


def change_big_images(last_image_names):
    aktueller_pfad = bilder_speicherplatz + "\\" + last_image_names[len(last_image_names)-1]

    scaled = calc_big_image(aktueller_pfad)
    pos_x ,pos_y = calc_big_image_pos(scaled["width"], scaled["heigth"])

    pixmap = QPixmap(aktueller_pfad)
    pixmap = pixmap.scaled(scaled["width"], scaled["heigth"])
    MainWindow.ui.bild_Gross.setPixmap(pixmap)

    MainWindow.ui.bild_Gross.setGeometry(pos_x,pos_y, scaled["width"], scaled["heigth"])
    MainWindow.ui.bild_Gross.setVisible(True)

def change_little_iamges(last_image_names):
    for i in range(len(last_image_names)):
        aktueller_pfad = bilder_speicherplatz + "\\" + last_image_names[len(last_image_names)-1-i]
        
        scaled = calc_little_image(aktueller_pfad)
        pos_x ,pos_y = calc_little_image_pos(scaled["width"], scaled["heigth"], i)
        
        pixmap = QPixmap(aktueller_pfad)
        pixmap = pixmap.scaled(scaled["width"], scaled["heigth"])

        img_margin = (scaled["width"] * 0.15)

        if i == 1 : 
            MainWindow.ui.bild_1.setPixmap(pixmap)
            MainWindow.ui.bild_1.setGeometry(pos_x - img_margin, pos_y, scaled["width"], scaled["heigth"])
            MainWindow.ui.bild_1.setVisible(True)
        if i == 2 :
            MainWindow.ui.bild_2.setPixmap(pixmap)
            MainWindow.ui.bild_2.setGeometry(pos_x - (img_margin / 2), pos_y, scaled["width"], scaled["heigth"])
            MainWindow.ui.bild_2.setVisible(True)
        if i == 3 : 
            MainWindow.ui.bild_3.setPixmap(pixmap)
            MainWindow.ui.bild_3.setGeometry(pos_x + (img_margin / 2), pos_y, scaled["width"], scaled["heigth"])
            MainWindow.ui.bild_3.setVisible(True)
        if i == 4 : 
            MainWindow.ui.bild_4.setPixmap(pixmap)
            MainWindow.ui.bild_4.setGeometry(pos_x + img_margin, pos_y, scaled["width"], scaled["heigth"])
            MainWindow.ui.bild_4.setVisible(True)
        if i == 5 : 
            MainWindow.ui.bild_5.setPixmap(pixmap)
            MainWindow.ui.bild_5.setGeometry(pos_x - img_margin, pos_y, scaled["width"], scaled["heigth"])
            MainWindow.ui.bild_5.setVisible(True)
        if i == 6 : 
            MainWindow.ui.bild_6.setPixmap(pixmap)
            MainWindow.ui.bild_6.setGeometry(pos_x - (img_margin / 2), pos_y, scaled["width"], scaled["heigth"])
            MainWindow.ui.bild_6.setVisible(True)
        if i == 7 : 
            MainWindow.ui.bild_7.setPixmap(pixmap)
            MainWindow.ui.bild_7.setGeometry(pos_x + (img_margin / 2), pos_y, scaled["width"], scaled["heigth"])
            MainWindow.ui.bild_7.setVisible(True)
        if i == 8 : 
            MainWindow.ui.bild_8.setPixmap(pixmap)
            MainWindow.ui.bild_8.setGeometry(pos_x + img_margin, pos_y, scaled["width"], scaled["heigth"])
            MainWindow.ui.bild_8.setVisible(True)

def calc_big_image(aktueller_pfad):
    global big_heigth
    scaled = {}
    im = Image.open(aktueller_pfad)
    img_width, img_height = im.size

    scaled["format"] = img_width/img_height

    scaled["width"] = monitor_info['width'] * prozent_grosses_bild
    scaled["heigth"] = scaled["width"] / img_width * img_height

    big_heigth = scaled["heigth"]
    return scaled

def calc_big_image_pos(width, heigth):
    global big_pos_y
    
    pos_x = (monitor_info["width"] / 2) - (width / 2)
    pos_y = (monitor_info["heigth"] + heigth/2) * 0.01

    big_pos_y = pos_y

    return pos_x, pos_y


def calc_little_image(aktueller_pfad):
    scaled = {}
    im = Image.open(aktueller_pfad)
    img_width, img_height = im.size

    scaled["format"] = img_width/img_height

    scaled["width"] = monitor_info['width'] * prozent_kleines_bild
    scaled["heigth"] = scaled["width"] / img_width * img_height

    return scaled

def calc_little_image_pos(width, heigth, aktuellesBild):
    global big_pos_y
    
    if aktuellesBild < 5: 
        pos_x = (monitor_info["width"] / 5 * aktuellesBild) - (width / 2)
        pos_y = (monitor_info["heigth"] + heigth/2 + big_heigth) * 0.24
    elif aktuellesBild >= 5: 
        pos_x = (monitor_info["width"] / 5 * (aktuellesBild - 4)) - (width / 2)
        pos_y = (monitor_info["heigth"] + heigth/2 + big_heigth) * 0.328

    return pos_x, pos_y


def get_files_in_folder():
    pfad = []
    _,_, images = next(os.walk(bilder_speicherplatz))
    for i in range(len(images)):
        if (images[i].endswith(".JPG")):
            pfad.append(images[i])
    return pfad[-9:]

            
def read_config():
    tressor_data = {}

    config_file = configobj.ConfigObj("config.cfg")
    config_file.encoding = "utf-8"

    global bilder_speicherplatz
    bilder_speicherplatz = str(pathlib.Path(config_file["Pfade"]["bilder_pfad"]))

    tressor_data["ftp_host"] = config_file["Pictrs"]["ftp_host"]
    tressor_data["ftp_user"] = config_file["Pictrs"]["ftp_user"]
    tressor_data["ftp_password"] = config_file["Pictrs"]["ftp_password"]
    tressor_data["ftp_port"] = config_file["Pictrs"]["ftp_port"]
    tressor_data["galerie"] = config_file["Pictrs"]["galerie"]

    return tressor_data

def create_config():
    config_file = configobj.ConfigObj()
    config_file.filename = "config.cfg"
    config_file.encoding = "utf-8"

    config_file["Pfade"] = {}
    config_file["Pfade"]["bilder_pfad"] = ""

    config_file["Pictrs"] = {}
    config_file["Pictrs"]["ftp_host"] = ""
    config_file["Pictrs"]["ftp_user"] = ""
    config_file["Pictrs"]["ftp_password"] = ""
    config_file["Pictrs"]["ftp_port"] = ""

    config_file.write()

def aktuallisiere_bilder():
    while True:
        last_image_names = []
        last_image_names = get_files_in_folder()

        try:change_big_images(last_image_names)
        except:print("Kein Bilde gefunden")

        try:change_little_iamges(last_image_names)
        except:print("Kein Bilde gefunden")

        time.sleep(3)
        global stop_threads
        if stop_threads:
            break

def keywatcher():
    while True:
        if keyboard.is_pressed('q'):
            print('kill all')
            PID = os.getpid()
            os.kill(PID, signal.SIGTERM)


def add_to_list(src_path):
    global hochladen_ftp
    hochladen_ftp = []
    hochladen_ftp.append(src_path)
    print(hochladen_ftp)

def rename_and_move_images():
    while True:
        global hochladen_ftp
        if len(hochladen_ftp) >=1:
            for i in range(len(hochladen_ftp)):
                oldpath = hochladen_ftp[i-1]
                _,_, images = next(os.walk(bilder_speicherplatz +  "\\"  + "ftp_upload"))
                count = []
                for j in range(len(images)):
                    if (images[j].endswith(".JPG")):
                        count.append(j)

                if os.path.exists(bilder_speicherplatz +  "\\"  + "ftp_upload" ) ==False:
                    os.makedirs(bilder_speicherplatz +  "\\"  + "ftp_upload")
                    
                new_path = bilder_speicherplatz +  "\\"  + "ftp_upload" +  "\\" + tressor_data["galerie"] + "_" + str(len(count)) + ".jpg"
                shutil.copy(oldpath, new_path)

                try:
                    ftp_upload(new_path, tressor_data["galerie"] + "_" + str(len(count)) + ".jpg")
                except:
                    print("Fehler beim upload")

                hochladen_ftp.remove(hochladen_ftp[i-1])

def ftp_upload(file_path, filename):
    ftp = ftplib.FTP(tressor_data["ftp_host"])
    ftp.login(tressor_data["ftp_user"],tressor_data["ftp_password"])
    new_file_path = str(pathlib.Path(file_path).absolute())
    myfile = open(new_file_path, 'rb')
    print(filename)
    ftp.storlines('STOR ' + filename,myfile)
    ftp.quit()


def watch_folder():
    event_handler = MyEventHandler()

    my_observer = Observer()
    my_observer.schedule(event_handler, bilder_speicherplatz, recursive=True)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        my_observer.stop()
        my_observer.join()


if __name__ == '__main__':

    global stop_threads
    stop_threads = False
    t1 = threading.Thread(target=aktuallisiere_bilder, args=(), name="Bilder Aktualisieren")
    t2 = threading.Thread(target=keywatcher, args=(), name="Colse watcher")
    t3 = threading.Thread(target=watch_folder, args=(), name="Monitor Folder")
    t4 = threading.Thread(target=rename_and_move_images, args=(), name="ftp_upload")

    tressor_data = read_config()

    app = QApplication(sys.argv)
    windowIcon = QIcon(str(logo_Pfad)) # Define Window Icon

    MainWindow = MainWindow()

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    MainWindow.show()
    sys.exit(app.exec()) # alles beenden