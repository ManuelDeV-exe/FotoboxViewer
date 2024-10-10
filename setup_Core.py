import sys
import os
from cx_Freeze import setup, Executable

target = [Executable(script="Core.py", base="Win32GUI", icon="data/favicon.ico"),
          Executable(script="FTP-Upload.py", base="Win32GUI", icon="data/favicon.ico"),
          Executable(script="Print_selphy_cp1500.py", base="Win32GUI", icon="data/favicon.ico"),
          ]

build_exe_options = {
    "include_files": ["data/", "index.html","platforms/", "dist/Viewer.exe", "dist/php_server.exe"],
    "excludes": ["tkinter", "unittest"],
}

# SETUP CX FREEZE
setup(
    name="Core",
    version="1.3.2",
    description="",
    author="Buecherl M.",
    options={"build_exe": build_exe_options},
    executables=target
)