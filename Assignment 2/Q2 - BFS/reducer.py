#!/usr/bin/env python
#mapper.py

# input format: node<tab>adjacency_list|score|colour|parent
# compare colours of same nodes and take the darker colour node
import sys

prev_node = None
# dict to hold the finished node
fin_node = {
'node_id' : None,
'adj_list' : None,
'score' : None,
'colour' : None,
'parent' : None
}

def updateFinishedNode(node, adj_list, score, colour, parent):
    fin_node['node_id'] = node
    fin_node['adj_list'] = adj_list
    fin_node['score'] = score
    fin_node['colour'] = colour
    fin_node['parent'] = parent # node parent with the lowest score


for line in sys.stdin:
    line = line.strip() # remove all whitespace at the front and the end of each of the lines
    node, rest = line.split('\t')
    adj_list, score, colour, parent = rest.split('|')
    adj_list_array = adj_list.split(',') # split by comma

    # first run
    if prev_node == None:
        # assign values to the finished node
        updateFinishedNode(node, adj_list, score, colour, parent)
        prev_node = node
        continue

    # if this is another record of the same node
    if prev_node == node:
        # COLOURS: compare colours and pick darker colour (based on alphabetical order)
        d_colour = min(fin_node['colour'], colour)
        if d_colour == "BLACK":
            fin_node['colour'] = "BLACK"
        elif d_colour == "GRAY":
            fin_node['colour'] = "GRAY"
        elif d_colour == "WHITE":
            fin_node['colour'] = "WHITE"
        else:
            raise ValueError('Colour is not in our list')

        # ADJACENCY LIST: Get the non-null adjacency list
        if adj_list != "None":
            fin_node['adj_list'] = adj_list
        # SCORE + PARENT: Get the score and parent of the lowest
        if score != "None" and fin_node['score'] != "None":
            if score < fin_node['score']:
                fin_node['score'] = score
                fin_node['parent'] = parent
        elif score != "None" and fin_node['score'] == "None":
            fin_node['score'] = score
            fin_node['parent'] = parent
        continue

    # if this is a new node
    if prev_node != node:
        print"%s\t%s|%s|%s|%s" %(fin_node['node_id'], fin_node['adj_list'], fin_node['score'], fin_node['colour'], fin_node['parent'])
        updateFinishedNode(node, adj_list, score, colour, parent)
        prev_node = node
print"%s\t%s|%s|%s|%s" %(fin_node['node_id'], fin_node['adj_list'], fin_node['score'], fin_node['colour'], fin_node['parent'])


    # # if colour is black or white, print the record
    # if colour  == "BLACK" or colour == "WHITE":
    #     print line
    # # if the colour is gray make the nodes colour black and emit the node
    # if colour == "GRAY":
    #     colour = "BLACK"
    #     print "%s\t%s|%s|%s|%s" %(node, adj_list, score, colour, parent)
    #     # for each kid, make their colour gray, assign parent, calculate score and print
    #     for kid in adj_list_array:
    #         kid_colour = "GRAY"
    #         kid_parent = node
    #         kid_score = int(score) + 1
    #         print"%s\t%s|%s|%s|%s" %(kid, None, kid_score, kid_colour, kid_parent)

    # print adj_list, colour, score, parent
    # print "%s, %s, %s" %(col, row, value)
