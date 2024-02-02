from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ["shiboken6"], 'excludes': [], 'include_files': ["data/", "index.html"],}

base = 'Win32Gui'

executables = [
    Executable('Core.py', base=base, icon=r"data/favicon.ico"),
    Executable('Viewer.py', base=base, icon=r"data/favicon.ico"),
    Executable('FTP-Upload.py', base=base, icon=r"data/favicon.ico")
]

setup(name='FotoBox',
      version = '1.5.0',
      description = 'Fotobox-Kernal',
      options = {'build_exe': build_options},
      executables = executables)
