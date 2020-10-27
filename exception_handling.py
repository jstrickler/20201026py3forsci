import sqlite3

file_name = "DATA/wombats.txt"

try:
    with open(file_name) as file_in:
        pass
except FileNotFoundError as err:
    print("Cannot open file:", err)


colors = ['red', 'blue', 'green']
try:
    print(colors[8])
except IndexError as err:
    print(err)

values = 5.6, 9.1, 3.7, 0.0, "1.23", "ab.c", 8.2, 2.2

for v in values:
    try:
        result = 20 / float(v)
    except ZeroDivisionError as err:
        print(err)
    except (ValueError, TypeError) as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        print(result)
    finally:
        pass # clean resources



