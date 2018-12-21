#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import product

_ = input()

def nonTrivial(n):
  for i in range(2, int(n**(.5)+1)):
    if n%i==0: return i
  return 0

print ("Case #1:")
n, j = map(int, input().split())
count = 0
for i in product("01", repeat=n-2):
  if count==j: break
  val, tmp = "1"+"".join(i)+"1", []

  for b in range(2, 11):
    p = nonTrivial(int(val, b))
    if not p: break
    tmp.append(p)

  if len(tmp) == 9:
    print (val, end="")
    for v in tmp:
      print ("", v, end="")
    print ()
    count+=1
