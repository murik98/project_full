import subprocess
import os
import sys
import psutil
from tkinter import Tk, Button, messagebox, Label
import atexit
import socket  

class DjangoServer:
    def __init__(self):
        self.PROJECT_PATH = r'C:\Users\222204\Documents\proj_full\student_management'
        self.SERVER_IP = '192.168.55.83'
        self.SERVER_PORT = 5050
        self.process = None
        self.is_daemon = False
        self.setup_ui()
        atexit.register(self.cleanup)
        self.ensure_static_files()

    def ensure_static_files(self):
        static_dir = os.path.join(self.PROJECT_PATH, 'static')
        if not os.path.exists(static_dir):
            os.makedirs(static_dir, exist_ok=True)
            self.run_manage_command('collectstatic --noinput')

    def run_manage_command(self, command):
        try:
            subprocess.run(
                f'python manage.py {command}',
                cwd=self.PROJECT_PATH,
                shell=True,
                check=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Yalnyslyk", f"Yalnyslyk: {e}")

    def setup_ui(self):
        self.root = Tk()
        self.root.title("Django serwer dolandyrys")
        
        self.status_label = Label(self.root, text="Serwer duruzylan", font=("Arial", 12))
        self.status_label.pack(pady=10)
        
        self.btn = Button(
            self.root, 
            text="Serweri islet", 
            command=self.toggle_server,
            width=20,
            height=3,
            bg="#e0e0e0"
        )
        self.btn.pack(padx=30, pady=30)
        
        if self.is_server_running():
            self.update_ui(True)

    def is_server_running(self):
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                cmd = ' '.join(proc.info['cmdline'] or [])
                if 'manage.py' in cmd and f"{self.SERVER_IP}:{self.SERVER_PORT}" in cmd:
                    self.process = proc
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return False

    def kill_process_on_port(self):
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                cmd = ' '.join(proc.info['cmdline'] or [])
                if 'manage.py' in cmd and f"{self.SERVER_IP}:{self.SERVER_PORT}" in cmd:
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    def is_port_in_use(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((self.SERVER_IP, self.SERVER_PORT))
                return False
            except socket.error:
                return True

    def start_server(self):
        try:
            if self.is_port_in_use():
                messagebox.showerror("Yalnyslyk", f"Port {self.SERVER_PORT} ugrady isletilýär. Başga port saýlaň ýa-da prosesi ýatyryň.")
                return

            os.chdir(self.PROJECT_PATH)
            self.process = subprocess.Popen(
                [
                    'python', 'manage.py', 'runserver',
                    f'{self.SERVER_IP}:{self.SERVER_PORT}',
                    '--noreload',
                    '--insecure'  
                ],
                creationflags=subprocess.CREATE_NO_WINDOW,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.update_ui(True)
            messagebox.showinfo("Status", "Serwer isledildi!")
        except FileNotFoundError:
            messagebox.showerror("Yalnyslyk", "manage.py faýly tapylmady. Proýektiň ýoluny barlaň.")
        except PermissionError:
            messagebox.showerror("Yalnyslyk", "Rugsat ýok. Programmany administrator hökmünde işlediň.")
        except Exception as e:
            messagebox.showerror("Yalnyslyk", f"Serweri işletmekde ýalňyşlyk: {str(e)}")

    def stop_server(self):
        if self.process:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
        self.kill_process_on_port()
        self.process = None
        self.update_ui(False)
        messagebox.showinfo("Status", "Serwer duruzyldy")

    def update_ui(self, is_running):
        self.is_daemon = is_running
        self.btn.config(
            text="Serweri sakla" if is_running else "Serweri islet",
            bg="#ffcccc" if is_running else "#e0e0e0"
        )
        self.status_label.config(text="Serwer isleyar" if is_running else "Serwer islanok")

    def toggle_server(self):
        if self.is_daemon:
            self.stop_server()
        else:
            self.start_server()

    def cleanup(self):
        self.stop_server()
        self.root.destroy()

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.cleanup)
        self.root.mainloop()

if __name__ == '__main__':
    server = DjangoServer()
    server.run()