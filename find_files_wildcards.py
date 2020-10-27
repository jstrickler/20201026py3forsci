import sys
import os
from glob import glob


def find_files(start_folder, *patterns):
    found = []
    for folder, subfolders, files in os.walk(start_folder):   #  C:/Users/yourname, etc.
        os.chdir(folder)
        for pattern in patterns:
            target_matches = glob(pattern)
            for file_name in files:
                if file_name in target_matches:
                    found.append(os.path.join(folder, file_name))
    return found

def find_files(start_folders, patterns):
    pass



#  find_files('/Users/jstrick', '*.txt', '*.json', '*.csv')
#  find_files('/Users/jstrick', '*.txt')
#  find_files('/Users/jstrick')

# TARGET_FOLDER = sys.argv.pop(1)   # first arg on command line
# TARGET_PATTERN = sys.argv.pop(1)  # second arg on command line

