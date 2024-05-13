import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
packages = [""]

target = [Executable(script="Core.py", base="Win32GUI", icon="data/favicon.ico"),Executable(script="FTP-Upload.py", base="Win32GUI", icon="data/favicon.ico"),Executable(script="Print_selphy-cp1500.py", base="Win32GUI", icon="data/favicon.ico"),]

build_exe_options = {
    'include_files': ["data/", "index.html"],
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6", "shiboken6"],
}

# SETUP CX FREEZE
setup(
    name="Core",
    version="1.2.6",
    description="",
    author="Buecherl M.",
    options={"build_exe": build_exe_options},
    executables=target
)