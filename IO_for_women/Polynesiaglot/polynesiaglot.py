#!/usr/bin/env python
# -*- coding: utf8 -*-

_MOD = (10**9)+7

def proc(c, v, length):
  _pre = [v, (v**2)+(v*c)]
  if length <= len(_pre):
    return _pre[length-1]
  for i in range(3, length+1):
    newres = ( v * _pre[-1] ) + ( c * v * _pre[-2] )
    _pre[0], _pre[1] = _pre[1], newres
  return _pre[-1]

for case in range(int(input())):
  c, v, length = map(int, raw_input().split())
  result = proc(c, v, length)
  print "Case #%d: %d" % (case+1, result%_MOD)
