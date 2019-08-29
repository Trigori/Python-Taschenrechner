# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:13:52 2019

@author: simon.stumm
"""

import math
import unittest


operators = {"+" : (1,"Addition     "),"-" : (-1,"Subtraktion  "),"*" : ("*","Mutiplikation"),"/" : ("/","Division     ")}
digits = ('1','2','3','4','5','6','7','8','9','0','.')
        

def calculate (term,deap=0):
       
    # brackets
    i = 0
    deap += 1
    print("deap:",deap)
    while i < len(term):
        if term[i] == [deap]:
            end = term.index([deap], i+1)
            print(term[i+1:end])
            result = calculate(term[i+1:end],deap)
            
            if result == 'ErrorDiv0':
                return 'ErrorDiv0'
            term[i] = result
            j = end
            while j > i:
                term.pop(j)
                j -= 1
        i += 1
            
    
    # Multiplication & Division
    k = 1
    print("Start multiply")
    print(term)
    while k < len(term):
        if term[k] == '*':
            term[k-1] = term.pop(k-1) * term.pop(k)
        elif term[k] == '/':
            try:
                term[k-1] = term.pop(k-1) / term.pop(k)
            except:
                return 'ErrorDiv0'
        else:
            k += 1
    print(term)
            
    # Addition & Subtraction
    print("Start add/sub")
    print(term)
    while 1 < len(term):
        term[0] = term[0] + term.pop(2) * operators[term.pop(1)][0]
    print(term)
    
    return term[0]


def stringConvert (eingabe):
    numbers = []
    bracket, sign = 0, 1
    k, i = 0, 0
    while i < len(eingabe):
        if eingabe[i] in operators:
            if (i == 0) or (eingabe[i-1] in operators) or (eingabe[i-1] == '('):
                if (eingabe[i] != '-') or (i == len(eingabe)-1) or (eingabe[i+1] not in digits):
                    numbers.append('0')
                    numbers.append(eingabe[i])
                else:
                    sign = -1
            elif eingabe[i-1] == ')':
                numbers.append(eingabe[i])
            else:
                numbers.append(sign * eingabe[k:i])
                sign = 1
                numbers.append(eingabe[i])
            k = i + 1
    
        elif eingabe[i] == '(':
            if (i == 0) or (eingabe[i-1] in operators) or (eingabe[i-1] == '('):
                numbers.append('(')
            elif eingabe[i-1] == ')':
                numbers.append('*')
                numbers.append(eingabe[i])
            else:
                numbers.append(sign * eingabe[k:i])
                numbers.append('*')
                numbers.append('(')
                sign = 1
            k = i + 1
            bracket += 1
        
        elif eingabe[i] == ')':
            if bracket == 0:
                return 'ErrorBracket'
            elif numbers[-1] == '(':
                numbers.pop(-1)
            elif eingabe[i-1] == ')':
                numbers.append(')')
            elif eingabe[i-1] in operators:
                numbers.append('0')
                numbers.append(')')
            else:
                numbers.append(sign * eingabe[k:i])
                sign = 1
                numbers.append(')')
            k = i + 1
            bracket -= 1
            
        elif eingabe[i] not in digits or eingabe[i-1:i+1] == '..':
            return 'ErrorSymbol'
        
        if i == len(eingabe)-1:
            if eingabe[i] == '(':
                numbers.pop(-1)
                bracket -= 1
            elif eingabe[i] in operators:
                numbers.append('0')
            elif eingabe[i] in digits:
                numbers.append(sign * eingabe[k:i+1])
            while bracket > 0:
                numbers.append(')')
                bracket -= 1
        i += 1  
    return numbers


def numConvert (numbers):
    bracket = 0
    j = 0
    while j < len(numbers):
        if numbers[j] == '(':
            bracket += 1
            numbers[j] = [bracket]   
        elif numbers[j] == ')':
            numbers[j] = [bracket]
            bracket -= 1
        elif numbers[j] not in operators:
            numbers[j] = float(numbers[j])
        j += 1
    return numbers


while True:
    
    #Einlesen
    print("Bitte geben sie einen Term ein \n","oder drücken sie 'ENTER' zum Beenden\n")
    for i in operators:
        print(operators[i][1]," : ",i)
    print("Klammern       :  ()")
    read = input() 
            
    #Konvertieren & Rechnen
    if len(read) == 0:
        print("Abbruch")
        break
    else:
        read = stringConvert(read)
        if read == 'ErrorBracket':
            print("Ungültige Verwendung von Klammern\n")
        elif read == 'ErrorSymbol':
            print("Ungültiges Symbol\n")
        else:
            read = numConvert(read)
            result = calculate(read)
            if result == 'ErrorDiv0':
                print("Division durch 0 nicht möglich\n")
            else:
                if result == int(result):
                    result = int(result)
                print(" = ",result,"\n")    