#!/usr/bin/env python
# -*- coding: utf8 -*-

t9 = [ ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
      ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'],
      ['w', 'x', 'y', 'z'] ]

def getKeypressed(j):
  for x in range(len(t9)):
    if j in t9[x]:
      return str(x+2)*(t9[x].index(j)+1)

for case in range(int(input())):
  data = str(raw_input())
  result = ''
  for i in range(len(data)):
    if data[i] == ' ':
      sol = '0'
    else: sol = getKeypressed(data[i])
    if len(result)>0:
      if result[-1] == sol[0]:
        result+=' '+sol
      else: result+=sol
    else: result+=sol
  print 'Case #%d: %s' %(case+1, result)
