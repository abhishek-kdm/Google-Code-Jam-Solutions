#!/usr/bin/env python
# -*- coding: utf8 -*-

inputfile = 'input.in'
outputfile = 'output.op'

def shortify(data):
  shortver = data[0][0]
  for i in data[0]:
    if i != shortver[-1]:
      shortver+=i
  return shortver

def average(data):
  count=0
  for i in xrange(len(data[0])):
    tmp = []
    for j in xrange(len(data)):
      tmp.append(data[j][i])
    count+=difference(tmp)
  return count

def difference(lst):
  lst = map(int, sorted(lst))
  count, N = 0, len(lst)-1
  for i in lst:
    if i < lst[N/2]: count+=(lst[N/2]-i)
    elif i > lst[N/2]: count+=(i-lst[N/2])
  return count

def solve(n, data):
  shortver = shortify(data)
  win = True
  result = []
  for i in xrange(len(data)):
    totcounts = []
    for letter in shortver:
      count = -1
      while len(data[i]) > 0:
        if data[i][0] == letter:
          data[i]=data[i][1:]
          count+=1
        else: break
      if count == -1:
        win = False
        break
      else:totcounts.append(count)
    if len(data[i]) >= 1: win = False
    if not win: break
    else: result.append(totcounts)
  if not win: return 'Fegla Won'
  return str(average(result))

if __name__ == '__main__':
  inputdata = open(inputfile, 'rb').readlines()
  cases = int(inputdata[0])
  inputdata.pop(0)
  with open(outputfile, 'wb') as out:
    for case in range(cases):
      n = int(inputdata[0])
      data = [x.strip() for x in inputdata[1:n+1]]
      out.write('Case #%d: %s\n' % (case+1, solve(n, data)))
      inputdata = inputdata[n+1:]