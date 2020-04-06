# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def parse(word):
  l, t, c = [], [], 0
  for i in word:
    if i == '(':
      c, t = 1, []
      continue
    if i == ')':
      c = 0
      l.append(t)
      continue
    if c: t.append(i)
    else: l.append(i)
  return l

def possibilities(ls, words):
  count = 0
  for i in words:
    if all((i[j] in ls[j]) for j in range(len(i))): count+=1
  return count

l, d, n = map(int, input().split())
words = []
for _ in range(d):
  words.append(input())
for c in range(1, n+1):
  print ("Case #%d:"%c, end=" ")
  ls = parse(input())
  print (possibilities(ls, words))

