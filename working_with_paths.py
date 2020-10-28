from datetime import datetime
import os
import sys

FOLDER = "DATA"
FILE = "mary.txt"

file_path = os.path.join(FOLDER, FILE)

print("file path:", file_path)

print(os.path.exists(file_path))

file_size = os.path.getsize(file_path)
print("file size:", file_size)

print("base name:", os.path.basename(file_path))
print("dir name:", os.path.dirname(file_path))
print("abs path:", os.path.abspath(file_path))

print('-' * 60)

for folder, subfolders, file_names in os.walk('.'):
    if '.git' in subfolders:
        subfolders.remove('.git')
    for file_name in file_names:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder, file_name)
            if sys.platform == 'darwin':
                stat_info = os.stat(file_path)
                create_time = datetime.fromtimestamp(stat_info.st_birthtime)
            elif sys.platform == 'win32':
                create_time = datetime.fromtimestamp(os.path.getctime(file_path))
            else:
                create_time = None   # no creation time on Linux

            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            access_time = datetime.fromtimestamp(os.path.getatime(file_path))
            print(create_time, mod_time, access_time, file_path)



