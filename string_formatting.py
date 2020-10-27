
x = 5
y = 239039

print(x, y)

print("{} {}".format(x, y))

print("{0} {1}".format(x, y))

print("{1} {0}".format(x, y))

print("{0:8d} {1:8d}".format(x, y))
print("{1:8d} {0:8d}".format(x, y))

print("{:8d} {:8d}".format(x, y))

print(f"{x:8d} {y:8d}")

x = ['red', 'blue', 'green']

print(x)

print(' '.join(x))

print(x[0])

print(x)

name = 'Bob'

print(name.upper().lower().title().count('o') * 10)
