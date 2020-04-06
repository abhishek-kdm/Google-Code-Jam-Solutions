#!/usr/bin/env python
# -*- coding: utf8 -*-

##  BEST WAY TO DO WITH THIS SHORT ALGORITHM (O(n^2))->
##  (x1-x2) * (y1-y2) < 0

def getIntersect(wires):
  result=0
  for i in range(len(wires)-1):
    x1, y1 = wires[i]
    for j in wires[i+1:]:
      x2, y2 = j
      if int(x1)>int(x2):
        if int(y1)<int(y2):
          result+=1
      elif int(y1)>int(y2):
        result+=1
  return result

for case in range(int(input())):
  n = int(input())
  wires = [tuple((raw_input().strip()).split()) for x in range(n)]
  print 'Case #%d: %d' %(case+1, getIntersect(wires))
