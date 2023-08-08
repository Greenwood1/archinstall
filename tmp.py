import urllib.request
import socket
import os
from colorama import Fore, Style, init

init(autoreset=True)



def check_motherboard_type():
    if os.path.exists("/sys/firmware/efi"):
        return "UEFI"
    else:
        return "BIOS"
    
    
print (Fore.YELLOW + "Checking the type of motherboard...\n")
motherboard_type = check_motherboard_type()
print(Fore.LIGHTCYAN_EX + "Motherboard Type:", motherboard_type)