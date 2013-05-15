#!/usr/bin/env python # -*- coding: utf-8 -*- 

from operator import itemgetter

def ingreso(diccionario, X):
    try:
        diccionario[X] = diccionario[X] + 1 
    except:
        diccionario[X] = 1

def funes():
    y= open("funes.txt", "r",encoding = 'utf-8')
    lines = y.read()
    lines = lines.lower()
    lista = lines.split()
    diccionario = {}
    diccionario = dict.fromkeys(lista,0)


    for X in lista:
        ingreso(diccionario,X) 

    diccionario = sorted(diccionario.items(),key=itemgetter(1),reverse=True)
    for X in diccionario:
        print (A)
    y.close()

funes()
