#!/bin/bash
cat input.txt| python mapper.py | sort -k 1,1 | python reducer.py
