# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:13:52 2019

@author: simon.stumm
"""

import math

operators = {"+" : (1,"Addition     "),"-" : (-1,"Subtraktion  ")}
ziffer = ('1','2','3','4','5','6','7','8','9','0','.')

#Einlesen
eingabe = input("Bitte geben sie eine Rechnung ein\n")
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
        if i == k:
            numbers.append(0)
        else:
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
if len(choose) == 0:
    if len(numbers) > 0:
        result = numbers[0]
    else:
        result = 0
else:
    result = numbers[0]
    l = 0
    while l < len(choose):
        result = result + numbers[l+1]*operators[choose[l]][0]
        l += 1
print(" = ",result)
