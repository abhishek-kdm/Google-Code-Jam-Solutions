#!/usr/bin/env python
# -*- coding: utf8 -*-

for case in range(int(input())):
  n, m = map(int, raw_input().split())
  lst = [raw_input().strip() for x in range(n+m)]
  exist = [x for x in lst[:n]]
  new = [x.split('/') for x in lst[n:]]
  mkdircount = 0
  for i in new:
    for j in range(1, len(i)):
      path =  '/'.join(i[:j+1])
      if not path in exist:
        mkdircount+=1
        exist.append(path)
  print 'Case #%d: %d' %(case+1, mkdircount)
