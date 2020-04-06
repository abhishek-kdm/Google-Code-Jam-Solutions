#!/usr/bin/env python
# -*- coding: utf8 -*-

def pickup(n, k, barn, time, c_pos, c_vel):
  crossed, swaps, result = 0, 0, 0
  x = n-1
  while(x>=0 and crossed<k):
    if c_pos[x]+(time*c_vel[x]) < barn:
      swaps+=1
    else:
      crossed+=1
      result+=swaps
    x-=1
  if crossed<k: result = 'Impossible' 
  return result

for case in range(int(input())):
  n, k, barn, time = map(int, raw_input().split())
  c_pos = map(int, raw_input().split())
  c_vel = map(int, raw_input().split())
  solution = pickup(n, k, barn, time, c_pos, c_vel)
  print 'Case #%d: %s'%(case+1, str(solution))
