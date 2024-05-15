import sys, os
import threading
import glob
import time
import subprocess
import shutil
from PIL import Image
import psutil

import reg_config
myimages_schlüssel =('big_1', 'little_1', 'little_2', 'little_3', 'little_4')
mypaths_schlüssel =('upload_folder', 'kamera_folder', 'viewer_path', 'upload_path', 'full_size_folder')
mysettings_schlüssel =('upload', 'prozent_grosses_bild', 'prozent_kleines_bild', 'prozent_werbung', 'background_img', 'compressed_width')
mypictrs_schlüssel =('ftp_host', 'ftp_user', 'ftp_password', 'galerie_folder')

MyImages = reg_config.My_Config('Images', myimages_schlüssel)
MyPaths = reg_config.My_Config('Paths', mypaths_schlüssel)
MySettings = reg_config.My_Config('Settings', mysettings_schlüssel)
MyPictrs = reg_config.My_Config('Pictrs', mypictrs_schlüssel)

logo_Pfad = os.path.abspath(r'data/icon.png')
thread_wait = True
global kill
kill = False

import PySide6
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_core import Ui_Core

class UiCore(QMainWindow):
    def __init__(self):
        super(UiCore, self).__init__()
        self.ui = Ui_Core()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(str(logo_Pfad)))

        self.ui.path_kamera_folder.setText(MyPaths.config['kamera_folder'])
        self.ui.upload_folder.setText(MyPaths.config['upload_folder'])
        self.ui.viewer_path.setText(MyPaths.config['viewer_path'])
        self.ui.upload_path.setText(MyPaths.config['upload_path'])
        self.ui.full_size_folder.setText(MyPaths.config['full_size_folder'])

        self.ui.Upload_Radio.setChecked(True if MySettings.config['upload'] == "True" else False)
        self.ui.prozent_werbung.setText(MySettings.config['prozent_werbung'])
        self.ui.prozent_kleines_bild.setText(MySettings.config['prozent_kleines_bild'])
        self.ui.prozent_grosses_bild.setText(MySettings.config['prozent_grosses_bild'])
        self.ui.background.setValue(int(MySettings.config['background_img']))
        self.ui.compressed_width.setText(MySettings.config['compressed_width'])

        self.ui.Upload_folder_name.setText(MyPictrs.config['galerie_folder'])

        self.ui.save_BTN.clicked.connect(self.save)
        self.ui.start_viewer_BTN.clicked.connect(self.openPGM)

        self.ui.start_BTN.clicked.connect(start)
        self.ui.stop_BTN.clicked.connect(stop)

        self.show()

    def openPGM(self):
        # subprocess.Popen(MyPaths.config['viewer_path'], stdout=subprocess.PIPE)
        os.spawnl(os.P_NOWAIT,MyPaths.config['viewer_path'], "--startup")

        if True if MySettings.config['upload'] == "True" else False == True:
            for proc in psutil.process_iter():
                try:
                    if proc.name() == "FTP-Upload.exe":
                        print("Notepad läuft bereits")
                        break
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            else:
                subprocess.Popen(MyPaths.config['upload_path'], stdout=subprocess.PIPE)

    def save(self):
        MyPaths.write('kamera_folder', self.ui.path_kamera_folder.text())
        MyPaths.write('upload_folder', self.ui.upload_folder.text())
        MyPaths.write('viewer_path', self.ui.viewer_path.text())
        MyPaths.write('upload_path', self.ui.upload_path.text())
        MyPaths.write('full_size_folder', self.ui.full_size_folder.text())

        MySettings.write('compressed_width', self.ui.compressed_width.text())
        MySettings.write('upload', self.ui.Upload_Radio.isChecked())
        MySettings.write('background_img', self.ui.background.value())
        MySettings.write('prozent_werbung', self.ui.prozent_werbung.text())
        MySettings.write('prozent_kleines_bild', self.ui.prozent_kleines_bild.text())
        MySettings.write('prozent_grosses_bild', self.ui.prozent_grosses_bild.text())

        MyPictrs.write('galerie_folder', self.ui.Upload_folder_name.text())

def watchfolder():
    global kill
    while True:
        if kill: break
        if thread_wait:
            continue

        files = glob.glob(MyPaths.config['kamera_folder'] + r'\\*.jpg')
        files = sorted(files, key=os.path.getmtime)
        
        old_path = []
        old_path.append(MyImages.config['big_1'])
        old_path.append(MyImages.config['little_1'])
        old_path.append(MyImages.config['little_1'])
        old_path.append(MyImages.config['little_1'])
        old_path.append(MyImages.config['little_1'])

        MyImages.read_new()

        new_path = []
        new_path.append(MyImages.config['big_1'])
        new_path.append(MyImages.config['little_1'])
        new_path.append(MyImages.config['little_1'])
        new_path.append(MyImages.config['little_1'])
        new_path.append(MyImages.config['little_1'])
        
        for index, new in enumerate(new_path):
            if new == '' and len(files) == 0: 
                continue
            elif len(files) >= 1:
                MyImages.write('big_1', files[len(files)-1])

                for index, file in enumerate(files):
                    if index == 0:continue
                    if index >=5:continue
                    MyImages.write(f'little_{index}', files[len(files)-index-1])
            else:
                if new != old_path[index]:
                    try:
                        MyImages.write('big_1', files[len(files)-1])
                        print(files[len(files)-1])
                        if len(files) <=1: continue
                        MyImages.write('little_1', files[len(files)-2])
                        print(files[len(files)-2])
                        if len(files) <=2: continue
                        MyImages.write('little_2', files[len(files)-3])
                        print(files[len(files)-3])
                        if len(files) <=3: continue
                        MyImages.write('little_3', files[len(files)-4])
                        print(files[len(files)-4])
                        if len(files) <=4: continue
                        MyImages.write('little_4', files[len(files)-5])
                        print(files[len(files)-5])
                    except Exception as e:
                        print(e)

        if True if MySettings.config['upload'] == "True" else False == True:
            for file in files:
                try:
                    if moveFile.is_alive() or moveFileupload.is_alive():
                        continue
                except:pass
                if read_upload_log(file) == True:
                    moveFileupload = threading.Thread(target=move_to_upload, name='upload_folder', args=[file,])
                    moveFileupload.start()

        if len(files) >= 6 and MyPaths.config['full_size_folder'] != "":
            try:
                if moveFile.is_alive() or moveFileupload.is_alive():
                    continue
            except:pass
            moveFile = threading.Thread(target=move_to_original, name=f'moveFile_{files[0]}', args=[files[0],])
            moveFile.start()

        time.sleep(1)

def log_copy_to_upload(file):
    if os.path.exists(MyPaths.config['kamera_folder'] + "/copy_to_upload.log") == False:
        with open(MyPaths.config['kamera_folder'] + "/copy_to_upload.log", 'w+') as f:
            f.close()

    with open(MyPaths.config['kamera_folder'] + "/copy_to_upload.log", 'a+') as f:
        f.write(file + '\n')
        f.close()

def read_upload_log(file):
    if os.path.exists(MyPaths.config['kamera_folder'] + "/copy_to_upload.log") == False:
        with open(MyPaths.config['kamera_folder'] + "/copy_to_upload.log", 'w+') as f:
            f.close()

    with open(MyPaths.config['kamera_folder'] + "/copy_to_upload.log", 'r') as f:
            text = f.read()
            f.close()
    
    if file in text:
        return False
    return True

def move_to_upload(file):
    if os.path.exists(MyPaths.config['upload_folder']) == False:
        os.makedirs(MyPaths.config['upload_folder'])

    try:
        img = Image.open(file)
        
        b = img.width
        h = img.height

        faktor = int(MySettings.config['compressed_width']) / b
        b = int(MySettings.config['compressed_width'])
        h = h * faktor

        filename = file.split("\\")
        filename = filename[len(filename)-1]

        img = img.resize((int(b), int(h)), Image.Resampling.LANCZOS)
        img.save(MyPaths.config['upload_folder'] + "/" + filename, optimize=True, quality=80)

        log_copy_to_upload(file)
    except Exception as e:
        print(e)

def move_to_original(file):
    try:
        if os.path.exists(MyPaths.config['full_size_folder']) == False:
            os.makedirs(MyPaths.config['full_size_folder'])
        shutil.copy(file, MyPaths.config['full_size_folder'])
        os.remove(file)
    except Exception as e:
        print(e)

def start():
    global thread_wait
    thread_wait = False

    UiCore.ui.start_BTN.setStyleSheet('background-color: #84ffc0')
    UiCore.ui.start_BTN.setEnabled(False)

def stop():
    global thread_wait
    thread_wait = True

    UiCore.ui.start_BTN.setStyleSheet('background-color: none')
    UiCore.ui.start_BTN.setEnabled(True)

def ende():
    app.exec()
    global kill
    kill = True

if __name__ == '__main__':
    if MySettings.config['background_img'] == '': MySettings.write('background_img', '1')
    if MySettings.config['upload'] == '': MySettings.write('upload', 'False')
    if MySettings.config['prozent_grosses_bild'] == '': MySettings.write('prozent_grosses_bild', '48')
    if MySettings.config['prozent_kleines_bild'] == '': MySettings.write('prozent_kleines_bild', '24')
    if MySettings.config['prozent_werbung'] == '': MySettings.write('prozent_werbung', '15')
    if MyPaths.config['viewer_path'] == '': MyPaths.write('viewer_path', r'C:/Program Files/Fotobox/Viewer.exe')
    if MyPaths.config['upload_path'] == '': MyPaths.write('upload_path', r'C:/Program Files/Fotobox/FTP-Upload.exe')
    if MySettings.config['compressed_width'] == '': MySettings.write('compressed_width', '2000')

    app = QApplication(sys.argv)

    UiCore = UiCore()

    MyImages.DeletesValue_reg()
    
    watchfolder = threading.Thread(target=watchfolder, args=[], name='watchfolder')
    watchfolder.start()

    sys.exit(ende())