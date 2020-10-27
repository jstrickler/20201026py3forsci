import os
from glob import glob

target_pattern = 'hello*'

found = False
for folder, subfolders, files in os.walk('/Users/jstrick/Desktop'):   #  C:/Users/yourname
    os.chdir(folder)
    target_matches = glob(target_pattern)
    for file_name in files:
        if file_name in target_matches:
            print(os.path.join(folder, file_name))

