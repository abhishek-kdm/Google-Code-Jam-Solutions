#!/usr/bin/env python
# -*- coding: utf8 -*-

def check(board, piece, xcoor, ycoor, k, n):
  ans = False
  x, xinc = xcoor
  y, yinc = ycoor
  count = 0
  while (x>=0 and y>=0 and x<n and y<n):
    if board[y][x] == piece:
      count+=1
    else:
      if count >= k:
        break
      else: count = 0
    x+=xinc
    y+=yinc
  return count


def joink(board, piece, k, n):
  for i in range(n):
    ## HORIZONTAL
    if check(board, piece, (0, 1), (i, 0), k, n) >= k: return True
    ## VERTICAL
    if check(board, piece, (i, 0), (0, 1), k, n) >= k: return True
    ## DIAGONAL (bot-left to top-right)
    if check(board, piece, (0, 1), (i, -1), k, n) >= k: return True
    if check(board, piece, (i, 1), (n-1, -1), k, n) >= k: return True
    ## DIAGONAL (top-left to bot-right)
    if check(board, piece, (i, 1), (0, 1), k, n) >= k: return True
    if check(board, piece, (0, 1), (i, 1), k, n) >= k: return True

  return False

def rotate(board, k):
  ## SQUARE, HENCE n = ROWS = COLUMNS
  n = len(board)
  GSHIFT = []
  pieces = ['R', 'B']
  for i in board:
    lst = shiftgravity(i)
    GSHIFT.append(lst)

  GSHIFT = GSHIFT[::-1]
  R_BOARD = [['' for x in range(n)] for i in range(n)]

  ## ACTUAL ROTATION
  for i in range(n):
    for j in range(n):
      R_BOARD[i][j] = GSHIFT[j][i]

  redwin = joink(R_BOARD, pieces[0], k, n)
  bluewin = joink(R_BOARD, pieces[1], k, n)

  if redwin and bluewin: return 'BOTH'
  elif bluewin: return 'BLUE'
  elif redwin: return 'RED'
  else: return 'NEITHER'

def shiftgravity(lst):
  newlist = []
  for i in lst:
    if not i == '.':
      newlist=[i]+newlist
  while not len(newlist) == len(lst):
    newlist.append('.')
  return newlist[::-1]

for case in range(int(input())):
  n, k = map(int, raw_input().split())
  board = [[i for i in raw_input()] for x in range(n)]
  print 'Case #%d: %s'% (case+1, rotate(board, int(k)))
