import sys, os
import time
import glob
import win32print
import win32ui
import threading
import reg_config
import my_mysql as my_SQL

import PySide6
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from PIL import Image, ImageWin

logo_Pfad = os.path.abspath('data/icon.png')

config_schlüssel = ('mysql_host', 'mysql_username', 'mysql_password')
MyConfig = reg_config.My_Config('Print_Config', config_schlüssel)
MyPaths = reg_config.My_Config('Paths', ('kamera_folder',))

mysql_data = {}
mysql_data["mysql_host"] = MyConfig.config['mysql_host']
mysql_data["mysql_username"] = MyConfig.config['mysql_username']
mysql_data["mysql_password"] = MyConfig.config['mysql_password']
mysql_data["mysql_database"] = "ImageViewer"
mysql_data["mysql_sql_tabel"] = "DatenBank"

mysql = my_SQL.new_MySql_object(mysql_data)
if mysql.verbunden == False:print("Ferhler, nicht verbunden.")
mysql.read_all_data()

from ui_FTP_starten import Ui_FTP_starten

thread_wait = True

class FTP_starten(QMainWindow):
    def __init__(self):
        super(FTP_starten, self).__init__()
        self.ui = Ui_FTP_starten()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(str(logo_Pfad)))

        self.setWindowTitle('Print_selphy-cp1500')
        self.ui.label_6.setText('Printservice starten')

        self.ui.start_BTN.clicked.connect(start)
        self.ui.stop_BTN.clicked.connect(stop)

        self.show()


def findImg(filename):
    pathlist = glob.glob(MyPaths.config['kamera_folder'] + '/**/*.jpg', recursive=True)

    for path in pathlist:
        if filename in path:
            return path

def CropImage(img, cords, sqlIndex):
    print_img_path = findImg(img)
    im = Image.open(print_img_path)

    width, height = im.size

    faktor_w = width / cords['img_width']
    faktor_h = height / cords['img_height']

    left = cords['img_pos_x'] * faktor_w
    top = cords['img_pos_y'] * faktor_h
    right = (cords['img_pos_x'] + cords['img_pos_width']) * faktor_w
    bottom = (cords['img_pos_y'] + cords['img_pos_heigth']) * faktor_h

    temp_img = im.crop((left, top, right, bottom))

    tmp = printImage(temp_img)
    if tmp == False: return
        
    mysql.delete('index', sqlIndex)
    time.sleep(30)

def printImage(img):
    try:
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
        printer_name = None
        for printer in printers:
            if "SELPHY" in printer[2]:
                printer_name = printer[2]
                break

        if printer_name is None:
            raise ValueError("Kein Samsung Drucker gefunden")

        # Druckerkontext erstellen
        hprinter = win32print.OpenPrinter(printer_name)
        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(printer_name)

        # Größen in mm (Beispiel: 100 mm x 150 mm)
        width_mm = 100
        height_mm = 148

        # Umrechnung in Pixel
        width_px = int(width_mm * 12)
        height_px = int(height_mm * 12)

        # Druckauftrag beginnen
        hDC.StartDoc('printImage')
        hDC.StartPage()

        # Bild laden und auf spezifizierte Größe skalieren
        bmp = img.transpose(Image.ROTATE_90)
        bmp.show()
        dib = ImageWin.Dib(bmp)
        dib.draw(hDC.GetHandleOutput(), (0, 0, width_px, height_px))

        # Druckauftrag beenden
        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()
        win32print.ClosePrinter(hprinter)

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def mainTastk():
    while True:
        if thread_wait:
            continue

        mysql.read_all_data()

        if len(mysql.data) > 0:
            cords = {}
            cords['img_width'] = float(mysql.data[0][1])
            cords['img_height'] = float(mysql.data[0][2])
            cords['img_pos_x'] = float(mysql.data[0][3])
            cords['img_pos_y'] = float(mysql.data[0][4])
            cords['img_pos_width'] = float(mysql.data[0][5])
            cords['img_pos_heigth'] = float(mysql.data[0][6])

            CropImage(mysql.data[0][7], cords, mysql.data[0][0])

        time.sleep(10)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    FTP_starten = FTP_starten()

    Mainthread = threading.Thread(target=mainTastk, args=[], name='Print_selphy-cp1500', daemon=True)
    Mainthread.start()

    sys.exit(app.exec())