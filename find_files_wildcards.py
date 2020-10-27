import sys
import os
from glob import glob

TARGET_FOLDER = sys.argv.pop(1)   # first arg on command line
TARGET_PATTERN = sys.argv.pop(1)  # second arg on command line

found = False
for folder, subfolders, files in os.walk(TARGET_FOLDER):   #  C:/Users/yourname, etc.
    os.chdir(folder)
    target_matches = glob(TARGET_PATTERN)
    for file_name in files:
        if file_name in target_matches:
            print(os.path.join(folder, file_name))

