# -*- coding: utf-8 -*-
"""
Taschenrechner

Created on Thu Aug 15 15:58:41 2019

@author: simon.stumm
"""
operators = {"+" : 1,"-" : -1}

def num_read (output=""):
    while True:
        try:
            read = input(output)
            read = int(read)
            print("\n")
            break
        except:
            print("Das ist keine Zahl")
    return read

###

num1 = num_read("Welche Zahl soll eingelesen werden? ")

while True:
    try:
        choose = input("Wie soll verrechnet werden?\nAddition   : +\nSubtraktion: -\n")
        operator = operators[choose]
        break
    except:
        print("Das ist kein gültiger Rechenoperator")

num2 = num_read("Welche Zahl soll verrechnet werden? ")
result = num1 + num2 * operator 
      
print("Ergebnis: ",num1," ",choose," ",num2," = ",result)
###