#!/usr/bin/env python
#reducer.py

import string
import sys

finalColor = None
finalAdjList = None
finalScore = None
fianlParent = None
prev_node = None
for line in sys.stdin:
	line = line.strip()
	# id<tab>adjList|score|color|parentNode
	id, remLine = line.split('\t')
	adjList, score, color, parent = remLine.split('|')

	# first iteration
	if prev_node == None:
		prev_node = id
		finalColor = color
		finalAdjList = adjList
		finalScore = score
		fianlParent = parent
		continue

	# new node
	if id != prev_node:
		print('%s\t%s|%s|%s|%s' % (prev_node, finalAdjList, finalScore, finalColor, fianlParent))
		prev_node = id
		finalColor = color
		finalAdjList = adjList
		finalScore = score
		fianlParent = parent
		continue

	# duplicate node
	if id == prev_node:
		# step 1: get darkest color
		if finalColor == 'BLACK' or color == 'BLACK':
			finalColor = 'BLACK'
		elif finalColor == 'GRAY' and color != 'BLACK':
			finalColor = 'GRAY'
		elif color == 'GRAY' and finalColor != 'BLACK':
			finalColor = 'GRAY'
		# if color is WHITE
		else:
			finalColor = 'WHITE'

		# step 2: get largest adjList
		if adjList != 'None' and finalAdjList != 'None':
			if len(adjList) > len(finalAdjList):
				finalAdjList = adjList
		elif adjList != 'None':
			finalAdjList = adjList

		# step 3 & 4: get the smallest score and its parent
		if score != 'null' and finalScore != 'null':
			if score < finalScore:
				finalScore = score
				fianlParent = parent
		elif score != 'null':
			finalScore = score
			fianlParent = parent

# print last node
print('%s\t%s|%s|%s|%s' % (prev_node, finalAdjList, finalScore, finalColor, fianlParent))
