#!/usr/bin/env python
# -*- coding: utf8 -*-

################################
## JUST WORKS WITH SMALL INPUT
################################

inputfile = 'input.in'
outputfile = 'output.op'

if __name__ == '__main__':
  inputdata = open(inputfile, 'rb').readlines()
  cases = int(inputdata[0])
  inputdata.pop(0)
  with open(outputfile, 'wb') as out:
    for case in range(cases):
      A, B, K = map(int, inputdata[0].split())
      res = len(['' for a in range(A) for b in range(B) if (a&b) < K])
      out.write('Case #%d: %d\n' % (case+1, res))
      inputdata = inputdata[1:]
