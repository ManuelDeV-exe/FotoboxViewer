import shutil
import sys, os
import time
from tkinter.tix import IMAGE
from turtle import pd
import PyQt6, PySide6
import pathlib
from screeninfo import get_monitors
import PySide6.QtCore as QtCore
import threading
import keyboard
import signal
import ftplib
import logging

import myconfig
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

tressor_data = myconfig.read_config()

prozent_grosses_bild = float(tressor_data['prozent_grosses_bild']) # Wert in Prozent der Seitenhöhe
prozent_kleines_bild = float(tressor_data['prozent_kleines_bild']) # Wert in Prozent der Seitenhöhe
prozent_werbung = float(tressor_data['prozent_werbung']) # Wert in Prozent der Seitenbreite

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

        pixmap_logo_links = QPixmap("data/logo_links.png")
        pixmap_logo_links = pixmap_logo_links.scaledToWidth(monitor_info['width']*prozent_werbung, mode=QtCore.Qt.TransformationMode.SmoothTransformation)
        self.ui.logo_links.setPixmap(pixmap_logo_links)

        pixmap_logo_rechts = QPixmap("data/logo_rechts.png")
        pixmap_logo_rechts = pixmap_logo_rechts.scaledToWidth(monitor_info['width']*prozent_werbung, mode=QtCore.Qt.TransformationMode.SmoothTransformation)
        self.ui.logo_rechts.setPixmap(pixmap_logo_rechts)

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
    aktueller_pfad = tressor_data["bilder_pfad"] + "\\" + last_image_names[len(last_image_names)-1]

    pixmap = QPixmap(aktueller_pfad)
    pixmap = pixmap.scaledToHeight(monitor_info["heigth"] * prozent_grosses_bild, mode=QtCore.Qt.TransformationMode.SmoothTransformation)
    MainWindow.ui.bild_Gross.setPixmap(pixmap)

    MainWindow.ui.bild_Gross.setVisible(True)

def change_little_iamges(last_image_names):
    for i in range(len(last_image_names)):
        aktueller_pfad = tressor_data["bilder_pfad"] + "\\" + last_image_names[len(last_image_names)-1-i]
        
        pixmap = QPixmap(aktueller_pfad)
        pixmap = pixmap.scaledToHeight(monitor_info["heigth"] * prozent_kleines_bild, mode=QtCore.Qt.TransformationMode.SmoothTransformation)


        if i == 1 : 
            MainWindow.ui.bild_1.setPixmap(pixmap)
            MainWindow.ui.bild_1.setVisible(True)
        if i == 2 :
            MainWindow.ui.bild_2.setPixmap(pixmap)
            MainWindow.ui.bild_2.setVisible(True)
        if i == 3 : 
            MainWindow.ui.bild_3.setPixmap(pixmap)
            MainWindow.ui.bild_3.setVisible(True)
        if i == 4 : 
            MainWindow.ui.bild_4.setPixmap(pixmap)
            MainWindow.ui.bild_4.setVisible(True)
        if i == 5 : 
            MainWindow.ui.bild_5.setPixmap(pixmap)
            MainWindow.ui.bild_5.setVisible(True)
        if i == 6 : 
            MainWindow.ui.bild_6.setPixmap(pixmap)
            MainWindow.ui.bild_6.setVisible(True)
        if i == 7 : 
            MainWindow.ui.bild_7.setPixmap(pixmap)
            MainWindow.ui.bild_7.setVisible(True)
        if i == 8 : 
            MainWindow.ui.bild_8.setPixmap(pixmap)
            MainWindow.ui.bild_8.setVisible(True)


def get_files_in_folder():
    pfad = []
    images = os.listdir(tressor_data["bilder_pfad"])
    for i in range(len(images)):
        if images[i].endswith(".JPG") or images[i].endswith(".jpg"):
            pfad.append(images[i])
    return pfad[-9:]
          
def aktuallisiere_bilder():
    while True:
        last_image_names = []
        last_image_names = get_files_in_folder()

        try:change_big_images(last_image_names)
        except:print("Keine Bilder gefunden")

        try:change_little_iamges(last_image_names)
        except:print("Keine Bilder gefunden")

        time.sleep(3)

def keywatcher():
    while True:
        if keyboard.is_pressed('q'):
            print('kill all')
            PID = os.getpid()
            os.kill(PID, signal.SIGTERM)

def rename_copy_upload_log(dateipfad, dateiname):
        if os.path.exists(tressor_data["bilder_pfad"] +  "\\ftp_upload") ==False:
                os.makedirs(tressor_data["bilder_pfad"] +  "\\"  + "ftp_upload")

        old_path = dateipfad
        _,_, images = next(os.walk(tressor_data["bilder_pfad"] +  "\\"  + "ftp_upload"))
        count = []
        for j in range(len(images)):
            if images[j].endswith(".jpg") or images[j].endswith(".JPG"):
                count.append(j)
            
        new_path = f"{tressor_data['bilder_pfad']}\\ftp_upload\\{tressor_data['galerie']}_{str(len(count))}.jpg"

        ftp_image_name = tressor_data["galerie"] + "_" + str(len(count)) + ".jpg"
        try:
            ftp_upload(old_path, new_path, ftp_image_name)
            logging.info(f"Upload abgeschlossen -> {ftp_image_name}")
            print(f"Upload abgeschlossen -> {ftp_image_name}")
            log_upload(dateiname)
        except:
            logging.warning(f"Fehler beim upload -> {dateipfad}")
            print(f"Fehler beim upload -> {dateipfad}")

def img_comp(old_path, file_path):
    img = Image.open(old_path)
    img.save(file_path, optimize=True, quality=50)
    time.sleep(0.5)

def ftp_upload(old_path, file_path, filename):

    img_comp(old_path, file_path)

    ftp = ftplib.FTP(tressor_data["ftp_host"])
    ftp.login(tressor_data["ftp_user"],tressor_data["ftp_password"])

    try:
        ftp.cwd("autoimport/" + tressor_data["galerie"])
    except:
        ftp.mkd("autoimport/" + tressor_data["galerie"])
        ftp.cwd("autoimport/" + tressor_data["galerie"])

    new_file_path = str(pathlib.Path(file_path).absolute())
    myfile = open(new_file_path, 'rb')

    logging.info(f"Upload start -> {filename}")
    print(f"Upload start -> {filename}")

    ftp.storbinary('STOR ' + filename, myfile)
    ftp.quit()

def read_upload_log():
    aktuelle_upload_liste = ()
    config_path = f"{tressor_data['bilder_pfad']}/upload_log.cfg"
    config_file = open(config_path, 'r')

    aktuelle_upload_liste = config_file.readlines()

    config_file.close()
    return aktuelle_upload_liste

def log_upload(file_upload):
    aktuelle_upload_liste = read_upload_log()
    aktuelle_upload_liste.append(file_upload)

    config_path = f"{tressor_data['bilder_pfad']}/upload_log.cfg"
    config_file = open(config_path, "w+")

    for i in range(len(aktuelle_upload_liste)):
        if aktuelle_upload_liste[i].endswith("\n")==False:
            aktuelle_upload_liste[i] = aktuelle_upload_liste[i] + "\n"
        config_file.writelines(aktuelle_upload_liste[i])

    config_file.close()

def watch_folder():
    while True:
        pfad = []
        backup_nach_upload = tressor_data["bilder_pfad"] + "/backup"
        images = os.listdir(tressor_data["bilder_pfad"])
        for i in range(len(images)):
            if images[i].endswith(".JPG") or images[i].endswith(".jpg"):
                pfad.append(images[i])

        for k in range(len(pfad)):
            bereits_hochgeladen = read_upload_log()

            res = any(pfad[k] in string for string in bereits_hochgeladen)
            if res == False:
                rename_copy_upload_log(dateipfad=tressor_data["bilder_pfad"] + "\\" + pfad[k], dateiname=pfad[k])

        try:
            res = pfad[:-9]
            for j in range(len(res)):
                if os.path.exists(backup_nach_upload)==False:os.makedirs(backup_nach_upload)
                shutil.move(tressor_data["bilder_pfad"] + "\\" + pfad[j], backup_nach_upload)
        except:
            pass

if __name__ == '__main__':

    # Pfade überprüfen

    if os.path.exists(tressor_data["bilder_pfad"]) == False:
        os.makedirs(tressor_data["bilder_pfad"])

    config_path = f"{tressor_data['bilder_pfad']}/upload_log.cfg"
    if os.path.exists(config_path) == False:
        f=open(config_path, 'w+')
        f.close()
    
    # Code

    logging.basicConfig(filename=tressor_data["bilder_pfad"] + '/log.log', encoding='utf-8', level=logging.INFO)

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