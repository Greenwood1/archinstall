import urllib.request
import socket

def check_internet_connection():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except (urllib.error.URLError, socket.timeout):
        return False
 
def get_motherboard_type():
    while True:
        choice = input("Select motherboard type (BIOS/MBR or UEFI/GPT): ").strip().lower()
        if choice in ["bios", "mbr", "uefi", "gpt"]:
            return choice
        else:
            print("Invalid choice. Please enter 'bios', 'mbr', 'uefi', or 'gpt'.")
            
def get_swap_info():
    choice = input("Do you want to create a SWAP file? (yes/no): ").strip().lower()
    if choice == "yes":
        size = input("Enter SWAP file size in GB: ")
        return f"create_swap {size}"
    else:
        return "no_swap"
    
def get_root_partition_size():
    choice = input("Enter root partition size in GB or choose 'use all remaining space': ").strip().lower()
    if choice == "use all remaining space":
        return choice
    else:
        return f"{choice}G"

if check_internet_connection():
    print("Internet connection is available.")
else:
    print("No Internet access.")
    
motherboard_type = get_motherboard_type()
swap_info = get_swap_info()
root_partition_size = get_root_partition_size()

print("Motherboard Type:", motherboard_type)
print("SWAP Info:", swap_info)
print("Root Partition Size:", root_partition_size)
