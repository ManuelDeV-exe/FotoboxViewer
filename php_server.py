import os
import subprocess
import reg_config
import shutil
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote
import mimetypes

mypaths_schlüssel = ('kamera_folder',)
MyPaths = reg_config.My_Config('Paths', mypaths_schlüssel)

kamera_folder = MyPaths.config['kamera_folder'] + "\\"
path = kamera_folder

if os.path.exists(path+ "\data"): pass
else: shutil.copytree(os.path.abspath("data"), path + "\data")

class PHPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # URL-decode and calculate the absolute path based on the Webhosting directory
        requested_path = unquote(self.path[1:])
        full_path = os.path.join(path, requested_path)  # Ensure all paths are relative to the Webhosting directory

        if requested_path.endswith(".php"):
            self.handle_php_request(full_path)
        else:
            self.handle_file_request(full_path)

    def handle_php_request(self, script_path):
        php_path = os.path.abspath(os.path.join(path, "data/php/php.exe"))  # Path to the PHP interpreter

        if not os.path.isfile(php_path):
            self.send_error(500, 'PHP-Interpreter nicht gefunden')
            return

        if not os.path.isfile(script_path):
            self.send_error(404, 'PHP-Datei nicht gefunden')
            return

        # Execute the PHP script
        try:
            process = subprocess.Popen([php_path, script_path], stdout=subprocess.PIPE)
            output, _ = process.communicate()

            # Send the response status code
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send the output of the PHP script as the response
            self.wfile.write(output)
        except Exception as e:
            self.send_error(500, f'Serverfehler: {str(e)}')

    def handle_file_request(self, file_path):
        try:
            # Determine the content type
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type is None:
                mime_type = 'application/octet-stream'

            # Open the file requested by the client
            with open(file_path, 'rb') as file:
                # Send the response status code
                self.send_response(200)
                self.send_header('Content-type', mime_type)
                self.end_headers()

                # Send the content of the file
                self.wfile.write(file.read())
        except IOError:
            self.send_error(404, f'Datei nicht gefunden: {self.path}')

def run(server_class=HTTPServer, handler_class=PHPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starte PHP-Server auf Port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    print("start")
    os.chdir(path)
    print("running")
    run()

