import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ["data/", "index.html"]
packages = [""]

target = [Executable(script="Core.py",base="Win32GUI",icon="data/favicon.ico"), Executable(script="FTP-Upload.py",base="Win32GUI",icon="data/favicon.ico")]

# SETUP CX FREEZE
setup(
    name="Core",
    version="1.2.3",
    description="",
    author="Buecherl M.",
    options={'build_exe': {'include_files': files}},
    executables=target
)