import sys
import os
from cx_Freeze import setup, Executable

# Build Optionen    
packages = ["os", "sys", "PySide6", "PyQt6", "pathlib", "time", "screeninfo", "threading", "PIL", "keyboard", "signal", "configobj", "ftplib", "watchdog", "logging"]
excludes = []
include_files = ["data/", "config.cfg", "platforms/"]

build_exe_options = dict(packages=packages, excludes=excludes, include_files=include_files)

# Ziel
base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(script="FotoboxViewer.py", base=base, icon="data/favicon.ico")

# Setup CX Freez
setup( 
    name = "FotoboxViewer",
    version = "1.1",
    description = "FotoboxViewer",
    options = {'build_exe' : build_exe_options},
    executables = [target]
    )