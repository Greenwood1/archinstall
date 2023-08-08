import urllib.request
import socket

def check_internet_connection():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except (urllib.error.URLError, socket.timeout):
        return False

if check_internet_connection():
    print("Internet connection is available.")
else:
    print("No Internet access.")