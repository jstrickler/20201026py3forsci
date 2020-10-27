
# i = 0
# while i < 3:
#     print(i)
#     i += 1
# print()


while True:
    username = input("Enter username: ")
    if username == 'q':
        break  # exit loop immediately
    if username == '':
        print("Please enter a name")
        continue  # go to top
    print("Hello,", username)


