

list1 = list()

colors = ['green', 'black', 'blue', 'purple', 'pink', 'white', 'brown']

stuff = []

print(list1)
print(stuff)
print(colors)

print(colors[0], colors[5])

print(colors[-1], colors[-3], '\n')

more_colors = ['ecru', 'mauve', 'orange', 'navy']

colors.append('scarlet')
colors.append('maroon')
print(colors, '\n')

colors.insert(0, 'avocado green')
print(colors, '\n')

colors.insert(5, 'grey')
print(colors, '\n')

colors.extend(more_colors)
print(colors, '\n')

#  .append(item)   .insert(pos, item)  .extend(list-of-items)

colors[0] = 'red'
print(colors, '\n')

colors[0] = "burnt umber"
print(colors, '\n')

del colors[5]
print(colors, '\n')

c = colors.pop()
print("c:", c)
print(colors, '\n')

c = colors.pop(0)
print("c:", c)
print(colors, '\n')

colors.remove('ecru')
print(colors, '\n')

print(len(colors), '\n')

print(colors[0], colors[5], colors[-1], '\n')

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', 'spam', 'spam', 'toast']

good_food = [f for f in food if f != 'spam']
print(good_food, '\n')

unique_food = set(food)
print(unique_food, '\n')

print(colors, '\n')

print(colors[:5], '\n')  # same as [0:5]

print(colors[4:7], '\n')

actor = "Chris Hemsworth"
print(actor[:5])
print(actor[3:5])
print(actor[-5:])
print(actor[-8:])
print()

for color in colors:
    print(color)
print()

# for VAR ... in ITERABLE:
#     ...

for char in actor:
    print(char.upper())
print()

for i, color in enumerate(colors):
    print(i, color)

print(list(enumerate(colors)))


print(len(colors), min(colors), max(colors), sorted(colors), '\n')

print(colors, '\n')

for color in reversed(colors):
    print(color, end=' ')
print('\n')

rcolors = reversed(colors)
print(rcolors)

enum_colors = enumerate(colors)
print(enum_colors)

print("first loop:")
for color in rcolors:
    print(color)

print("second loop:")
for color in rcolors:
    print(color)

print("done.", '\n')

descriptions = ['Great', 'Lesser', 'Windward', 'Leeward']
places = ['Britain', 'Antilles', 'Islands', 'Islands', 'Things', 'Other', 'Stuff']

for description, place in zip(descriptions, places):
    print(description, place)

print(list(zip(descriptions, places)))

for i in range(10):
    print("I will not hide my teacher's iPad")
print()

# range(stop)  range(start, stop)  range(start, stop, step)

for i in range(1, 11):
    print(i)
print()

for i in range(5, 101, 5):
    print(i, end=', ')
print('\n')





