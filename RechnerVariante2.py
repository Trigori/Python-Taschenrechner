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


def listConvert (string):
    term = []
    bracket, sign = 0, 1
    k, i = 0, 0
    while i < len(string):
        if string[i] in operators:
            if (i == 0) or (string[i-1] in operators) or (string[i-1] == '('):
                if (string[i] != '-') or (i == len(string)-1) or (string[i+1] not in digits):
                    term.append('0')
                    term.append(string[i])
                else:
                    sign = -1
            elif string[i-1] == ')':
                term.append(string[i])
            else:
                term.append(sign * string[k:i])
                sign = 1
                term.append(string[i])
            k = i + 1
    
        elif string[i] == '(':
            if (i == 0) or (string[i-1] in operators) or (string[i-1] == '('):
                term.append('(')
            elif string[i-1] == ')':
                term.append('*')
                term.append(string[i])
            else:
                term.append(sign * string[k:i])
                term.append('*')
                term.append('(')
                sign = 1
            k = i + 1
            bracket += 1
        
        elif string[i] == ')':
            if bracket == 0:
                return 'ErrorBracket'
            elif term[-1] == '(':
                term.pop(-1)
            elif string[i-1] == ')':
                term.append(')')
            elif string[i-1] in operators:
                term.append('0')
                term.append(')')
            else:
                term.append(sign * string[k:i])
                sign = 1
                term.append(')')
            k = i + 1
            bracket -= 1
            
        elif string[i] not in digits or string[i-1:i+1] == '..':
            return 'ErrorSymbol'
        
        if i == len(string)-1:
            if string[i] == '(':
                term.pop(-1)
                bracket -= 1
            elif string[i] in operators:
                term.append('0')
            elif string[i] in digits:
                term.append(sign * string[k:i+1])
            while bracket > 0:
                term.append(')')
                bracket -= 1
        i += 1  
    return term


def numConvert (term):
    bracket = 0
    j = 0
    while j < len(term):
        if term[j] == '(':
            bracket += 1
            term[j] = [bracket]   
        elif term[j] == ')':
            term[j] = [bracket]
            bracket -= 1
        elif term[j] not in operators:
            term[j] = float(term[j])
        j += 1
    return term


while True:
    
    #Einlesen
    print("Bitte geben sie einen Term ein \n","oder drücken sie 'ENTER' zum Beenden\n")
    for i in operators:
        print(operators[i][1]," : ",i)
    print("Klammern       :  ( )")
    read = input() 
            
    #Konvertieren & Rechnen
    if len(read) == 0:
        print("Abbruch")
        break
    else:
        read = listConvert(read)
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