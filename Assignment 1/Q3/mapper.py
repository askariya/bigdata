#!/usr/bin/env python
#mapper.py

import sys
import string
import os

for line in sys.stdin:
    fpath = os.environ["mapreduce_map_input_file"] # environment variable for Hadoop containing filepath
    fileName = os.path.split(fpath)[-1] # get the end of the filepath
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for c in string.punctuation:
            word=word.replace(c,"")
        print '%s\t%s' %(word, fileName) # key = word, value = filename
