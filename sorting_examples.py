fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]



f1 = sorted(fruits)
print("f1:", f1, "\n")

f2 = sorted(fruits, key=str.lower)
print("f2:", f2, "\n")

f3 = sorted(fruits, key=len)
print("f3:", f3, "\n")

def lower_len(e):
    return len(e), e.lower()

f4 = sorted(fruits, key=lower_len)
print("f4:", f4, "\n")

def wacky(e):
    return e[-1]

f5 = sorted(fruits, key=wacky)
print("f5:", f5, "\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print()

def by_dob(p):
    return p[3]

for person in sorted(people, key=by_dob):
    print(person)
print()

def by_name(p):
    return p[1], p[0]

for person in sorted(people, key=by_name):
    print(person)
print()

for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)
print()

