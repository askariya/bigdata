#!/usr/bin/env python
#mapper.py

import string
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    prev_word = None
    for word in words:
        for c in string.punctuation:
            word=word.replace(c,"")

        if(prev_word == None):
        	prev_word = word
        	continue

        print'%s %s\t%s' %(prev_word,word,1)
        prev_word = word
