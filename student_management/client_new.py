import webview
import requests
from tkinter import messagebox
import tkinter as tk
import sys
import time

SERVER_IP = '192.168.55.83'
SERVER_PORT = 5050
SERVER_URL = f'http://{SERVER_IP}:{SERVER_PORT}'
CUSTOM_HEADERS = {
    'User-Agent': 'StudentManagementWebView/1.0',
    'X-App-Access': 'SECRET_KEY_123'
}

def check_server():
    try:
        response = requests.get(
            f'{SERVER_URL}/healthcheck/',
            headers=CUSTOM_HEADERS,
            timeout=5
        )
        return response.status_code == 200
    except:
        return False

def show_error(msg):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Yalnyslyk", msg)
    root.destroy()
    sys.exit(1)

def main():
    for _ in range(10):
        if check_server():
            break
        time.sleep(1)
    else:
        show_error("Serwer jogap berenok")
    
    try:
        window = webview.create_window(
            title='Student Management System',
            url=SERVER_URL,
            width=1400,
            height=900,
            min_size=(1024, 768),
            confirm_close=True,
            http_headers=CUSTOM_HEADERS
        )
        
        def on_closing():
            if not window.closed:
                show_error("Close operation blocked!")
        
        window.events.closing += on_closing
        
        webview.start(
            debug=False,
            http_server=True,
            storage_path='./app_data'
        )
    
    except Exception as e:
        show_error(str(e))

if __name__ == '__main__':
    main()