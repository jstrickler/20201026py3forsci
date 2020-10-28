import lxml.etree as et
import csv

root = et.Element('presidents')

with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    for term, first_name, last_name, birthplace, birth_state, party in rdr:
        p = et.SubElement(root, 'president', term_number=term)
        fn = et.SubElement(p, 'firstname')
        fn.text = first_name
        et.SubElement(p, 'lastname').text = last_name
        et.SubElement(p, 'birthplace').text = birthplace
        et.SubElement(p, 'birthstate').text = birth_state
        et.SubElement(p, 'party').text = party



print(et.tostring(root, pretty_print=True, xml_declaration=True).decode())

doc = et.ElementTree(root)

doc.write('potus.xml', pretty_print=True, xml_declaration=True)

