#!/usr/bon/env python
# -*- coding: utf8 -*-

def solve(N, Slist):
  stoodup, needed = 0, 0
  for i in range(N+1):
    if stoodup >= i:
      stoodup+=Slist[i]
    else:
      needed+=(i-stoodup)
      stoodup+=(i-stoodup)+Slist[i]
  return needed

for case in range(int(input())):
  data = raw_input().split()
  M_idx = int(data[0])
  Slist = map(int, list(data[1]))
  print 'Case #%d: %d'%(case+1, solve(M_idx, Slist))
