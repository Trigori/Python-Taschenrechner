# -*- coding: utf-8 -*-
"""
Taschenrechner

Created on Thu Aug 15 15:58:41 2019

@author: simon.stumm
"""
import math

operators = {"+" : (1,"Addition     "),"-" : (-1,"Subtraktion  "),"*" : ("*","Mutiplikation"),"/" : ("/","Division     ")}

#Einlesen von Zahlen
def num_read (output=""):
    while True:
        try:
            read = input(output)
            if read == "pi":
                read = math.pi
            elif read == "e":
                read = math.e
            else:
                read = int(read)
            print("\n")
            break
        except:
            print("Das ist keine Zahl")
    return read

###

#Eingabe
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

#Verrechnen
result = ""
while result == "":
    if operator in (-1,1):
        result = num1 + num2 * operator
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        try:
            result = num1 / num2
            if result == int(result):
                result = int(result)
        except:
            print("Division durch 0 nicht möglich")
            break
    print("Ergebnis: ",num1," ",choose," ",num2," = ",result)
###