pyinstaller --noconfirm --onefile --windowed --icon "P:/Python/FotoboxViewer/FotoboxViewer/data/favicon.ico"  "P:/Python/FotoboxViewer/FotoboxViewer/Viewer.py"
pyinstaller --noconfirm --onefile --icon "P:/Python/FotoboxViewer/FotoboxViewer/data/favicon.ico"  "P:/Python/FotoboxViewer/FotoboxViewer/php_server.py"
python setup_Core.py build 

PAUSE