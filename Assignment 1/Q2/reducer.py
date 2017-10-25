#!/usr/bin/env python
#reducer.py

import string
import sys

prev_key = None
tot_count = 0
for line in sys.stdin:
    line = line.rstrip()
    digram,count = line.split('\t')
    if prev_key==None:
        prev_key=digram
        tot_count=int(count)
        continue
    if prev_key==digram:
        tot_count=tot_count+int(count)
        continue
    if prev_key!=digram:
        print '%s\t%s' %(prev_key,tot_count)
        prev_key=digram
        tot_count=int(count)
print '%s\t%s' %(prev_key,tot_count)