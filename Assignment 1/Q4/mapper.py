#!/usr/bin/env python
#mapper.py

import string
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for c in string.punctuation:
            word=word.replace(c,"")
        if(len(word) > 0):
            if(word[0].isdigit()):
                print '%s.%s' %(0, word) # if the word is a number, make the key a 0
                continue
            print '%s.%s' %(word[0], word) # send first char of word + full word to the key field partitioner
