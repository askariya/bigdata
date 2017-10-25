#!/usr/bin/env python
#reducer.py
import string
import sys

prev_word = None
fileList = [] # list of all files associated with a given word

for line in sys.stdin:
    line = line.rstrip()
    word,filename = line.split('\t')

    if (prev_word == None): # if this is the first line
        prev_word=word  # save word
        fileList.append(filename) #add file to list
        continue
    if prev_word == word: # if this word has already been recorded
        if filename in fileList: # ignore if the current filename is the same as the last
            continue
        else:# if this is a new filename, add it to file list
            fileList.append(filename)
            continue
    if prev_word != word: # if this is a new word, print the previous word and its fileList
        print '%s\t%s' %(prev_word,fileList)
        prev_word=word
        del fileList[:] # clear the fileList
        fileList.append(filename) # add current file to the list

print '%s\t%s' %(prev_word, fileList) #print the last word and its associated fileList
