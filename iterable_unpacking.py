

person = 'Bill', 'Gates', 'Microsoft', '1954-10-28'

first_name, last_name, product, dob = person   # unpacking!


colors = ['purple', 'puce', 'mauve']

for i, color in enumerate(colors):
    # i, color = next(...)
    print(i, color)
print()

print(list(enumerate(colors)))

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)
