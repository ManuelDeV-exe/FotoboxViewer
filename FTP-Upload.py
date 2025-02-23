import sys, os
import ftplib
import threading
import time
import glob
import shutil
import paramiko

import reg_config

import PySide6
from PySide6.QtGui import *
from PySide6.QtWidgets import *

logo_Pfad = os.path.abspath('data/icon.png')

mypaths_schlüssel =('upload_folder', 'kamera_folder', 'viewer_path', 'upload_path')
mypictrs_schlüssel =('ftp_host', 'ftp_user', 'ftp_password', 'galerie_folder')

MyPaths = reg_config.My_Config('Paths', mypaths_schlüssel)
MyPictrs = reg_config.My_Config('Pictrs', mypictrs_schlüssel)

thread_wait = True

from ui_FTP_starten import Ui_FTP_starten

class FTP_starten(QMainWindow):
    def __init__(self):
        super(FTP_starten, self).__init__()
        self.ui = Ui_FTP_starten()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(str(logo_Pfad)))

        self.ui.start_BTN.clicked.connect(start)
        self.ui.stop_BTN.clicked.connect(stop)

        self.show()

def upload_file(file):
    try:
        # Aufbau der SFTP-Verbindung über Port 22
        transport = paramiko.Transport((MyPictrs.config['ftp_host'], 22))
        transport.connect(username=MyPictrs.config['ftp_user'], password=MyPictrs.config['ftp_password'])
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Wechsel in das Galerie-Verzeichnis oder erstelle es, falls es nicht existiert
        try:
            sftp.chdir(MyPictrs.config['galerie_folder'])
        except IOError:
            sftp.mkdir(MyPictrs.config['galerie_folder'])
            sftp.chdir(MyPictrs.config['galerie_folder'])

            # Upload von Dateien und Erstellen von Unterverzeichnissen aus data\ImagePage
            local_dir = os.path.abspath(r'data\ImagePage')
            for item in os.listdir(local_dir):
                local_path = os.path.join(local_dir, item)
                if os.path.isfile(local_path):
                    sftp.put(local_path, item)
                elif os.path.isdir(local_path):
                    try:
                        sftp.mkdir(item)
                    except IOError:
                        pass  # Verzeichnis existiert bereits

            time.sleep(0.5)
            # Wechsel in das "js" Unterverzeichnis und lade dort Dateien hoch
            try:
                sftp.chdir("js")
            except IOError:
                sftp.mkdir("js")
                sftp.chdir("js")
            js_local_dir = os.path.abspath(r'data\ImagePage\js')
            for item in os.listdir(js_local_dir):
                local_path = os.path.join(js_local_dir, item)
                if os.path.isfile(local_path):
                    sftp.put(local_path, item)
                elif os.path.isdir(local_path):
                    try:
                        sftp.mkdir(item)
                    except IOError:
                        pass
            sftp.chdir("..")

        # Wechsel in das "data"-Verzeichnis oder erstelle es, falls es nicht existiert
        try:
            sftp.chdir("data")
        except IOError:
            sftp.mkdir("data")
            time.sleep(0.5)
            sftp.chdir("data")

        # Bestimme den Dateinamen aus dem übergebenen Pfad
        filename = os.path.basename(file)

        print(f"Upload start -> {file}")
        sftp.put(file, filename)
        
        # Warte, bis der Upload vollständig ist
        wait_for_upload_completion(sftp, filename, file)

        sftp.close()
        transport.close()

        log_uploaded_file(file)
        print(f"Upload beendet -> {file}")

    except Exception as ex:
        print(f"Fehler: {ex}")

def wait_for_upload_completion(sftp, remote_file, local_file, max_retries=10, wait_time=1):
    """
    Überprüft, ob die Datei auf dem Server vollständig hochgeladen wurde,
    indem die Dateigröße verglichen wird.
    """
    local_size = os.path.getsize(local_file)

    for attempt in range(max_retries):
        try:
            remote_size = sftp.stat(remote_file).st_size
            if remote_size == local_size:
                print(f"Datei vollständig hochgeladen: {remote_file}")
                return
            else:
                print(f"Warten auf vollständigen Upload ({remote_size}/{local_size} Bytes)...")
        except Exception as e:
            print(f"Fehler beim Abrufen der Dateigröße ({remote_file}): {e}")

        time.sleep(wait_time)

    print(f"Warnung: Upload von {remote_file} konnte nicht verifiziert werden!")

def log_uploaded_file(file):
    if os.path.exists(MyPaths.config['upload_folder'] + "/log.log") == False:
        with open(MyPaths.config['upload_folder'] + "/log.log", 'w+') as f:
            f.close()

    with open(MyPaths.config['upload_folder'] + "/log.log", 'a+') as f:
            f.write(file + '\n')
            f.close()

def read_update_log(file):
    if os.path.exists(MyPaths.config['upload_folder'] + "/log.log") == False:
        with open(MyPaths.config['upload_folder'] + "/log.log", 'w+') as f:
            f.close()

    with open(MyPaths.config['upload_folder'] + "/log.log", 'r') as f:
            text = f.read()
            f.close()
    
    if file in text:
        return False
    return True

def start():
    global thread_wait
    thread_wait = False 
    
    FTP_starten.ui.start_BTN.setStyleSheet('background-color: #84ffc0')
    FTP_starten.ui.start_BTN.setEnabled(False)

def stop():
    global thread_wait
    thread_wait = True

    FTP_starten.ui.start_BTN.setStyleSheet('background-color: none')
    FTP_starten.ui.start_BTN.setEnabled(True)

def watchfolder_upload():
    while True:

        if thread_wait:
            continue

        files = glob.glob(MyPaths.config['upload_folder'] + r'\\*.jpg')
        files = sorted(files, key=os.path.getmtime)

        for file in files:
            if read_update_log(file) == True and thread_wait == False:
                upload_file(file)
        
        time.sleep(3)
   
if __name__ == '__main__':

    if MyPictrs.config['ftp_host'] == '' or MyPictrs.config['ftp_user'] == '' or MyPictrs.config['ftp_password'] == '' or MyPictrs.config['galerie_folder'] == '':
        print('Fehler keine FTP-Daten!')

    app = QApplication(sys.argv)
    
    FTP_starten = FTP_starten()

    watchfolder_upload = threading.Thread(target=watchfolder_upload, args=[], name='watchfolder_upload', daemon=True)
    watchfolder_upload.start()

    sys.exit(app.exec())