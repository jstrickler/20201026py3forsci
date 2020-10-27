import os

target_file = 'requirements.txt'

found = False
for folder, subfolders, files in os.walk('/Users/jstrick/Desktop'):   #  C:/Users/yourname
    for file_name in files:
        if file_name == target_file:
            print(os.path.join(folder, file_name))
            found = True
            break

    if found:
        break
else:
    print(f"Sorry, {target_file} not found")

