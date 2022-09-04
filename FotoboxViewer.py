from ast import arg
from pickletools import optimize
import shutil
import sys, os
import time
from tkinter.tix import IMAGE
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
import PIL
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
        if images[i].endswith(".JPG") or images[i].endswith(".jpg"):
            pfad.append(images[i])
    return pfad[-9:]

            
def read_config():
    tressor_data = {}

    config_file = configobj.ConfigObj("config.cfg")
    config_file.encoding = "utf-8"

    global bilder_speicherplatz
    bilder_speicherplatz = str(pathlib.Path(config_file["Pfade"]["bilder_pfad"]))
    tressor_data["bilder_pfad"] = str(pathlib.Path(config_file["Pfade"]["bilder_pfad"]))

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
        except:print("Keine Bilder gefunden")

        try:change_little_iamges(last_image_names)
        except:print("Keine Bilder gefunden")

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

def rename_and_copy_images(dateipfad):
        hochladen_ftp_temp = dateipfad


        if os.path.exists(bilder_speicherplatz +  "\\ftp_upload") ==False:
                os.makedirs(bilder_speicherplatz +  "\\"  + "ftp_upload")

        oldpath = hochladen_ftp_temp
        _,_, images = next(os.walk(bilder_speicherplatz +  "\\"  + "ftp_upload"))
        count = []
        for j in range(len(images)):
            if images[j].endswith(".jpg") or images[j].endswith(".JPG"):
                count.append(j)
            
        new_path = bilder_speicherplatz +  "\\ftp_upload\\" + tressor_data["galerie"] + "_" + str(len(count)) + ".jpg"
        
        time.sleep(2)
        try:
            shutil.copy(oldpath, new_path)
        except: 
            os.remove(new_path)
            hochladen_ftp.insert(0, hochladen_ftp_temp)

        ftp_image_name = tressor_data["galerie"] + "_" + str(len(count)) + ".jpg"
        try:
            ftp_upload(new_path, ftp_image_name)
            print(f"Upload abgeschlossen -> {ftp_image_name}")
        except:
            hochladen_ftp.insert(0, hochladen_ftp_temp)
            print("Fehler beim upload")

def img_comp(file_path):
    img = Image.open(file_path)
    # x,y = img.size
    # img = img.resize((x,y),PIL.Image.Resampling.LANCZOS)
    img.save(file_path, optimize=True, quality=50)

def ftp_upload(file_path, filename):

    img_comp(file_path)

    time.sleep(2)

    ftp = ftplib.FTP(tressor_data["ftp_host"])
    ftp.login(tressor_data["ftp_user"],tressor_data["ftp_password"])

    try:
        ftp.cwd("autoimport/" + tressor_data["galerie"])
    except:
        ftp.mkd("autoimport/" + tressor_data["galerie"])
        ftp.cwd("autoimport/" + tressor_data["galerie"])

    new_file_path = str(pathlib.Path(file_path).absolute())
    myfile = open(new_file_path, 'rb')
    print(f"Upload -> {filename}")

    ftp.storbinary('STOR ' + filename, myfile)
    ftp.quit()


def watch_folder():
    pfad_1 = []
    pfad_2 = []
    _,_, images = next(os.walk(bilder_speicherplatz))
    for i in range(len(images)):
        if (images[i].endswith(".JPG")) or (images[i].endswith(".jpg")):
            pfad_1.append(images[i])
    pfad_2 = pfad_1
    
    while True:
        pfad_1 = []
        _,_, images = next(os.walk(bilder_speicherplatz))
        for j in range(len(images)):
            if (images[j].endswith(".JPG")) or (images[j].endswith(".jpg")):
                pfad_1.append(images[j])

        for k in range(len(pfad_1)-1):
            if pfad_1[k] in pfad_2:
                continue
            else:
                rename_and_copy_images(bilder_speicherplatz + "\\" + pfad_1[k])
                print(bilder_speicherplatz + "\\" + pfad_1[k])

        pfad_2 = pfad_1
        time.sleep(5)



if __name__ == '__main__':

    tressor_data = read_config()

    if os.path.exists(tressor_data["bilder_pfad"]) == False:
        os.makedirs(tressor_data["bilder_pfad"])

    global stop_threads
    stop_threads = False
    t1 = threading.Thread(target=aktuallisiere_bilder, args=(), name="Bilder Aktualisieren")
    t2 = threading.Thread(target=keywatcher, args=(), name="Colse watcher")
    t3 = threading.Thread(target=watch_folder, args=(), name="Monitor Folder")

    app = QApplication(sys.argv)
    windowIcon = QIcon(str(logo_Pfad)) # Define Window Icon

    MainWindow = MainWindow()

    t1.start()
    t2.start()
    t3.start()

    MainWindow.show()
    sys.exit(app.exec()) # alles beenden