import psutil 
import os
path_folder = os.path.join(os.path.expanduser("~") , r"C:\Users\Windows\Desktop\project")
folder_name = "cpu,memory,disk"
new_folder = os.path.join(path_folder,folder_name)
try:
    os.makedirs(new_folder)
    print(f'pooshe {new_folder} ba movafaghiat sakhte shod')
except FileExistsError :
    print(f'pooshe {new_folder} az ghabl vojood darad')
memory = psutil.virtual_memory()
print(f'memory percent ==> {memory.percent}%')
cpu = psutil.cpu_percent(interval=1)
print(f'cpu percent ==> {cpu}%')
disk = psutil.disk_usage('/')
disk_gb = disk.free / (1024 ** 3)
print(f'free disk ==> {disk_gb : .2f} GB')
