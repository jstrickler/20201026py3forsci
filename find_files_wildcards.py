"""
Utilities for finding files.
"""
import sys
import os
from glob import glob
from typing import List


def find_files(start_folder: str, *patterns) -> List[str]:
    """
    Find files matching one or more filename wildcards, beginning in specified folder.

    All files matching all patterns are returned.

    Example:
     find_files('/Users/myname/projects', '*.txt', '*.json', '*.csv')
     find_files('/Users/myname/projects', 'tr*st.asc')

    :param start_folder: Starting folder for search.
    :param patterns: Iterable of patterns
    :return: List of matching files, with paths relative to starting folder
    """
    found = []
    for folder, subfolders, files in os.walk(start_folder):   #  C:/Users/yourname, etc.
        os.chdir(folder)
        for pattern in patterns:
            target_matches = glob(pattern)
            for file_name in files:
                if file_name in target_matches:
                    found.append(os.path.join(folder, file_name))
    return found



if __name__ == '__main__':  # if not imported (i.e., if run directly as a script)
    script_name = sys.argv.pop(0)  # remove script name from argv

    start_dir = sys.argv.pop(0)   # remove and get 2nd element of sys.argv
    patterns = sys.argv   # get all

    found = find_files(start_dir, *patterns)

    for file_path in found:
        print(file_path)


