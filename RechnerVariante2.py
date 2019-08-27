# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:13:52 2019

@author: simon.stumm
"""
import math

operators = {"+" : (1,"Addition     "),"-" : (-1,"Subtraktion  "),"*" : ("*","Mutiplikation"),"/" : ("/","Division     ")}
ziffer = ('1','2','3','4','5','6','7','8','9','0','.')

def calculate (operator, term):
    
    if len(operator) == 0:
        if len(term) != []:
            return term[0]
        else:
            return 0
    
    # Multiplication & Division
    i = 0
    while i < len(operator):
        if operator[i] == "*":
            term[i] = term[i] * term.pop(i+1)
            operator.remove("*")
        elif operator[i] == "/":
            try:
                term[i] = term[i] / term.pop(i+1)
                if term[i] == int(term[i]):
                    term[i] = int(term[i])
                operator.remove("/")
            except:
                return "undefined"
        else:
            i += 1
    # Addition & Subtraction
    while 0 < len(operator):
        term[0] = term[0] + term.pop(1) * operators[operator.pop(0)][0]
    return term[0]


#Einlesen
print("Bitte geben sie eine Rechnung ein\n")
for i in operators:
    print(operators[i][1]," : ",i)
eingabe = input()

numbers = []
choose  = []
k = 0
i = 0
while i < len(eingabe):
    if eingabe[i] in operators:
        if i == k:
            numbers.append(0)
        else:
            numbers.append(eingabe[k:i])
        print(numbers)
        if i == len(eingabe)-1:
            numbers.append(0)
            print(numbers)
        choose.append(eingabe[i])
        k = i+1
        print(choose," ",k)
    elif eingabe[i] not in ziffer:
        print("Eingabefehler")
        numbers = []
        choose  = []
        k = 0
        i = 0
        eingabe = input("Bitte geben sie eine Rechnung ein\n")
    elif i == len(eingabe)-1:
        numbers.append(eingabe[k:i+1])
        print(numbers)
    i += 1

#In Zahlen konvertieren
j = 0
while j < len(numbers):
    numbers[j] = int(numbers[j])
    j += 1
print(numbers)

#Rechnen
if calculate(choose,numbers) == "undefined":
    print("Division durch 0 nicht möglich")
else:
    print(" = ",numbers[0])
