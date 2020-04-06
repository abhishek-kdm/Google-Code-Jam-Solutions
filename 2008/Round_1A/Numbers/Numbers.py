#!/usr/bin/env python
# -*- coding: utf8 -*-

def matrix_mult(A, B):
  C = [[0, 0], [0, 0]]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        C[i][k] = (C[i][k] + A[i][j] * B[j][k]) % 1000
  return C

def fast_exponentiation(A, n):
  if n == 1:
    return A
  else:
    if n % 2 == 0:
      A1 = fast_exponentiation(A, n/2)
      return matrix_mult(A1, A1)
    else:
      return matrix_mult(A, fast_exponentiation(A, n - 1))

def solve(n):
  A = [[3, 5], [1, 3]]
  A_n = fast_exponentiation(A, n)
  return (2 * A_n[0][0] + 999) % 1000

for case in range(int(input())):
  result = str(solve(int(input())))
  if len(result) < 3:
    while not len(result) == 3:
      result = '0'+result
  print 'Case #%d: %s' %(case+1, result)
