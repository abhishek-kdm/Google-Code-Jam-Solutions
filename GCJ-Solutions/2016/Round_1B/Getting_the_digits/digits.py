#!/usr/bin/env python
# -*- coding: utf8 -*-

digits = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

def clean(idx, data):
  for i in digits[idx]:
    idx2 = data.index(i)
    data = data[:idx2]+data[idx2+1:] 
  return data

def solve(data):
  lst = []
  while 'Z' in data:
    data = clean(0, data)
    lst.append(0)

  while 'G' in data:
    data = clean(8, data)
    lst.append(8)

  while 'H' in data:
    data = clean(3, data)
    lst.append(3)

  while 'X' in data:
    data = clean(6, data)
    lst.append(6)

  while 'W' in data:
    data = clean(2, data)
    lst.append(2)

  while 'U' in data:
    data = clean(4, data)
    lst.append(4)

  while 'F' in data:
    data = clean(5, data)
    lst.append(5)

  while 'V' in data:
    data = clean(7, data)
    lst.append(7)

  while 'O' in data:
    data = clean(1, data)
    lst.append(1)

  while 'N' in data:
    data = clean(9, data)
    lst.append(9)

  return ''.join(map(str, sorted(lst)))


for case in range(int(input())):
  S = str(raw_input())
  print 'Case #%d: %s' % (case+1, solve(S))
