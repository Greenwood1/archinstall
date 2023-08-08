import urllib.request
import socket
import os
import subprocess
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
    
def kb_to_gb(kilobytes):
    gigabytes = kilobytes / (1024 * 1024)  # 1 GB = 1024 MB = 1024 * 1024 KB
    return round(gigabytes)

command_output = subprocess.check_output(['cat', '/proc/meminfo'], universal_newlines=True)

mem_total_line = next(line for line in command_output.split('\n') if line.startswith('MemTotal:'))

mem_total_kb = int(mem_total_line.split()[1])

###########################################################
#
# Temporary launch of the functions below  
#
###########################################################

print (Fore.YELLOW + "Checking the type of motherboard...\n")
motherboard_type = check_motherboard_type()
print(Fore.MAGENTA + "Motherboard Type:", motherboard_type)

mem_total_gb = kb_to_gb(mem_total_kb)
print(f"Total Memory: {mem_total_kb} KB = {mem_total_gb} GB")

