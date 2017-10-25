#!/usr/bin/env python
#mapper.py

import sys
import random
num = 0
for line in sys.stdin:
    line = line.strip() # remove all whitespace at the front and the end of each of the lines
    randomint = random.randint(0,9) # pick a random integer between 1 and 10
    if(randomint == 1):
    	print '%s' % (line) # output the key value pair where k = num, and v = line

    