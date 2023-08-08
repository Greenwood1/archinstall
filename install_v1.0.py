import urllib.request
import socket
import os
from colorama import Fore, Style, init

init(autoreset=True)

def check_internet_connection():
    print(Fore.YELLOW + "Check the Internet connection...")
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except (urllib.error.URLError, socket.timeout):
        return False
    

def check_motherboard_type():
    if os.path.exists("/sys/firmware/efi"):
        return "UEFI"
    else:
        return "BIOS"
    
###########################################################
#
# Temporary launch of the functions below  
#
###########################################################

print (Fore.YELLOW + "Checking the type of motherboard...\n")
motherboard_type = check_motherboard_type()
print(Fore.MAGENTA + "Motherboard Type:", motherboard_type)

