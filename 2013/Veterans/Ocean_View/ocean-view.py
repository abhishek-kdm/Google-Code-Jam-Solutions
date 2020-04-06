#!/usr/bin/env python
# -*- coding: utf8 -*-

def solve(N, data):
  count=0
  for i in range(1, N):
    if data[i] <= data[i-1]:
      count+=1
  return count

for case in range(int(input())):
  N = int(int(input()))
  houses = map(int, raw_input().split())
  print 'Case #%d: %d'%(case+1, solve(N, houses))
