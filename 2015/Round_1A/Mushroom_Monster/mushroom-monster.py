#!/usr/bin/env python
# -*- coding: utf8 -*-

def first(lst):
  data=map(int, lst)
  init, count = data[0], 0
  for i in data[1:]:
    if i < init:
      count+=(init-i)
    init = i
  return count

def second(n, lst):
  data=map(int, lst)
  count, eat_rate = 0, 0
  for i in range(1, n):
    eat_rate = max(eat_rate, data[i-1]-data[i])
  for i in range(n-1):
    count+=min(eat_rate, data[i])
  return count

for case in range(int(input())):
  n, data = int(input()), raw_input().split()
  F, S = first(data), second(n, data)
  print 'Case #%d: %d %d'%(case+1, F, S)
