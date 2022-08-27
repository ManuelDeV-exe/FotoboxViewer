import sys
import os
from cx_Freeze import setup, Executable

# Build Optionen
build_exe_options = dict(packages = ["os", "sys", "PySide6", "PyQt6", "pathlib", "time", "screeninfo", "threading", "PIL", "configparser", "keyboard", "signal"], excludes = [], include_files = ["data/", "config.cfg"])

# Ziel
target = Executable(
    script="FotoboxViewer.py",
    base="Win32GUI",
    icon="data/favicon.ico"
)

# Setup CX Freez
setup( 
    name = "FotoboxViewer",
    version = "0.2",
    description = "FotoboxViewer",
    author= "Manuel Bücherl",
    options = {'build_exe' : build_exe_options},
    executables = [target]
    )