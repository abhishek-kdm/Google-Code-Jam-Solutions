#!/usr/bin/env python
# -*- coding: utf8 -*-

from string import ascii_uppercase as up

def solve(passwd):
  if len(passwd) < 2: return 'IMPOSSIBLE'
  for i in passwd:
    if passwd.count(i) > 1: return up
  sol = passwd[::-1]
  for i in up:
    if i not in sol: sol+=i
  return sol

for case in range(int(input())):
  plen, passwd = int(input()), str(raw_input().strip())
  print 'Case #%d: %s' % (case+1, solve(passwd))
