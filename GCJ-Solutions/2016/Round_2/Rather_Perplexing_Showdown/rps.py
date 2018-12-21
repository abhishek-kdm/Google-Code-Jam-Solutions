#!/usr/bin/env python
# -*- coding: utf8 -*-

val = {'s': ('p', 's'), 'r': ('r', 's'), 'p': ('p', 'r')}

def flatten(iterator):
  lst = []
  for i in iterator:
    if hasattr(i, '__iter__'):
      for i in flatten(i):
        lst.append(i)
    else: lst.append(i)
  return lst

def treesort(N, data):
  if N == 2: return data
  d1, d2 = data[:N/2], data[N/2:]
  count1 = sum([3-val.values().index((d1[x], d1[x+1])) for x in range(0, N/2, 2)])
  count2 = sum([3-val.values().index((d2[x], d2[x+1])) for x in range(0, N/2, 2)])
  if count2 > count1: data = d2+d1
  return treesort(N/2, data[:N/2])+treesort(N/2, data[N/2:])

def check(move, N):
  data = [move]
  while len(data) < 2**N:
    for i in range(len(data)):
      data[i] = val[data[i]]
    data = flatten(data)
  return treesort(2**N, data)

def solve(N, r, p, s):
  if r >= 1:
    lst = check('r', N)
    if lst.count('r') == r and lst.count('s') == s and lst.count('p') == p:
      return ''.join(lst).upper()
  if p >= 1:
    lst = check('p', N)
    if lst.count('r') == r and lst.count('s') == s and lst.count('p') == p:
      return ''.join(lst).upper()
  if s >= 1:
    lst = check('s', N)
    if lst.count('r') == r and lst.count('s') == s and lst.count('p') == p:
      return ''.join(lst).upper()
  return 'IMPOSSIBLE'

for case in range(int(input())):
  n, r, p, s = map(int, raw_input().split())
  print 'Case #%d: %s'% (case+1, solve(n, r, p, s))
