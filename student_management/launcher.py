import subprocess
import threading
import time
import webview
import os
import sys
import webbrowser
import socket
from tkinter import messagebox
import tkinter as tk

PROJECT_PATH = r'D:\proj_09.05\student_management'

django_process = None

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0  

def run_django():
    global django_process
    os.chdir(PROJECT_PATH)
    try:
        startupinfo = None
        if sys.platform == 'win32':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        django_process = subprocess.Popen(
            ['python', 'manage.py', 'runserver', '--noreload'],
            startupinfo=startupinfo,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
        )
        django_process.wait()  
    except Exception as e:
        print(f"Serwer isletmekde yalnyslyk: {e}")
        show_error_message(f"Serwer isledilmedi: {e}")
        sys.exit(1)

def show_error_message(msg: str):
    root = tk.Tk()
    root.withdraw() 
    messagebox.showerror("Yalnyslyk", msg)
    root.destroy()

def on_closed():
    if django_process:
        django_process.terminate()  
    os._exit(0)

def start_app():
    if is_port_in_use(8000):
        show_error_message("8000 port bos dal! Beyleki Django serwerli ocurin.")
        sys.exit(1)

    django_thread = threading.Thread(target=run_django, daemon=True)
    django_thread.start()

    time.sleep(3)

    try:
        window = webview.create_window(
            'Student Management',
            'http://127.0.0.1:8000',
            width=1400,
            height=900,
            fullscreen=False,
            frameless=False,
            resizable=True,
            easy_drag=True,
        )

        window.events.closed += on_closed

        webview.start()
    except Exception as e:
        show_error_message(f"Yalnyslyk: {e}")
        webbrowser.open('http://127.0.0.1:8000')

if __name__ == '__main__':
    start_app()