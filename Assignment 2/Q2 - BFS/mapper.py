#!/usr/bin/env python
#mapper.py

# input format: node<tab>adjacency_list|score|colour|parent
import sys
for line in sys.stdin:
    line = line.strip() # remove all whitespace at the front and the end of each of the lines
    node, rest = line.split('\t')
    adj_list, score, colour, parent = rest.split('|')
    adj_list_array = adj_list.split(',') # split by comma

    # if colour is black or white, print the record
    if colour  == "BLACK" or colour == "WHITE":
        print line
    # if the colour is gray make the nodes colour black and emit the node
    if colour == "GRAY":
        colour = "BLACK"
        print "%s\t%s|%s|%s|%s" %(node, adj_list, score, colour, parent)
        # for each kid, make their colour gray, assign parent, calculate score and print
        for kid in adj_list_array:
            kid_colour = "GRAY"
            kid_parent = node
            kid_score = int(score) + 1
            print"%s\t%s|%s|%s|%s" %(kid, None, kid_score, kid_colour, kid_parent)

    # print adj_list, colour, score, parent
    # print "%s, %s, %s" %(col, row, value)
