#!/usr/bin/env python
# -*- coding: utf8 -*-

from string import ascii_uppercase as up

def rem(data):
  tup = []
  while (len(tup) <= 1):
    idx = data.index(max(data))
    tup.append(idx)
    data[idx]-=1
    if sum(data) == 0 or sum(data) == 2: break
  return data, tup

def solve(N, data):
  lst = []
  while ( sum(data) != 0 ):
    data, tup = rem(data)
    lst.append(''.join(up[i] for i in tup))
  return ' '.join(lst)

for case in range(int(input())):
  N = int(input())
  data = map(int, raw_input().split())
  print 'Case #%d: %s' % (case+1, solve(N, data))
