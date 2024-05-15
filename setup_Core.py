import sys
import os
import PySide6
from cx_Freeze import setup, Executable

target = [Executable(script="Core.py", base="Win32GUI", icon="data/favicon.ico"),
          Executable(script="FTP-Upload.py", base="Win32GUI", icon="data/favicon.ico"),
          Executable(script="Print_selphy_cp1500.py", base="Win32GUI", icon="data/favicon.ico"),
          ]

build_exe_options = {
    "include_files": ["data/", "index.html"],
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6"],
    "packages": ["win32print", "win32ui"],
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