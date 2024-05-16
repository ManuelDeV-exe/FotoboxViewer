import sys, os
import ftplib
import glob

import reg_config

mypaths_schlüssel =('upload_folder', 'kamera_folder', 'viewer_path', 'upload_path')
mypictrs_schlüssel =('ftp_host', 'ftp_user', 'ftp_password', 'galerie_folder')

MyPaths = reg_config.My_Config('Paths', mypaths_schlüssel)
MyPictrs = reg_config.My_Config('Pictrs', mypictrs_schlüssel)

file= r"C:\Users\b_m21\Downloads\data\Feuerwehrball_2023_100.jpg"
def upload_file(file):      
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

    ftp.cwd("data")

    myfile = open(file, 'rb')

    filename = file.split("\\")
    filename = filename[len(filename)-1]

    print(f"Upload start -> {file}")

    ftp.storbinary('STOR ' + filename, myfile)
    ftp.quit()

    print(f"Upload beendet -> {file}")

upload_file(file)