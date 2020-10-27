
# y = "yellow"

x = 100  # GLOBAL variable

def spam():
    y = 42  # LOCAL variable
    print("In spam(): x is", x)
    print("In spam(): y is", y)

spam()

# print("in main: y is", y)


