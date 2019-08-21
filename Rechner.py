# -*- coding: utf-8 -*-
"""
Taschenrechner

Created on Thu Aug 15 15:58:41 2019

@author: simon.stumm
"""

import sys

while True:
    try:
        number = input("Welche Zahl soll eingelesen werden? ")
        number = int(number)
        print("Ok")
        break
    except:
        print("Das ist keine Zahl")

print("Eingabe: " , number)
###