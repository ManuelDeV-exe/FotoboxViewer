import configobj
import os,sys
import pathlib

def read_config():
    tressor_data = {}

    config_file = configobj.ConfigObj("config.cfg")
    config_file.encoding = "utf-8"

    global bilder_speicherplatz
    tressor_data["bilder_pfad"] = str(pathlib.Path(config_file["Pfade"]["bilder_pfad"]))

    tressor_data["ftp_host"] = config_file["Pictrs"]["ftp_host"]
    tressor_data["ftp_user"] = config_file["Pictrs"]["ftp_user"]
    tressor_data["ftp_password"] = config_file["Pictrs"]["ftp_password"]
    tressor_data["ftp_port"] = config_file["Pictrs"]["ftp_port"]
    tressor_data["galerie"] = config_file["Pictrs"]["galerie"]

    tressor_data["prozent_grosses_bild"] = config_file["Einstellungen"]["prozent_grosses_bild"]
    tressor_data["prozent_kleines_bild"] = config_file["Einstellungen"]["prozent_kleines_bild"]
    tressor_data["prozent_werbung"] = config_file["Einstellungen"]["prozent_werbung"]

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

    config_file["Einstellungen"] = {}
    config_file["prozent_grosses_bild"] = ""
    config_file["prozent_kleines_bild"] = ""
    config_file["prozent_werbung"] = ""
    config_file.write()
