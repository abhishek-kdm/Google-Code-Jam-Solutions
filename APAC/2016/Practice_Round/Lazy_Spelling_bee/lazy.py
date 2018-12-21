#!/usr/bin/env python
# -*- coding: utf8 -*-

_MOD = (10**9)+7

def solve(w):
  l = len(w)
  if l == 1: return 1
  elif l == 2:
    if w[0] != w[1]: return 4
    else: return 1

  sol = 1
  if w[0] != w[1]: sol*=2
  if w[l-1] != w[l-2]: sol*=2
  for i in range(1, l-1):
    count = 1
    if w[i-1] != w[i]: count+=1
    if w[i+1] not in [w[i-1], w[i]]: count+=1
    sol*=count
  return sol%_MOD

for case in range(int(input())):
  w = map(str, raw_input().strip())
  print 'Case #%d: %d' % (case+1, solve(w))
