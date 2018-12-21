#!/usr/bin/env python
# -*- coding: utf8 -*-

def solve(data):
  pat = ['-', '+']
  if data[-1]==pat[0]: count=1
  else: count=0
  for i in range(len(data)-1):
    if data[i] != data[i+1]:
      count+=1
  return count

for case in range(int(input())):
  data = raw_input().strip()
  print 'Case #%d: %d'%(case+1, solve(data))
