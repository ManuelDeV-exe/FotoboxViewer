import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ["platforms/", "data/", "config.cfg"]
packages = [""]

target = Executable(
    script="FotoboxViewer.py",
    base="Win32GUI",
    icon="data/favicon.ico"
)

# SETUP CX FREEZE
setup(
    name="FotoboxViewer",
    version="1.2.1",
    description="",
    author="Buecherl M.",
    options={'build_exe': {'include_files': files}},
    executables=[target]
)