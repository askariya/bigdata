#!/usr/bin/env python
#reducer.py

import string
import sys

prev_key = None
for line in sys.stdin:
    line = line.rstrip()
    firstchar, word = line.split('.') # split and assign to 2 different variables

    if prev_key == None:
        prev_key=word
        continue
    if prev_key == word:
        continue
    if prev_key != word:
        print '%s' %(prev_key)
        prev_key = word
print '%s' %(prev_key)
