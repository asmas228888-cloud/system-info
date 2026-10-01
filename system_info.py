import platform
import os
import socket
import sys
import shutil
import json
from datetime import datetime

system = platform.system()
if system == "Windows":
    os_name = "Windows"
elif system == "Linux":
    os_name = "Linux"
elif system == "Darwin":
    os_name = "macOS"

os_info = {
    "name": os_name,
    "version": platform.version(),
    "release": platform.release(),
    "architecture": platform.machine(),
    "CPU": platform.processor()
}

computer_info = {
    "computer_name": socket.gethostname(),
    "user_name": os.getlogin(),
    "python_version": sys.version.split()[0],
    "current_directory": os.getcwd()
}

cpu_info = {
    "threads": os.cpu_count()
}

disk = shutil.disk_usage(os.getcwd())

disk_info = {
    "total_bytes": disk.total,
    "used_bytes": disk.used,
    "free_bytes": disk.free
}

try:
    ip_address = socket.gethostbyname(socket.gethostname())
except:
    ip_address = "ip_address not defined"

network_info = {
    "hostname": socket.gethostname(),
    "ip_address": ip_address
}

data = {
    "REQUEST TIME": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),

    "OS name": os_info["name"],
    "OS version": os_info["version"],
    "OS release": os_info["release"],
    "OS architecture": os_info["architecture"],
    "CPU": os_info["CPU"],

    "computer name": computer_info["computer_name"],
    "user name": computer_info["user_name"],
    "python version": computer_info["python_version"],
    "current directory": computer_info["current_directory"],

    "threads": cpu_info["threads"],

    "disk total bytes": disk_info["total_bytes"],
    "disk used bytes": disk_info["used_bytes"],
    "disk free bytes": disk_info["free_bytes"],

    "hostname": network_info["hostname"],
    "IP address": network_info["ip_address"]
}

json_name = "system_info.json"

with open(json_name, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Information has been collected.")
print("json-file was created:", os.path.abspath(json_name))