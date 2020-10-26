
actor = "Chris Hemsworth"

print(actor)

print(type(actor), len(actor))

print(actor.upper())
print(actor.lower())
print(actor.count('h'))
print(actor.lower().count('h'))

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print(actor.replace('Chris', 'Liam'))

print(actor.find('is'))
print(actor.index('is'))

s = "       Guido is the creator of Python       "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "uidcaatoGuido is the creator of Pythonodctaiuiuiui"
print("|" + s.lstrip("acdiotu") + "|")
print("|" + s.rstrip("acdiotu") + "|")
print("|" + s.strip("acdiotu") + "|")
print()

raw_data = "wombat:tractor:hazelnut:marionberry"
words = raw_data.split(':')
print(words)

phrase = "I      have\t\tjust\tbegun to             fight"
words = phrase.split()
print(words)



