#!/usr/bin/env python
# -*- coding: utf8 -*-

def minProduct(lst):
  all_xs = sorted([int(x) for x in lst[1].split()])
  all_ys  = sorted([int(x) for x in lst[2].split()])[::-1]
  result = 0
  for x in range(len(all_xs)):
    result+=all_xs[x]*all_ys[x]
  return result

for i in range(int(input())):
  print 'Case #%d: %d'%(i+1, minProduct([raw_input() for x in range(3)]))
