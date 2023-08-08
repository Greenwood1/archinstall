import urllib.request
import socket
import os
from colorama import Fore, Style, init

init(autoreset=True)



def kb_to_gb(kilobytes):
    gigabytes = kilobytes / (1024 * 1024)  # 1 GB = 1024 MB = 1024 * 1024 KB
    return round(gigabytes)

# Виклик функції
kilobytes = 8046656
gigabytes = kb_to_gb(kilobytes)
print(f"{kilobytes} KB = {gigabytes} GB")