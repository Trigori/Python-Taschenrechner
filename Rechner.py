# -*- coding: utf-8 -*-
"""
Taschenrechner

Created on Thu Aug 15 15:58:41 2019

@author: simon.stumm
"""
operators = {"+" : 1,"-" : -1}

while True:
    try:
        num1 = input("Welche Zahl soll eingelesen werden? ")
        num1 = int(num1)
        print("Ok")
        break
    except:
        print("Das ist keine Zahl")

while True:
    try:
        choose = input("Wie soll verrechnet werden?\nAddition   : +\nSubtraktion: -\n")
        operator = operators[choose]
        print("Ok")
        break
    except:
        print("Das ist kein gültiger Rechenoperator")

while True:
    try:
        num2 = input("Welche Zahl soll addiert werden? ")
        num2 = int(num2)
        print("Ok")
        break
    except:
        print("Das ist keine Zahl")
 
result = num1 + num2 * operator       
print("Ergebnis: ",num1," ",choose," ",num2," = ",result)
###