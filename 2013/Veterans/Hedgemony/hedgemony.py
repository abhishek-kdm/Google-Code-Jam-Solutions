#!/usr/bin/env python
# -*- coding: utf8 -*-

def solve(N, data):
  for i in range(1, N-1):
    avg = float(data[i-1]+data[i+1])/2
    if data[i]>avg:
      data[i]=avg
  return data[-2]

for case in range(int(input())):
  N = int(input())
  data = map(int, raw_input().split())
  print 'Case #%d: %f' % (case+1, solve(N, data))
