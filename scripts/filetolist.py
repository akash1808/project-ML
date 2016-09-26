#!/usr/bin/python
import sys
d = []
with open(sys.argv[1]) as f:
    for line in f:
       d.append(line.rstrip())
print d
