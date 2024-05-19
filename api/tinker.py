import tkinter as tk
from tkinter import filedialog
from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        print(file_path)
        self.wfile.write(file_path.encode())
        return file_path