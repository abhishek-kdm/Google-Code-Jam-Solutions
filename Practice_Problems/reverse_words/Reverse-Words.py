#!/usr/bin/env python
# -*- coding: utf8 -*-

for case in range(int(input())):
  print 'Case #%d: %s'%(case+1, ' '.join(raw_input().split()[::-1]))
