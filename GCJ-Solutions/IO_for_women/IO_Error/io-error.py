#!/usr/bin/env python
# -*- coding: utf8 -*-

import re

## MANUALLY COVERTING INTO BINARY (NOT NEEDED CAUSE PYTHON ROCKS!!)
## BUT STILL A DETAILED EXAGERATED CODE
## HAVEN'T USED THIS BELOW

def convert(data):
  binary = ['0', '1']
  base = len(binary)
  message = ''
  for i in data:
    dec_no = 0
    for power, j in enumerate(i[::-1]):
      val = binary.index(j)
      dec = val*(base**power)
      dec_no+=dec
    message+=chr(dec_no)
  return message

##
## EASY SOLUTION BELOW ->
##

I = re.compile(r'I')
O = re.compile(r'O')
for case in range(int(input())):
  l, data = int(input()), raw_input().strip()
  datalist = []
  for i in range(l):
    datalist.append(data[:8])
    data = data[8:]
  for i in range(len(datalist)):
    datalist[i] = re.sub(I, '1', datalist[i])
    datalist[i] = re.sub(O, '0', datalist[i])
  print 'Case #%d: %s'%(case+1,''.join([chr(int(i,2)) for i in datalist]))
