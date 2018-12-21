#!/usr/bin/env python
# -*- coding: utf8 -*-

def solve(p, e, t, ratio):
  pedal_ratios = [[x/y for x in p] for y in e] ## pedal to extra
  for i in range(len(pedal_ratios)):
    tmp = e[:i]+e[i+1:]
    sol = [round(a*x/y, len(ratio.split('.')[1])) for a in pedal_ratios[i] \
      for x in tmp for y in t]
    if ratio in map(str, sol):
      return 'Yes'
  return 'No'

for case in range(int(input())):
  _ = raw_input()
  p, e, t = map(int, raw_input().split())
  Np = map(float, raw_input().split())
  Ne = map(float, raw_input().split())
  Nt = map(float, raw_input().split())
  Nq = int(input())
  print 'Case #%d:' % (case+1)
  for i in range(Nq):
    ratio = map(float, raw_input().split())
    G_ratio = ratio[0]/ratio[1]
    print solve(Np, Ne, Nt, str(G_ratio))
