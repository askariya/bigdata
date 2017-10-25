#!/usr/bin/env python
#mapper.py

#input format: row_index, column_index, value
import sys
for line in sys.stdin:
    line = line.strip() # remove all whitespace at the front and the end of each of the lines
    row, col, value = line.split(', ') # split by comma
    print "%s, %s, %s" %(col, row, value)
