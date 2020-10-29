#!/usr/bin/env python
#
import numpy as np

a = np.arange(1, 31) # <1>
a.shape = 3, 10 # <2>
print(a)

def spam(value): # <3>
    return value ** 2

b = spam(a) # <4>
print(b)
