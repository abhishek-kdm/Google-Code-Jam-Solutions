#!/usr/bin/env python
# -*- coding: utf8 -*-

def swaps(lst):
  count = 0
  for i in lst:
    if i%2 == 0:
      count+=1
  return count

def solve(N, data):
  pat1 = data[0]
  pat2 = [chr(ord('0')+ord('1')-ord(i)) for i in pat1]
  pat1_idx, pat2_idx = [], []
  for i in range(N):
    if data[i] == pat1:
      pat1_idx.append(i)
    elif data[i] == pat2:
      pat2_idx.append(i)
    else: return 'IMPOSSIBLE'
  if len(pat1_idx) != len(pat2_idx):
    return 'IMPOSSIBLE'
  return min(swaps(pat1_idx), swaps(pat2_idx))

for case in range(int(input())):
  N = int(input())*2
  data = [list(raw_input().strip()) for x in xrange(N)]
  result = solve(N, data)
  if not result == 'IMPOSSIBLE':
    transposedata = [list(x) for x in zip(*data)]
    T_result = solve(N, transposedata)
    if T_result == 'IMPOSSIBLE':
      result = 'IMPOSSIBLE'
    else: result+=T_result
  print 'Case #%d: %s'%(case+1, str(result))
