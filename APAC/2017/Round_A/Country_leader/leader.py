#!/usr/bin/env python
# -*- coding: utf8 -*-

for case in range(int(input())):
  n = int(input())
  names =  [raw_input().strip() for x in xrange(n)]
  unique_names = {}
  for name in names:
    u = ''
    for a in name:
      if a not in u and a != ' ': u+=a
    unique_names[name] = len(sorted(u))

  newlst = []
  biggest = max(unique_names.values())
  for i in unique_names:
    if unique_names[i] == biggest: newlst.append(i)

  res = sorted(newlst)[0]
  print 'Case #%d: %s\n' % (case+1, res)