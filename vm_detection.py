import os
import platform
import subprocess

def detect_virtual_machine():
    print("----- VM Detection -----")

    # Method 1: Check system manufacturer
    try:
        output = subprocess.check_output("dmidecode -s system-manufacturer", shell=True).decode().lower()
        if "vmware" in output or "virtualbox" in output or "qemu" in output:
            print("Running inside a Virtual Machine.")
            return
    except:
        pass

    # Method 2: Check CPU virtualization flag
    cpuinfo = ""
    try:
        cpuinfo = open("/proc/cpuinfo").read().lower()
        if "hypervisor" in cpuinfo:
            print("Hypervisor flag detected → VM environment.")
            return
    except:
        pass

    # Method 3: Check platform metadata
    if "virtual" in platform.platform().lower():
        print("VM pattern found in platform data.")
        return

    print("System appears to be running on a physical machine.")

detect_virtual_machine()
