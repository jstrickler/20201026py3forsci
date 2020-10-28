import lxml.etree as et

doc = et.parse('potus.xml')

root = doc.getroot()  # get top-level element

party_values = []
for president_element in root:
    party_element = president_element.find('party')
    party_text = party_element.text
    party_values.append(party_text)

print(party_values, '\n')

parties = []
for party_element in doc.findall('.//party'):
    parties.append(party_element.text)

print(parties, '\n')
