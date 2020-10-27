import json

d1 = dict()  # empty dict
print(d1)

d2 = {'red': 5, 'purple': 18, 'chartreuse': 3}
print(d2)

d3 = {}  # empty dict

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports['YYZ'])
print(airports['IAD'])
print(len(airports))
airports['DCA'] = "National (Reagan)"

print(airports, '\n')

airports['LAX'] = "Los Angeles International"

with open('airports.json', 'w') as json_out:
    json.dump(airports, json_out)

with open('airports.json', 'r') as json_in:
    ja = json.load(json_in)

print("ja:", ja)
print(ja['LAX'], ja['EWR'])

print(airports.get('XXX'))
print(airports.get('XXX', 'NOT FOUND'))

del airports['MCO']

print(airports, '\n')

for k in 'LAX', 'MCO', 'HEL', 'RIC', 'RDU':
    print(k, k in airports)

print(airports.keys())
print(airports.values())
print()

#   key,   value  in  dict.items()
for code, name in airports.items():
    print(code, name)
print()











