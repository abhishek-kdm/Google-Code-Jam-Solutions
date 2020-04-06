#!/usr/bin/env python
# -*- coding: utf8 -*-

def getDecimal(alien_no, src_lang):
  baseofSrc = len(src_lang)
  dec_no = 0
  for power, i in enumerate(alien_no[::-1]):
    val = src_lang.index(i)
    dec = val * (baseofSrc**power)
    dec_no += dec
  return int(dec_no)

def targetLang(base_10, target_lang):
  mod = []
  baseofTarget = len(target_lang)

  while base_10 != 0:
    remainder = base_10 % baseofTarget
    mod.append(target_lang[remainder])
    base_10/=baseofTarget
  return str(''.join(mod[::-1]))

for case in xrange(int(input())):
  alien_no, src_lang, target_lang = map(str, raw_input().split())
  base_10 = getDecimal(alien_no, src_lang)
  print 'Case #%d: %s'%(case+1, targetLang(base_10, target_lang))
