#!/usr/bin/env python
# -*- coding: utf8 -*-

from string import ascii_lowercase as al

for case in range(int(input())):
  S = raw_input().strip().lower()
  s = S[0]
  for i in S[1:]:
    if al.index(i)>=al.index(s[0]): s = i+s
    else: s+=i
  print 'Case #%d: %s'%(case+1, s.upper())
