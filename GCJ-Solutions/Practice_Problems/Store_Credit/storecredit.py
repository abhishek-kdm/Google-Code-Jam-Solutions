#!/usr/bin/env python
# -*- coding: utf8 -*-

def calc_price(inputdata):
  credit, no_items, itemprice = inputdata
  prices = [int(x) for x in itemprice.split()]

  for i in range(int(no_items)):
    for j in range(i+1, int(no_items)):
      if prices[i] + prices[j] == int(credit):
        return (i+1, j+1)

for i in range(int(input())):
  inputdata = tuple([raw_input() for x in range(3)])
  result = calc_price(inputdata)
  print 'Case #%d: %d %d' % (i+1, result[0], result[1])
