
s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"  # or r'...'  r"""...""" etc

print("Guido's the creator of Python")
print('Guido is the "BDFL" of Python')

print("""Guido's the "BDFL" of Python""")

#  "Guido's the \"BDFL\" of Python"

query = """
select title, artist
from artworks
where title like 'mona lisa'
"""

print(s5)


 # \n \r \t               \b \f

a = 'apple'
b = 'banana'

c1 = a + '-' + b  # too much work
c2 = f'{a}-{b}'  # preferred if few strings
c3 = "-".join([a, b]) # preferred if many strings

print(c1, c2, c3)

