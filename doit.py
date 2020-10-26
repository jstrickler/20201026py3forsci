import sys

print(sys.argv)

print("argv[1]", sys.argv[1])
print("argv[2]", sys.argv[2])

value = int(sys.argv[1])
# value = sys.argv[1]

print(value * 10)
