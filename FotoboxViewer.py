import sys, os
from turtle import pd
import pathlib
from screeninfo import get_monitors
import PySide6.QtCore as QtCore
import threading
import keyboard
import signal
import ftplib
import glob

import myconfig
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PIL import Image

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
        self.ui.logo_links.mousePressEvent = self.kill_all

        pixmap_logo_rechts = QPixmap("data/logo_rechts.png")
        pixmap_logo_rechts = pixmap_logo_rechts.scaledToWidth(monitor_info['width']*prozent_werbung, mode=QtCore.Qt.TransformationMode.SmoothTransformation)
        self.ui.logo_rechts.setPixmap(pixmap_logo_rechts)

        self.setStyleSheet(f'background-image: url(:/BG/data/{tressor_data["bg"]}.jpg);')

    def kill_all(self, event):
        print('kill all')
        PID = os.getpid()
        os.kill(PID, signal.SIGTERM)
               
def change_big_images(last_image_names):
    aktueller_pfad = last_image_names[len(last_image_names)-1]

    pixmap = QPixmap(aktueller_pfad)

    pixmap = pixmap.scaledToHeight(int(monitor_info["heigth"] * prozent_grosses_bild), mode=QtCore.Qt.TransformationMode.SmoothTransformation)
    
    MainWindow.ui.bild_Gross.setPixmap(pixmap)
    
def change_little_iamges(last_image_names):
    for i, element in enumerate(last_image_names):
        aktueller_pfad = element

        pixmap = QPixmap(aktueller_pfad)
        pixmap = pixmap.scaledToHeight(int(monitor_info["heigth"] * prozent_kleines_bild), mode=QtCore.Qt.TransformationMode.SmoothTransformation)

        x = len(last_image_names)-i
        if x == 1 : 
            MainWindow.ui.bild_1.setPixmap(pixmap)
        elif x == 2 : 
            MainWindow.ui.bild_2.setPixmap(pixmap)
        elif x == 3 :  
            MainWindow.ui.bild_3.setPixmap(pixmap)
        elif x == 4 :  
            MainWindow.ui.bild_4.setPixmap(pixmap)


def get_files_in_folder():
    files = glob.glob(tressor_data["bilder_pfad"] + r'\\*.jpg')
    files = sorted(files, key=os.path.getmtime)
    return files[-6:]
          
def aktuaB(last_image_names):
    try:
        change_big_images(last_image_names)
    except:print(Exception)
    try:
        change_little_iamges(last_image_names[-6:-1])
    except:print(Exception)

def aktuallisiere_bilder():
    while True:
        last_image_names = get_files_in_folder()

        aktB = threading.Thread(target=aktuaB, args=(last_image_names,), name='aktuB')
        aktB.start()

        while aktB.is_alive():
            QApplication.processEvents()


def ftp_upload(file_path):

    filename = file_path.split('\\')
    filename = filename[len(filename)-1]

    ftp = ftplib.FTP(tressor_data["ftp_host"])
    ftp.login(tressor_data["ftp_user"],tressor_data["ftp_password"])

    try:
        ftp.cwd("autoimport/" + tressor_data["galerie"])
    except:
        ftp.mkd("autoimport/" + tressor_data["galerie"])
        ftp.cwd("autoimport/" + tressor_data["galerie"])

    myfile = open(file_path, 'rb')

    print(f"Upload start -> {file_path}")

    ftp.storbinary('STOR ' + filename, myfile)
    ftp.quit()

def read_upload_log(cfg_file_name):
    aktuelle_upload_liste = ()
    config_path = f"{tressor_data['bilder_pfad']}{cfg_file_name}"
    config_file = open(config_path, 'r')

    aktuelle_upload_liste = config_file.readlines()

    config_file.close()
    return aktuelle_upload_liste

def log_upload(file_upload):
    aktuelle_upload_liste = read_upload_log(r'/upload_log.cfg')
    aktuelle_upload_liste.append(file_upload)

    config_path = f"{tressor_data['bilder_pfad']}/upload_log.cfg"
    config_file = open(config_path, "w+")

    for i in range(len(aktuelle_upload_liste)):
        if aktuelle_upload_liste[i].endswith("\n")==False:
            aktuelle_upload_liste[i] = aktuelle_upload_liste[i] + "\n"
        config_file.writelines(aktuelle_upload_liste[i])

    config_file.close()

def upload_images_from_folder():
    while True:
        pfad = glob.glob(tressor_data["bilder_pfad"] + r'\compressed\\*.jpg')
        pfad = sorted(pfad, key=os.path.getctime)

        for img_path in pfad:
            bereits_hochgeladen = read_upload_log(r'/upload_log.cfg')
            res = any(img_path in string for string in bereits_hochgeladen)
            if res == False:
                upload_log(dateipfad=img_path)

def upload_log(dateipfad):
        try:
            ftp_upload(dateipfad)
            print(f"Upload abgeschlossen -> {dateipfad}")
            log_upload(dateipfad)
        except:
            print(f"Fehler beim upload -> {dateipfad}")


def save_folder_ueberwachen():
    while True:
        files = glob.glob(tressor_data["bilder_pfad"] + '/*.jpg')
        files = sorted(files, key=os.path.getmtime)

        if len(files) <= 5: 
            for element in files:
                count = glob.glob(tressor_data["bilder_pfad"] + r'\compressed' + '/*.jpg')
                res = check_if_compressed(element)
                if res == 0:
                    img_compress(element, tressor_data["bilder_pfad"] + r'\compressed\\', count)
        else:
            res = check_if_compressed(files[0])
            if res == 0:
                count = glob.glob(tressor_data["bilder_pfad"] + r'\compressed' + '/*.jpg')
                img_compress(files[0], tressor_data["bilder_pfad"] + r'\compressed\\', count)
            
            count = glob.glob(tressor_data["bilder_pfad"] + r'\original' + '/*.jpg')
            img_move(files[0], tressor_data["bilder_pfad"] + r'\original\\', count)

def check_if_compressed(path_file):
    bereits_umgewandelt = read_upload_log(r'/compressed_log.cfg')
    for zeile in bereits_umgewandelt:
        if path_file in zeile:
            return 1
    return 0

def log_compressed(path_file):
    aktuelle_upload_liste = read_upload_log(r'/compressed_log.cfg')
    aktuelle_upload_liste.append(path_file)

    config_path = f"{tressor_data['bilder_pfad']}/compressed_log.cfg"
    config_file = open(config_path, "w+")

    for i in range(len(aktuelle_upload_liste)):
        if aktuelle_upload_liste[i].endswith("\n")==False:
            aktuelle_upload_liste[i] = aktuelle_upload_liste[i] + "\n"
        config_file.writelines(aktuelle_upload_liste[i])

    config_file.close()

def img_move(origin_path, new_path, count):
    os.rename(origin_path, new_path + r'IMG_' + str(len(count)+1).zfill(4) + '.JPG')
    print(origin_path + "  --->  " + new_path + r'IMG_' + str(len(count)+1).zfill(4) + '.JPG')

def img_compress(old_path, new_path, count):
    img = Image.open(str(old_path))

    b = img.width
    h = img.height

    faktor = int(tressor_data['max_bild_breite']) / b
    b = int(tressor_data['max_bild_breite'])
    h = h * faktor

    img = img.resize((int(b), int(h)), Image.Resampling.LANCZOS)
    img.save(new_path + 'IMG_' + str(len(count)+1).zfill(4) + '.JPG', optimize=True, quality=80)

    log_compressed(old_path)

if __name__ == '__main__':

    # Pfade überprüfen

    if os.path.exists(tressor_data["bilder_pfad"]) == False:
        os.makedirs(tressor_data["bilder_pfad"])
    if os.path.exists(tressor_data["bilder_pfad"] + r'\original') == False:
        os.makedirs(tressor_data["bilder_pfad"] + r'\original')
    if os.path.exists(tressor_data["bilder_pfad"] + r'\ftp_upload') == False:
        os.makedirs(tressor_data["bilder_pfad"] + r'\ftp_upload')
    if os.path.exists(tressor_data["bilder_pfad"] + r'\compressed') == False:
        os.makedirs(tressor_data["bilder_pfad"] + r'\compressed')

    config_path = f"{tressor_data['bilder_pfad']}/upload_log.cfg"
    if os.path.exists(config_path) == False:
        f=open(config_path, 'w+')
        f.close()
    if os.path.exists(f"{tressor_data['bilder_pfad']}/compressed_log.cfg") == False:
        f=open(f"{tressor_data['bilder_pfad']}/compressed_log.cfg", 'w+')
        f.close()
    
    # Code
    app = QApplication(sys.argv)
    windowIcon = QIcon(str(logo_Pfad)) # Define Window Icon

    MainWindow = MainWindow()

    mainFolderObserver = threading.Thread(target=save_folder_ueberwachen, args=(), name="MainFolderWatcher")
    bilderAktuallisieren = threading.Thread(target=aktuallisiere_bilder, args=(), name="Bilder Aktualisieren")
    ftpUpload = threading.Thread(target=upload_images_from_folder, args=(), name="Monitor Folder")

    mainFolderObserver.start() # ordner überwachen und bilder compriemierun und sotieren
    bilderAktuallisieren.start() # aktuelle bilder anzeigen in der Fotobox
    ftpUpload.start() # Upload images

    MainWindow.show()
    sys.exit(app.exec()) # alles beenden