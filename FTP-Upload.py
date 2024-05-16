import sys, os
import ftplib
import threading
import time
import glob
import shutil

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
        ftp = ftplib.FTP_TLS()
        ftp.connect(MyPictrs.config['ftp_host'])

        ftp.auth()
        ftp.prot_p()

        ftp.login(MyPictrs.config['ftp_user'],MyPictrs.config['ftp_password'])

        try:
            ftp.cwd(MyPictrs.config['galerie_folder'])
        except:
            ftp.mkd(MyPictrs.config['galerie_folder'])
            ftp.cwd(MyPictrs.config['galerie_folder'])

            for item in os.listdir(os.path.abspath('data\ImagePage')):
                local_path = os.path.join(os.path.abspath('data\ImagePage'), item)
                if os.path.isfile(local_path):
                    # Lade die Datei hoch
                    with open(local_path, 'rb') as file:
                        ftp.storbinary(f'STOR {item}', file)
                elif os.path.isdir(local_path):
                    # Rekursiver Aufruf für Unterverzeichnisse
                    ftp.mkd(item)
            
            ftp.cwd("js")
            for item in os.listdir(os.path.abspath('data\ImagePage\js')):
                local_path = os.path.join(os.path.abspath('data\ImagePage\js'), item)
                if os.path.isfile(local_path):
                    # Lade die Datei hoch
                    with open(local_path, 'rb') as file:
                        ftp.storbinary(f'STOR {item}', file)
                elif os.path.isdir(local_path):
                    # Rekursiver Aufruf für Unterverzeichnisse
                    ftp.mkd(item)
            ftp.cwd("../")

        ftp.cwd("data")
        myfile = open(file, 'rb')

        filename = file.split("\\")
        filename = filename[len(filename)-1]

        print(f"Upload start -> {file}")

        ftp.storbinary('STOR ' + filename, myfile)
        ftp.quit()

        log_uploaded_file(file)
        print(f"Upload beendet -> {file}")
    except Exception as ex:
        print(ex)

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
            if read_update_log(file) == True:
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