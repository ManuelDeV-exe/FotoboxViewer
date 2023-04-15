import winreg

class My_Config():
    def __init__(self, key_name, key_list):
        self.settings_folder = winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"Software\\Fotobox\\{key_name}")
        self.settings_key = key_list
        self.config = {}

        self.first_running()

    def first_running(self):
        for key in self.settings_key:
            try:
                winreg.QueryValueEx(self.settings_folder, key)
            except:
                winreg.SetValueEx(self.settings_folder, str(key), 0, winreg.REG_SZ, "")

        self.read()

    def write(self, key, value):
        winreg.SetValueEx(self.settings_folder, str(key), 0, winreg.REG_SZ, str(value))
        self.config[str(key)] = str(value)

    def read(self):
        for key in self.settings_key:
            self.config[str(key)] = winreg.QueryValueEx(self.settings_folder, key)[0]
    
    def DeletesValue_reg(self):
        for key in self.settings_key:
            winreg.SetValueEx(self.settings_folder, str(key), 0, winreg.REG_SZ, str(''))

    def read_new(self):
        for key in self.settings_key:
            self.config[str(key)] = winreg.QueryValueEx(self.settings_folder, key)[0]

    
