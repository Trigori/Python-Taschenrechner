# -*- coding: utf-8 -*-
"""
Taschenrechner

Created on Thu Aug 15 15:58:41 2019

@author: simon.stumm
"""

import sys

print("Welche Zahl soll eingelesen werden? ")
number = 0
while 1:
    c = sys.stdin.read(1)
    if c == '\n':
        break
    else
        number = number*10 + int(c)

print("Eingabe: " , number)

###