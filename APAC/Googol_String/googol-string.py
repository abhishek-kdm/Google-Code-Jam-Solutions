#!/usr/bin/env python
# -*- coding: utf8 -*-

bit_2 = ['0', '0', '1']

def switch(itr):
  return ''.join([chr(ord('1')+ord('0')-ord(x)) for x in itr])

def pow2(num):
  n=1
  while(not 2**n>num): n+=1
  return n

def shrink(diff, n):
  transpose = True
  while n>0:
    if (2**n) - 2**(n-1) == diff:
      return int(transpose)
    elif (2**n)-2**(n-1) < diff:
      diff = ((2**(n+1)) - diff) - (2**n)
      transpose = not transpose
    n-=1
  if not transpose:
    return switch(bit_2[(2**n)-diff-1])
  return bit_2[(2**n)-diff-1]

def solve(K):
  if K & (K-1) == 0: return 0 # returns 0 if K is pow of 2 .. [2^n = k]
  n = pow2(K)
  diff = (2**(n))-K
  return shrink(diff, n)

for case in range(int(input())):
  K = int(input())
  if K < 3:
    result = bit_2[K-1]
  else: result = solve(K)
  print 'Case #%d: %s' % (case+1, result)
