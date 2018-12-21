#!/usr/bin/env python
# -*- coding: utf8 -*-

def calculate(sym):
  dct = {sym[0]:1}
  for i in sym:
    length = len(dct)
    if not i in dct.keys():
      if length == 1:
        dct[i] = 0
      else:
        dct[i] = length
  base, result = max(len(dct), 2), 0
  for i in sym:
    result*=base
    result+=dct[i]
  return result

for case in range(int(input())):
  symbols = raw_input().strip()
  print 'Case #%d: %d' %(case+1, calculate(symbols))
