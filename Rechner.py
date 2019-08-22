# -*- coding: utf-8 -*-
"""
Taschenrechner

Created on Thu Aug 15 15:58:41 2019

@author: simon.stumm
"""
operators = {"+" : (1,"Addition     "),"-" : (-1,"Subtraktion  "), "*" : ("*","Mutiplikation")}

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
        print("Wie soll verrechnet werden?")
        for i in operators:
            print(operators[i][1]," : ",i)
        choose = input()
        operator = operators[choose][0]
        break
    except:
        print("Das ist kein gültiger Rechenoperator \n")

num2 = num_read("Welche Zahl soll verrechnet werden? ")
if operator in (-1,1):
    result = num1 + num2 * operator
elif operator == "*":
    result = num1 * num2
      
print("Ergebnis: ",num1," ",choose," ",num2," = ",result)
###