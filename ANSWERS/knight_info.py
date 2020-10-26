#!/usr/bin/env python

import sys
from knight_old import Knight

for name in sys.argv[1:]:
    k = Knight(name)
    print("Name: {} {}".format(k.title, name))
    print("Favorite Color:", k.color)
    print()
