import webview
import webbrowser
from tkinter import messagebox
import tkinter as tk
import sys

SERVER_URL = 'http://192.168.55.83:5050' 

def show_error_message(msg: str):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Yalnyslyk", msg)
    root.destroy()

def start_client():
    try:
        window = webview.create_window(
            'Student Management - Client',
            SERVER_URL,
            width=1400,
            height=900,
            fullscreen=False,
            frameless=False,
            resizable=True
        )
        
        window.events.closed += lambda: sys.exit(0)
        
        webview.start()
    except Exception as e:
        show_error_message(f"Yalnyslyk: {e}")
        webbrowser.open(SERVER_URL)

if __name__ == '__main__':
    start_client()