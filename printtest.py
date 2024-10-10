import os
import win32print
import win32ui
from PIL import Image, ImageWin, ImageCms

def saveImageWithICC(img, icc_profile_path):
    if os.path.exists(icc_profile_path):
        # ICC-Profil laden und Bild konvertieren
        icc_input = ImageCms.ImageCmsProfile(icc_profile_path)
        icc_output = ImageCms.createProfile("sRGB")  # Z.B. sRGB oder anderer Drucker-Farbraum
        img = ImageCms.profileToProfile(img, icc_input, icc_output)
        
        # Bild speichern (falls Drucker nur JPEG unterstützt)
        img.save('output_image_with_icc.jpg', 'JPEG')
        print("Bild mit ICC-Profil gespeichert.")
        return img
    else:
        print("ICC-Profil nicht gefunden.")
        return None

def directPrint(img, printer_name):
    try:
        # Druckerkontext öffnen
        hprinter = win32print.OpenPrinter(printer_name)
        hdc = win32ui.CreateDC()
        hdc.CreatePrinterDC(printer_name)

        # Bildgrößen festlegen
        width_px, height_px = img.size
        bmp = img.rotate(90)  # Beispiel für Drehung um 90 Grad
        dib = ImageWin.Dib(bmp)

        # Druckauftrag beginnen
        hdc.StartDoc('Bilddruck')
        hdc.StartPage()

        # Bild auf Drucker zeichnen
        dib.draw(hdc.GetHandleOutput(), (0, 0, width_px, height_px))

        # Druckauftrag beenden
        hdc.EndPage()
        hdc.EndDoc()

        # Druckerkontext schließen
        hdc.DeleteDC()
        win32print.ClosePrinter(hprinter)

        print(f"Bild erfolgreich an den Drucker {printer_name} gesendet.")
    
    except Exception as e:
        print(f"Fehler beim Drucken: {e}")

def printImageWithICC(img, icc_profile_path, printer_name):
    # Schritt 1: Bild mit ICC-Profil speichern/konvertieren
    img_with_icc = saveImageWithICC(img, icc_profile_path)
    
    # Schritt 2: Direktdruck auf den angegebenen Drucker
    if img_with_icc is not None:
        directPrint(img_with_icc, printer_name)

if __name__ == "__main__":
    # Beispielbild laden
    img = Image.open(r"C:\Users\b_m21\Downloads\DaniLaura\u\Feuerwehrball_2023_198.jpg")

    # ICC-Profilpfad
    icc_profile_path = os.path.abspath(r"data/CanonSelphyCP1500 - P RP108 - F288-v2.icc")  # Hier den Pfad zum ICC-Profil anpassen

    # Name deines Druckers (z.B. "SELPHY CP1500")
    printer_name = "Canon SELPHY CP1500"

    # Drucken ohne Benutzerinteraktion
    printImageWithICC(img, icc_profile_path, printer_name)
