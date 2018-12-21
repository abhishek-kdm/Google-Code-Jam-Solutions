#!/usr/bin/env python
# -*- coding: utf8 -*-

from string import digits

def solve(data):
  d = list(digits)
  dx = str(data)
  x=1
  while(len(d)>0):
    dx = str(data*x)
    for i in dx:
      if i in d: d.remove(i)
    x+=1
  return dx

for case in range(int(input())):
  n = raw_input().strip()
  if n=='0': result = 'INSOMNIA'
  else: result = solve(int(n))
  print 'Case #%d: %s' %(case+1, str(result))
