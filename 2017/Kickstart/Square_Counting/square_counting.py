# !/usr/bin/env python3
# -*- coding: utf-8 -*-

_MOD = (10**9)+7
SqSum = lambda a: a[0]*a[1]*a[1]

# For Blocks in a grid(m, n) -> m < n
# All possible straight squares, given by =>
# sum(m^2) + (n-m)*sum(m)
# m(m+1)(2m+1)/6 + (n-m)m(m+1)/2

straight_squares = lambda r, c: int (
  r*(r+1)*(2*r+1)/6 + (c-r) * (r*(r+1)/2)
)

def tilted_squares(m, n):
  l = range(1, m)
  a = (n-m) * (sum(l[:-1]) if len(l) > 1 else sum(l))
  return a + sum(map(SqSum, zip(l, l[::-1])))

for case in range(int(input())):
  print ("Case: #%d: "%(case+1), end="")
  r, c = map(int, input().split())
  grid = sorted([r-1, c-1])
  straight = straight_squares(*grid)
  tilted = tilted_squares(*grid)
  print ((straight+tilted) % _MOD)
