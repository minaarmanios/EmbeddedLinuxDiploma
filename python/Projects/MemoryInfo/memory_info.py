
"""
System Resource Monitor using psutil.

This script retrieves and displays the following system statistics:

1. CPU Usage:
   - Prints the current CPU utilization percentage.

2. Virtual Memory:
   - Total memory in GB.
   - Available memory in GB.
   - Used memory in GB.
   - Memory usage percentage.

3. Disk Memory:
   - Iterates through all disk partitions.
   - For each partition, prints:
       * Device name
       * Total space in GB
       * Available space in GB
       * Used space in GB
       * Disk usage percentage

Dependencies:
- psutil: A cross-platform library for accessing system details and process utilities.

Example:
    CPU Percentage = 15.0%
    total mem = 16.0GB
    available mem = 8.0GB
    used mem = 7.5GB
    mem usage percentage = 47%
    Drive: C:\
    total mem = 256G
    available mem = 100G
    used mem = 140G
    mem usage percentage = 58%
"""

import psutil

#Get Cpu percentage
print(f'CPU Percentage = {psutil.cpu_percent(interval = 1)}%')

#virtual memory statistics
GIGA = 1024**3
vir_memory = psutil.virtual_memory()

print(f'total mem = {vir_memory.total/GIGA}GB')
print(f'available mem = {vir_memory.available/GIGA}GB')
print(f'used mem = {vir_memory.used/GIGA}GB')
print(f'mem usage percentage = {vir_memory.percent}%')

#Disk memory statistics
partions = psutil.disk_partitions()

for partion in partions:
    disk_memory = psutil.disk_usage(partion.mountpoint)
    print(f"Drive:{partion.device}")
    print(f'total mem = {disk_memory.total/GIGA}G')
    print(f'available mem = {disk_memory.free/GIGA}G')
    print(f'used mem = {disk_memory.used/GIGA}G')
    print(f'mem usage percentage = {disk_memory.percent}%')
