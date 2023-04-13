import sys, os
import threading
import glob
import time
import subprocess
import shutil
from PIL import Image

import reg_config
myimages_schlüssel =('big_1', 'little_1', 'little_2', 'little_3', 'little_4')
mypaths_schlüssel =('upload_folder', 'kamera_folder', 'viewer_path', 'upload_path', 'full_size_folder')
mysettings_schlüssel =('upload', 'prozent_grosses_bild', 'prozent_kleines_bild', 'prozent_werbung', 'background_img', 'compressed_width')
mypictrs_schlüssel =('ftp_host', 'ftp_user', 'ftp_password', 'galerie_folder')

MyImages = reg_config.My_Config('Images', myimages_schlüssel)
MyPaths = reg_config.My_Config('Paths', mypaths_schlüssel)
MySettings = reg_config.My_Config('Settings', mysettings_schlüssel)
MyPictrs = reg_config.My_Config('Pictrs', mypictrs_schlüssel)

from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_core import Ui_Core

class UiCore(QMainWindow):
    def __init__(self):
        super(UiCore, self).__init__()
        self.ui = Ui_Core()
        self.ui.setupUi(self)
        # self.setWindowIcon(windowIcon)

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

        self.show()

    def openPGM(self):
        res = subprocess.Popen(MyPaths.config['viewer_path'])

        if True if MySettings.config['upload'] == "True" else False == True:
            res = subprocess.Popen(MyPaths.config['upload_path'])

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
    while True:
        time.sleep(1)
        files = glob.glob(MyPaths.config['kamera_folder'] + r'\\*.jpg')
        files = sorted(files, key=os.path.getmtime)

        try:
            MyImages.write('big_1', files[len(files)-1])
            if len(files) <=1: continue
            MyImages.write('little_1', files[len(files)-2])
            if len(files) <=2: continue
            MyImages.write('little_2', files[len(files)-3])
            if len(files) <=3: continue
            MyImages.write('little_3', files[len(files)-4])
            if len(files) <=4: continue
            MyImages.write('little_4', files[len(files)-5])
        except Exception as e:
            print(e)

        if len(files) >= 6 and MyPaths.config['full_size_folder'] != "":
            try:
                if moveFile.is_alive():
                    continue
            except:pass
            moveFile = threading.Thread(target=move_to_new_folder, name=f'moveFile_{files[0]}', args=[files[0],], daemon=False)
            moveFile.start()
    
def move_to_new_folder(file):
    if True if MySettings.config['upload'] == "True" else False == True:
        if os.path.exists(MyPaths.config['upload_folder']) == False:
            os.makedirs(MyPaths.config['upload_folder'])

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

    if os.path.exists(MyPaths.config['full_size_folder']) == False:
        os.makedirs(MyPaths.config['full_size_folder'])
    shutil.move(file, MyPaths.config['full_size_folder'])

if __name__ == '__main__':
    if MySettings.config['background_img'] == '': MySettings.write('background_img', '1')
    if MySettings.config['upload'] == '': MySettings.write('upload', 'False')
    if MySettings.config['prozent_grosses_bild'] == '': MySettings.write('prozent_grosses_bild', '0.330')
    if MySettings.config['prozent_kleines_bild'] == '': MySettings.write('prozent_kleines_bild', '0.15')
    if MySettings.config['prozent_werbung'] == '': MySettings.write('prozent_werbung', '0.1')
    if MyPaths.config['viewer_path'] == '': MyPaths.write('viewer_path', 'C:/Program Files/Fotobox/Viewer.exe')
    if MyPaths.config['upload_path'] == '': MyPaths.write('upload_path', 'C:/Program Files/Fotobox/FTP-Upload.exe')
    if MySettings.config['compressed_width'] == '': MySettings.write('compressed_width', '2000')

    app = QApplication(sys.argv)

    UiCore = UiCore()

    watchfolder = threading.Thread(target=watchfolder, args=[], name='watchfolder', daemon=False)
    watchfolder.start()

    sys.exit(app.exec())