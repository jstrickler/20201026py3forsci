
#  file_obj = open("filename", "mode")

#  MODE: "r"  "w"  "a"  "x" "rb" "wb" "ab" "xb"

# with EXPR:
# with open("filename", "mode") as file_obj:
# with EXPR as VARIABLE:

with open('DATA/mary.txt', 'r') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip() #  line = raw_line[:-1]    raw_line.pop()
        print(line)
print('-' * 60)

with open('DATA/mary.txt', "r") as mary_in:
    contents = mary_in.read()  # read entire file into string
    print("RAW:")
    print(repr(contents))  # repr gives "raw" view of string (or anything)
    print("NORMAL:")
    print(contents)
print('-' * 60)

with open('DATA/mary.txt', "r") as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    with open('upper_mary.txt', 'w') as upper_mary_out:
        for line in mary_in:
            upper_mary_out.write(line.upper())


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitnames.txt', 'x') as fruit_out:
    for fruit in fruits:
        fruit_out.write(fruit + '\n')    #   f"{fruit}\n"




