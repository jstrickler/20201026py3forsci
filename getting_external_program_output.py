import os

with os.popen("netstat -an") as netstat_in:
    for raw_line in netstat_in:
        if "ESTAB" in raw_line:
            line = raw_line.rstrip()
            print(line)
