

import random
import Tkinter as tk
from Tkinter import StringVar, Tk, Spinbox, Button
from _tkinter import mainloop
from cgitb import text
from pipes import stepkinds
from _ast import Str
from getpass import fallback_getpass
import tkFileDialog
import tkMessageBox
import _ast
import ast
import copy
import ThreadBackTracking
import time
import multiprocessing
import signal


#Variables globales--------------

global matrizBooleana
global gameframe
#--------------------------------
matrizKakuroFinal =""






#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************
def backtracking(tablero):
    chkTablero = copy.deepcopy(tablero)
    if checkKakuro(chkTablero):
        return(tablero)
    elif(juegoPerdido(tablero)):
        return(None)
    elif(juegoPerdido3(tablero)):
        return(None)
    else:
        iTemp,jTemp = coordenada(tablero)
        i = copy.deepcopy(iTemp)
        j = copy.deepcopy(jTemp)
        if(i!=-1):
            posibles = tablero[i][j]
            posibilidades = copy.deepcopy(posibles)
            temporal = copy.deepcopy(tablero)
            for x in posibilidades:
                print("x= " + str(x) + " i= " + str(i) + " j= " + str(j))
                poda = podaX(temporal,i,j,x)
                intento = copy.deepcopy(poda)
                resuelto = backtracking(intento)
                if(resuelto!=None):
                    return(resuelto)
                else:
                    temporal[i][j] = posibilidades
        else:
            return(None)
def printK(tablero):
    #Imprime matriz en consola
    a=""
    for k in range(len(matrizBooleana)):
        for j in range(len(matrizBooleana)):
            a+=str(tablero[k][j])+'\t'
        print (a)
        a=""

            
def modificarTablero(tablero):
    for i in range(len(matrizBooleana)):
        for j in range(len(matrizBooleana)):
            if(matrizBooleana[i][j]==0):
                tablero[i][j]=matrizPrePoda[i][j]
    return(tablero)
########################################################################
def revisarFilaIzq(kakuro,i,j, numeroCasilla):
    for x in range(0, len(kakuro[0])):
        j -= 1
        if type(kakuro[i][j]) == int:
            if numeroCasilla == kakuro[i][j]:
                return False
        else:
            break
    return  True
################################################################################

def revisarFilaDer(kakuro,i,j, numeroCasilla):
    for x in range(j + 1, len(kakuro[0])):
        if type(kakuro[i][x]) == int:
            if numeroCasilla == kakuro[i][x]:
                return False
        else:
            break
    return  True
################################################################################

def revisarColumArri(kakuro, i, j, numeroCasilla):
    for x in range(0, len(kakuro)):
        i -= 1
        if type(kakuro[i][j]) == int:
            if numeroCasilla == kakuro[i][j]:
                return False
        else:
            break
    return True
################################################################################

def revisarColumAbaj(kakuro, i, j, numeroCasilla):
    for x in range(i + 1, len(kakuro[0])):
        if type(kakuro[x][j]) == int:
            if numeroCasilla == kakuro[x][j]:
                return False
        else:
            break
    return True
################################################################################

def verificarBackCol(kakuro, i, j, sumaColumna):
    for x in range(i + 1, len(kakuro)):
        if type(kakuro[x][j]) == int:
            sumaColumna -= kakuro[x][j]
        else:
            break
    if sumaColumna == 0:
        return True
    else:
        return False
################################################################################
    
def verificarBackFila(kakuro, i, j, sumaFila):
    for x in range(j + 1, len(kakuro[0])):
        if type(kakuro[i][x]) == int:
            sumaFila -= kakuro[i][x]
        else:
            break
    if sumaFila == 0:
        return True
    else:
        return False
################################################################################

'''
Funcion para verificar que un kakuro este bien resuelto
'''
def checkKakuro(kakuro):
    # Recorremos todas las casillas 
    for i in range(0, len(kakuro)):
        for j in range(0, len(kakuro[0])):
            if kakuro[i][j] == [0,0]:
                # En este caso no se revisa nada
                pass
            elif type(kakuro[i][j]) == int:
                # En este caso buscamos numeros repetidos
                if (revisarFilaIzq(kakuro, i, j, kakuro[i][j]) == True
                    and revisarFilaDer(kakuro, i, j, kakuro[i][j]) == True
                    and revisarColumArri(kakuro, i, j, kakuro[i][j]) == True
                    and revisarColumAbaj(kakuro, i, j, kakuro[i][j]) == True):
                    print("Numero no esta Repetido")
                    pass
                else:
                    # Si esta repetido el kakuro esta malo
                    return False
            else:
                # En este caso revisamos las sumas de cada tupla
                if kakuro[i][j][0] == 0:
                    pass
                else:
                    # Se ejecuta la revision de la columna
                    if verificarBackCol(kakuro, i, j, kakuro[i][j][0][0]):
                        pass
                    else:
                        return False
                if kakuro[i][j][1] == 0:
                    pass
                else:
                    # Se ejecuta la revision de la fila
                    if verificarBackFila(kakuro, i, j, kakuro[i][j][1][0]):
                        pass
                    else:
                        return False
    return True
########################################################################
def reemplazar(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j]==0:
                tablero[i][j]=[1,2,3,4,5,6,7,8,9]
    return tablero
########################################################################
def juegoPerdido(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if(matrizBooleana[i][j]==1):
                if(tablero[i][j]==[]):
                    return(True)
    return(False)
########################################################################
def juegoPerdido3(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if(matrizBooleana[i][j]==1 and type(tablero[i][j])==list):
                return  False
    return True
########################################################################

### Verifica si una fila tiene una suma incorrecta
#Retorna true si la fila tiene una lista o si la suma es correcta
#Retorna False si la fila no suma a lo que deberia
def chkRow2(tablero,i,j):
    print("i= " + str(i) + ", j= " + str(j))
    suma=tablero[i][j][1]
    if suma==0:
        return(True)
    j+=1
    while(matrizBooleana[i][j]==1 and j<len(tablero)):
        if(type(tablero[i][j])==list):
            return(True)
        else:
            suma-=tablero[i][j]
        j+=1
    if(suma==0):
        return(True)
    return(False)

### Verifica si una columna tiene una suma incorrecta
#Retorna true si la columna tiene una lista o si la suma es correcta
#Retorna False si la columna no suma a lo que deberia
def chkCol2(tablero,i,j):
    suma=tablero[i][j][0]
    if suma==0:
        return(True)
    i+=1
    while(matrizBooleana[i][j]==1 and i<len(tablero)):
        if(type(tablero[i][j])==list):
            return(True)
        else:
            suma-=tablero[i][j]
        i+=1
    if(suma==0):
        return(True)
    return(False)
########################################################################
def coordenada(tablero):
    minimo = 15
    col=-1
    fila=-1
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if(matrizBooleana[i][j]==1 and type(tablero[i][j])==list):
                if len(tablero[i][j])<minimo:
                    minimo = len(tablero[i][j])
                    fila=i
                    col=j
    return (fila,col)
########################################################################
def podaX(tablero,i,j,valor):
    global matrizBooleana
    tablero[i][j]=valor
    contador = 1
    #izquierda
    while(matrizBooleana[i][j-contador]!=0):
        if(type(tablero[i][j-contador])==list):
            if valor in tablero[i][j-contador]:
                tablero[i][j-contador].remove(valor)
        contador+=1
    contador = 1
    #derecha
    while((matrizBooleana[i][j+contador]!=0) and (j+contador<len(matrizBooleana))):
        if(type(tablero[i][j+contador])==list):
            if valor in tablero[i][j+contador]:
                tablero[i][j+contador].remove(valor)
        contador+=1
    contador = 1
    #arriba
    while(matrizBooleana[i-contador][j]!=0):
        if(type(tablero[i-contador][j])==list):
            if valor in tablero[i-contador][j]:
                tablero[i-contador][j].remove(valor)
        contador+=1
    contador = 1
    #abajo
    while((matrizBooleana[i+contador][j]!=0) and (i+contador<len(matrizBooleana))):
        if(type(tablero[i+contador][j])==list):
            if valor in tablero[i+contador][j]:
                tablero[i+contador][j].remove(valor)
        contador+=1
    return tablero
########################################################################

#########################################################################

matrizBooleana = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

tablero1 = [[[0, 0], [0, 0], [5, 0], [0, 0], [13, 0], [21, 0], [45, 0], [12, 0], [7, 0], [14, 0], [0, 0]], [[0, 0], [17, 5], 0, [16, 27], 0, 0, 0, 0, 0, 0, [0, 0]], [[0, 3], 0, [0, 36], 0, 0, 0, 0, 0, 0, 0, [0, 0]], [[0, 9], 0, [9, 25], 0, 0, 0, 0, [19, 0], [28, 0], [18, 0], [0, 0]], [[0, 8], 0, 0, [0, 0], [0, 29], 0, 0, 0, 0, 0, [0, 0]], [[0, 0], [13, 6], 0, [11, 0], [16, 27], 0, 0, 0, 0, 0, [0, 0]], [[0, 4], 0, [0, 8], 0, 0, [14, 17], 0, 0, 0, 0, [0, 0]], [[0, 1], 0, [6, 32], 0, 0, 0, 0, 0, 0, [3, 0], [0, 0]], [[0, 14], 0, 0, [7, 18], 0, 0, 0, [8, 8], 0, 0, [0, 0]], [[0, 0], [0, 0], [0, 7], 0, [0, 17], 0, 0, 0, [0, 1], 0, [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]

matrizPrePoda = [[[0, 0], [0, 0], [[5, [5]], 0], [0, 0], [[13, [[1, 3, 9], [1, 4, 8], [1, 5, 7], [2, 3, 8], [2, 4, 7], [2, 5, 6], [3, 4, 6]]], 0], [[21, [[1, 2, 3, 6, 9], [1, 2, 3, 7, 8], [1, 2, 4, 5, 9], [1, 2, 4, 6, 8], [1, 2, 5, 6, 7], [1, 3, 4, 5, 8], [1, 3, 4, 6, 7], [2, 3, 4, 5, 7]]], 0], [[45, [[1, 2, 3, 4, 5, 6, 7, 8, 9]]], 0], [[12, [[3, 9], [4, 8], [5, 7]]], 0], [[7, [[1, 6], [2, 5], [3, 4]]], 0], [[14, [[5, 9], [6, 8]]], 0], [0, 0]], [[0, 0], [[17, [[1, 7, 9], [2, 6, 9], [2, 7, 8], [3, 5, 9], [3, 6, 8], [4, 5, 8], [4, 6, 7]]], [5, [5]]], [5], [[16, [[7, 9]]], [27, [[1, 2, 3, 4, 8, 9], [1, 2, 3, 5, 7, 9], [1, 2, 3, 6, 7, 8], [1, 2, 4, 5, 6, 9], [1, 2, 4, 5, 7, 8], [1, 3, 4, 5, 6, 8], [2, 3, 4, 5, 6, 7]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0]], [[0, [3, [3]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, [36, [[1, 2, 3, 6, 7, 8, 9], [1, 2, 4, 5, 7, 8, 9], [1, 3, 4, 5, 6, 8, 9], [2, 3, 4, 5, 6, 7, 9]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0]], [[0, [9, [9]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[9, [[1, 8], [2, 7], [3, 6], [4, 5]]], [25, [[1, 7, 8, 9], [2, 6, 8, 9], [3, 5, 8, 9], [3, 6, 7, 9], [4, 5, 7, 9], [4, 6, 7, 8]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[19, [[1, 2, 7, 9], [1, 3, 6, 9], [1, 3, 7, 8], [1, 4, 5, 9], [1, 4, 6, 8], [1, 5, 6, 7], [2, 3, 5, 9], [2, 3, 6, 8], [2, 4, 5, 8], [2, 4, 6, 7], [3, 4, 5, 7]]], 0], [[28, [[1, 3, 7, 8, 9], [1, 4, 6, 8, 9], [1, 5, 6, 7, 9], [2, 3, 6, 8, 9], [2, 4, 5, 8, 9], [2, 4, 6, 7, 9], [2, 5, 6, 7, 8], [3, 4, 5, 7, 9], [3, 4, 6, 7, 8]]], 0], [[18, [[1, 8, 9], [2, 7, 9], [3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]]], 0], [0, 0]], [[0, [8, [[1, 7], [2, 6], [3, 5]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8], [0, 0], [0, [29, [[1, 4, 7, 8, 9], [1, 5, 6, 8, 9], [2, 3, 7, 8, 9], [2, 4, 6, 8, 9], [2, 5, 6, 7, 9], [3, 4, 5, 8, 9], [3, 4, 6, 7, 9], [3, 5, 6, 7, 8]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0]], [[0, 0], [[13, [[1, 3, 9], [1, 4, 8], [1, 5, 7], [2, 3, 8], [2, 4, 7], [2, 5, 6], [3, 4, 6]]], [6, [6]]], [1, 2, 3, 4, 5, 6, 7, 8], [[11, [[2, 9], [3, 8], [4, 7], [5, 6]]], 0], [[16, [[1, 6, 9], [1, 7, 8], [2, 5, 9], [2, 6, 8], [3, 4, 9], [3, 5, 8], [3, 6, 7], [4, 5, 7]]], [27, [[1, 2, 7, 8, 9], [1, 3, 6, 8, 9], [1, 4, 5, 8, 9], [1, 4, 6, 7, 9], [1, 5, 6, 7, 8], [2, 3, 5, 8, 9], [2, 3, 6, 7, 9], [2, 4, 5, 7, 9], [2, 4, 6, 7, 8], [3, 4, 5, 6, 9], [3, 4, 5, 7, 8]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0]], [[0, [4, [4]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, [8, [[1, 7], [2, 6], [3, 5]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[14, [[1, 4, 9], [1, 5, 8], [1, 6, 7], [2, 3, 9], [2, 4, 8], [2, 5, 7], [3, 4, 7], [3, 5, 6]]], [17, [[1, 2, 5, 9], [1, 2, 6, 8], [1, 3, 4, 9], [1, 3, 5, 8], [1, 3, 6, 7], [1, 4, 5, 7], [2, 3, 4, 8], [2, 3, 5, 7], [2, 4, 5, 6]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0]], [[0, [1, [1]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[6, [6]], [32, [[1, 2, 5, 7, 8, 9], [1, 3, 4, 7, 8, 9], [1, 3, 5, 6, 8, 9], [1, 4, 5, 6, 7, 9], [2, 3, 4, 6, 8, 9], [2, 3, 5, 6, 7, 9], [2, 4, 5, 6, 7, 8]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[3, [[1, 2]]], 0], [0, 0]], [[0, [14, []]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [6], [[7, [7]], [18, [[1, 8, 9], [2, 7, 9]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[8,[8]], [8, [[1, 7], [2, 6]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 6, 7], [0, 0]], [[0, 0], [0, 0], [0, [7, [7]]], [7], [0, [17, [[1, 7, 9], [2, 6, 9], [2, 7, 8]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 6, 7, 8, 9], [0, [1, [1]]], [1, 2], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]

#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************


def posCombinations(spaces):
    result = 1
    currentMultiplier = 9

    for x in range(0, spaces):
        result = result * currentMultiplier
        currentMultiplier -= 1

    return result

def revisaFilCol(t1):
    if len(t1)>11:
        time.sleep(1*(len(t1)+40))
        redraw(parcialSolution)
    else:
        p = multiprocessing.Process(target=backtracking, name="Backtracking", args=(t1))
        p.start()
        time.sleep(1*(len(t1)+7))
        if p.is_alive():
            p.terminate()
            redraw(parcialSolution)
    
###############################################################

'''
Function to get the minimum number using x given spaces
spaces: amount of spaces to be used
'''
def minNumber(spaces):
    result = 0
    for x in range(1, spaces + 1):
        result += x
    return result
###############################################################

'''
Function to get the maximum number using x given spaces
spaces: amount of spaces to be used 
'''
def maxNumber(spaces):
    result = 0
    for x in range(10 - spaces, 10):
        result += x
    return result
###############################################################

'''
Function to check if a number is in a given vector
number: number to check if it's in the vector
vector: vector we want to check the presence of the number
'''
def checkPresence(number, vector):
    if number in vector:
        return True
    else:
        return False
###############################################################

'''
Function to get the valid(s) vectors that sum up a given number
numbers: must be [1,2,3,4,5,6,7,8,9]
target: The desired sum we want to reach
allowedSpaces: the amount of numbers you can use to reach the desired number
finalResult: must start as []
partial: must start as []
'''
def combinaciones(numbers, target, allowedSpaces, finalResult, partial):
    # Special case for one space number
    if allowedSpaces == 1:
        return [target]
    
    # We have to make sure we don't use the target number
    if target in numbers:
        numbers.remove(target)
    
    # We check the amount of numbers we have used isn't out of range
    if len(partial) <= allowedSpaces:
        
        s = sum(partial)

        # check if the partial sum is equals to target and uses the right amount of numbers
        if s == target and len(partial) == allowedSpaces:
            # We add the partial result to the final result
            finalResult.append(partial)
            
        if s >= target:
            return # if we reach the number we stop

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i+1:]
            combinaciones(remaining, target, allowedSpaces, finalResult, partial + [n])

        return finalResult
#################################################################################################

'''
Function to check if a vectors numbers are in another vector
vector_1: the vector we want to check if the numbers are in vector_2, must be a list
vector_2: where we check if the number are in, must be a list
returns: True if we can delete the given vector, False if we can't
'''
def checkPosRemove(vector_1, vector_2):
    if type(vector_1) == int or type(vector_2) == int:
        return False
    for x in range(0, len(vector_1)):
        if vector_1[x] in vector_2:
            return False
    return True
###############################################################

'''
Function to delete certain elements from a vector
returns: the vector with the desired indexes deleted
'''
def removeVector(indexes, vector):
    indexCorrector = 0
    for x in range(0, len(indexes)):
        del vector[x - indexCorrector]
        indexCorrector += 1
    return vector
###############################################################

'''
Function to delete posible uses of vectors
returns: Both vectors without the comb. of numbers they can't use
'''
def removePosSolutionPre(vector_1, vector_2):
    if len(vector_1) == 1 and len(vector_2) > 1:

        indexCorrector = 0
        for index in range(0, len(vector_2)):
            if checkPosRemove(vector_2[index - indexCorrector], vector_1[0]):
                del vector_2[index - indexCorrector]
                indexCorrector += 1
        return [vector_1, vector_2]

    elif len(vector_2) == 1 and len(vector_1) > 1:

        indexCorrector = 0
        for index in range(0, len(vector_1)):
            if checkPosRemove(vector_1[index - indexCorrector], vector_2[0]):
                del vector_1[index - indexCorrector]
                indexCorrector += 1
        return [vector_1, vector_2]
    else:
        return [vector_1, vector_2]
###############################################################################

'''
Funcion para eliminar posibles combinaciones durante
el backTracking
'''
def removePosSolutionRun(vector_1, tablero):
    if len(vector_1[0]) <= (len(tablero) - tablero.count(0)):
    # Si se cumple la condicion empezamos a tratar de eliminar los
    # posibles numeros por usar

        new_vectors = removePosSolutionPre(vector_1, [tablero])
        vector_1 = new_vectors[0]
        return vector_1
    else:
        return vector_1
###############################################################

'''
Funcion que cuenta cuantos espacios son para cada
numero en el kakuro
'''
def cuentaEspacios(kakuro, i, j, direccion):
    # Si es para una fila
    if direccion == 1:
        contador = 0
        for x in range(j + 1, len(kakuro[i])):
            if kakuro[i][x] == 0:
                contador += 1
            else:
                break # Para de contar espacios ya que no hay mas
        return contador
    
    # Si es para una columna
    elif direccion == 2:
        contador = 0
        for x in range(i + 1, len(kakuro)):
            if kakuro[x][j] == 0:
                contador += 1
            else:
                break
        return contador
###############################################################
    

'''
Funcion que se corre antes del backtracking
para saber las combinaciones de cada numero
'''
def preBackTracking(kakuro):
    for i in range(0, len(kakuro)):
        for j in range(0, len(kakuro[0])):
            # No hacemos nada sobre las casillas negras
            if kakuro[i][j] == [0,0]:
                pass
                # No se hace nada
            elif kakuro[i][j] == 0:
                # No se hace nada
                pass
            else:
                # Se analiza para la fila y la columna si lo hay en ambas o
                # solo una
                if kakuro[i][j][0] == 0:
                    # No hace nada para la columna
                    pass
                else:
                    # Empieza el analisis para la columna
                    espacios = cuentaEspacios(kakuro, i, j, 2)
                    posibilidades = combinaciones([1,2,3,4,5,6,7,8,9],
                                                  kakuro[i][j][0], espacios,
                                                  [],[])
                    kakuro[i][j][0] = [kakuro[i][j][0], posibilidades]
                if kakuro[i][j][1] == 0:
                    # No hace nada para la fila
                    pass
                else:
                    espacios = cuentaEspacios(kakuro, i, j, 1)
                    posibilidades = combinaciones([1,2,3,4,5,6,7,8,9],
                                                  kakuro[i][j][1], espacios,
                                                  [],[])
                    kakuro[i][j][1] = [kakuro[i][j][1], posibilidades]
    return kakuro
###############################################################
                
"""
Devuelve una nueva lista resultado de insertar
x dentro de lst en la posicion i.
"""
def inserta(x, lst, i):
    return lst[:i] + [x] + lst[i:]
###############################################################

"""
Devuelve una lista con el resultado de
insertar x en todas las posiciones de lst.  
"""
def inserta_multiple(x, lst):
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]
#------------------------------------------------------------------------------------------------------------

"""
Calcula y devuelve una lista con todas las
permutaciones posibles que se pueden hacer
con los elementos contenidos en c.
"""
def permuta(c):
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],[])
#------------------------------------------------------------------------------------------------------------

'''
Funcion para saber si un campo de una fila se comparte con una columna
retorna: None si no se comparte
         Una lista con el indice del numero de la fila y el numero de la columna
'''
def interseccion(i_entrada, j_entrada, kakuro):
    new_i = i_entrada - 1
    for x in range(0, len(kakuro[0])):
        if kakuro[new_i][j_entrada] == 0:
            new_i -= 1
        elif type(kakuro[new_i][j_entrada]) == set:
            new_i -= 1
        elif kakuro[new_i][j_entrada][0] == 0:
            # Si no encuentra una interseccion devuelve none
            return None
        else:
            return [new_i, j_entrada]
#------------------------------------------------------------------------------------------------------------

'''
Funcion para ejecutar toda la pre poda
antes 
'''
def fullPrePoda(kakuro):
    kakuro = preBackTracking(kakuro)
    kakuro_comb = kakuro
    # Desde uno porque en la primera fila no se pueden poner numeros
    # el - 1 es porque la ultima columna es de ceros y la ultima fila tambien 
    for i in range(1, len(kakuro)):
        for j in range(0, len(kakuro[0])):
            # En este caso si ejecutamos la pre poda
            if kakuro[i][j] == 0:
                kakuro[i][j] = posibles(i, j, kakuro_comb)
            elif kakuro [i][j] == [0,0]:
                pass
            elif kakuro[i][j][1] == 0:
                pass
            elif kakuro[i][j][1][0] != 0:
                for x in range(j + 1, len(kakuro[0])):
                    # Empezamos a probar con cada espacio blanco
                    if kakuro[i][x] == 0:
                        # Si el espacio esta en blanco probamos las intersecciones
                        # Vemos si tiene alguna interseccion
                        lista_analisis = interseccion(i, x, kakuro)
                        # Si tiene alguna interseccion se hace el analisis
                        if lista_analisis != None:
                            posV2 = lista_analisis
                            nuevos_vectores = removePosSolutionPre(
                                kakuro[i][j][1][1],
                                kakuro[posV2[0]][posV2[1]][0][1])
                            # ahora cambiamos los vectores
                            kakuro[i][j][1][1] = nuevos_vectores[0]
                            kakuro[posV2[0]][posV2[1]][0][1] = nuevos_vectores[1]
                    
            else:
                pass


    for i in range(len(kakuro[0])):
        for j in range (len(kakuro[0])):
            if type(kakuro[i][j])==set:
                kakuro[i][j]= list(kakuro[i][j])
                   
    return kakuro
#------------------------------------------------------------------------------------------------------------

def posibles(i_entrada, j_entrada, kakuro):
    nuevo_conjunto = set()
    new_i = i_entrada - 1
    #print("Arriba")
    for x in range(0, len(kakuro[0])):
        if kakuro[new_i][j_entrada] == 0:
            new_i -= 1
        elif type(kakuro[new_i][j_entrada]) == set:
            new_i -= 1
        elif kakuro[new_i][j_entrada][0] == 0:
            # Si no encuentra una interseccion para
            break
        else:
            for x in range(0, len(kakuro[new_i][j_entrada][0][1])):
                #print(kakuro[new_i][j_entrada][0][1])
                conjunto_temp = kakuro[new_i][j_entrada][0][1][x]
                if type(conjunto_temp) == int:
                    conjunto_temp = {conjunto_temp}
                else:
                    conjunto_temp = set(conjunto_temp)
                # Unimos los conjuntos
                nuevo_conjunto = nuevo_conjunto | conjunto_temp
    new_j = j_entrada - 1
    #print("Abajo")
    for y in range(0, len(kakuro)):
        if kakuro[i_entrada][new_j] == 0:
            new_j -= 1
        elif type(kakuro[i_entrada][new_j]) == set:
            new_j -= 1
        elif kakuro[i_entrada][new_j][1] == 0:
            # Si no encuentra una interseccion para
            break
        else:
            for x in range(0, len(kakuro[i_entrada][new_j][1][1])):
                #print(kakuro[i_entrada][new_j][1][1])
                conjunto_temp = kakuro[i_entrada][new_j][1][1][x]
                if type(conjunto_temp) == int:
                    conjunto_temp = {conjunto_temp}
                else:
                    conjunto_temp = set(conjunto_temp)
                # Unimos los conjuntos
                nuevo_conjunto = nuevo_conjunto | conjunto_temp
    return nuevo_conjunto
#------------------------------------------------------------------------------------------------------------
               
    
    
def matrizEditable(matrizKakuroFinal):
    matrizBooleana = []
    matrizBooleana = [[0] * len(matrizKakuroFinal) for i in range(len(matrizKakuroFinal))]
    for i in range(len(matrizKakuroFinal[0])):
        for j in range(len(matrizKakuroFinal[0])):
            if type(matrizKakuroFinal[i][j])==list:
                matrizBooleana[i][j]=0
            else: 
                matrizBooleana[i][j]=1
    return matrizBooleana
            

#Manejo de archivos para abrir y guardar kakuros-------------------------------------------------------------------------------------------------
def saveFile(matrizKakuro):
    f = tkFileDialog.asksaveasfile(mode= 'w', defaultextension= '.txt')
    if f is None:
        return
    txtSave = str(matrizKakuro)
    f.write(txtSave)
    f.close()
    tkMessageBox.showinfo("Manejo de Arhivos", "Kakuro Guardado")
    
    
def openFile():
    a= ""
    matrizGuardada = []
    filename = tkFileDialog.askopenfile(filetypes=[("Text files","*.txt")])
    txt = filename.read()
    matrizGuardada = ast.literal_eval(txt)
    redraw(matrizGuardada)
    filename.close()
    
#---------------------------------------------------------------------------------------------------------------------------------------------------


#Dibuja el tablero en la pantalla----------------------------------------------------------------------------
def redraw(matrix):


    gameframe.destroy()  
    global gameframe
    gameframe = tk.Frame(window)
    gameframe.pack()
    
    for i,row in enumerate(matrix):
        for j,column in enumerate(row):
            if type(matrix[i][j])!=list:   
                L = tk.Label(gameframe,text=(matrix[i][j]),bg= "gray")
                L.grid(row=i,column=j,padx='1',pady='1')
            else:
                L = tk.Label(gameframe,text=(matrix[i][j]),bg= "black", fg= "gray")
                L.grid(row=i,column=j,padx='1',pady='1')
#------------------------------------------------------------------------------------------------------------
                          

#Genera las tuplas correspondientes a la sumas de las filas y columnas---------------------------------------------------------------------------
def generarTuplas(matrizFinal):
    global parcialSolution
    parcialSolution = [] 
    for i in range(len(matrizFinal[0])):
        for j in range(len(matrizFinal[0])):
            if matrizFinal[i][j]==0 :
                matrizFinal[i][j]= [0,0]
            if matrizFinal[i][j]=='0':
                matrizFinal[i][j]= [0,0]
                
    for i in range(len(matrizFinal[0])-1):
        sumaColumna = 0
        for j in range(len(matrizFinal[0])-1):
            sumaFila =0
            sumaColumna=0
            if type(matrizFinal[i][j]) == list:
                (matrizFinal[i][j])[1] = verificarTuplaFila(matrizFinal,i,j,sumaFila)
                (matrizFinal[i][j])[0] = verificarTuplaCol(matrizFinal,i,j,sumaColumna)

                
            else:
                pass
    parcialSolution = copy.deepcopy(matrizFinal)
    
            
    for i in range(len(matrizFinal[0])-1):
        for j in range(len(matrizFinal[0])-1):
            if type(matrizFinal[i][j])!=list:
                matrizFinal[i][j]=0
            else:
                pass
            
    return matrizFinal

def verificarTuplaCol(matrizFinal, i, j, sumaColumna):
    if i >= (len(matrizFinal[0])-2):
        while type(matrizFinal[i][j]) != list:
            sumaColumna+= matrizFinal[i][j]
        return sumaColumna
    else:
        i+=1
        while type(matrizFinal[i][j]) != list:
            sumaColumna+= matrizFinal[i][j]
            i+=1
        return sumaColumna 
    
def verificarTuplaFila(matrizFinal, i, j, sumaFila):
    if j >= (len(matrizFinal[0])-2):
        while type(matrizFinal[i][j]) != list:
            sumaFila+= matrizFinal[i][j]
        return sumaFila
    else:
        j+=1
        while type(matrizFinal[i][j]) != list:
            sumaFila+= matrizFinal[i][j]
            j+=1
        return sumaFila 

#-------------------------------------------------------------------------------------------------------------------------------------------------



#Obtiene la interseccion entre una fila y una columna--------------------------------------------------------------------------------------------
def interseccionGenerador(listaRandomCol,listaRandomFila,matrizFinal):
    p = listaRandomCol[:]
    for i in range(0,len(listaRandomCol)):
        if(listaRandomCol[i] not in listaRandomFila):
            p.remove(listaRandomCol[i])
    if p ==[]:
        p=[0]
        
    
    return p
#-----------------------------------------------------------------------------------------------------------------------------------------------
    
    

#Obtiene las combinaciones necesarias para generar un kakuro con solucion------------------------------------------------------------------------
def revisarCasillasBlanca(matrizFinal, numeroFilas):
    listaRevision = ['0']*(numeroFilas+1) #Columna temporal para terminar de revisar
    
    for i in range(numeroFilas): #Columna temporal para terminar de revisar
        matrizFinal[i].append('0')
    matrizFinal.append(listaRevision)
        
    for i in range(1,len(matrizFinal[0])):
        for j in range(1, len(matrizFinal[0])):
            listaRandomFila = [1,2,3,4,5,6,7,8,9]
            listaRandomCol = [1,2,3,4,5,6,7,8,9]
            if matrizFinal[i][j]!='0':
                listaRandomCol= verificarSumaColumna(matrizFinal, i, j, listaRandomCol)
                listaRandomFila= verificarSumaFila(matrizFinal, i, j, listaRandomFila)
                listaRandom = interseccionGenerador(listaRandomCol,listaRandomFila, matrizFinal)
                if len(listaRandom)==1:
                    numeroCasilla = 0
                else:
                    numeroCasilla = random.randint(0,(len(listaRandom))-1)
                matrizFinal[i][j]= listaRandom[numeroCasilla]
    
    matrizTuplas = generarTuplas(matrizFinal)
    return matrizTuplas

def verificarSumaFila(matrizFinal,i,j,listaPos):
        while matrizFinal[i][j]!='0':
            j-=1
        j+=1
        while matrizFinal[i][j]!='0' :
            if matrizFinal[i][j] in listaPos :
                listaPos.remove(matrizFinal[i][j])
            j+=1
            
        return listaPos

        
def verificarSumaColumna(matrizFinal,i,j,listaPos):
        while matrizFinal[i][j]!='0':
            i-=1
        i+=1
        while matrizFinal[i][j]!='0' :
            if matrizFinal[i][j] in listaPos :
                listaPos.remove(matrizFinal[i][j])
            i+=1
        return listaPos
#----------------------------------------------------------------------------------------------------------------------------------------------    
    
    
#Revisa si existen casillas blancas entre dos negras y la elimina-----------------------------------------

def revisarAdyacencias(matrizAdyacencias):
    
    for i in range(1,len(matrizAdyacencias[0])-1):
        for j in range(1,len(matrizAdyacencias[0])-1):
            if matrizAdyacencias[i][j]=='1' and matrizAdyacencias[i][j-1]=='0' and matrizAdyacencias[i][j+1]=='0' and matrizAdyacencias[i-1][j]=='0' and matrizAdyacencias[i+1][j]=='0':
                matrizAdyacencias[i][j]='0'
              
    matrizTupla = revisarCasillasBlanca(matrizAdyacencias, len(matrizAdyacencias[0]))
    return matrizTupla

#--------------------------------------------------------------------------------------------------------

#Valida si una fila o una columna tiene mas de 9 casillas------------------------------------------
def validar9Casillas(matrizKakuro):

    for i in range(1,len(matrizKakuro[0])):
        numeroBlancasFila =0
        for j in range(1,len(matrizKakuro[0])):
            if matrizKakuro[i][j]== '1' :
                numeroBlancasFila+=1
                if numeroBlancasFila>9:
                    matrizKakuro[i][j]='0'
                    numeroBlancasFila = 0
                else:
                    pass
            else:
                numeroBlancasFila=0     


    for i in range(1,len(matrizKakuro[0])):
        numeroBlancasColumna= 0
        for j in range(1,len(matrizKakuro[0])):
            if matrizKakuro[j][i]=='1':
                numeroBlancasColumna+=1
                if numeroBlancasColumna>9:
                    matrizKakuro[j][i]='0'
                    numeroBlancasColumna= 0
                else:
                    pass
            else:
                numeroBlancasColumna =0
        
    matrizAdyacencias = revisarAdyacencias(matrizKakuro)  
    return matrizAdyacencias  
     
#------------------------------------------------------------------------                

#Genera casillas aleatorias con una pequena probabilidad---------------------------------------------
def generateRndm():
    casillas =['0','1']
    pesos = [0.3,0.7]
    resultado= []
    
    for e, p in zip(casillas, pesos):
        resultado += [e] * int(p * 100)
        
    return random.choice(resultado)
#-----------------------------------------------------------------------------------------------------
    
#Funcion que una matriz del tamano dado---------------------------------------------------------------
def crearMatriz(filas, columnas):
    global matrizRevision
    matrizInicial = []
    matrizRevision= []
    global matrizKakuroFinal 
    global matrizBooleana
    a = ""
    b=  ""
    #Crea la matriz del tamano indicado
    for k in range(filas):
        matrizInicial.append([1]*columnas)
    #Inicializa toda la primera columna y fila con campos en negro    
    for i in range(filas):
        matrizInicial[0][i]=0
        matrizInicial[i][0]=0
        
    #Genera espacios aleatorios en el kakuro    
    for k in range(1,filas):
        for j in range(1,columnas):
            matrizInicial[k][j]= generateRndm()
     
    #Llama a funcion para validar espacios         
    matrizFinal=   validar9Casillas(matrizInicial) #Obtiene todas las validaciones respectivas
    matrizKakuroFinal = matrizFinal[:]
    redraw(matrizKakuroFinal)
    matrizBooleana =  matrizEditable(matrizKakuroFinal)
    for k in range(filas):
        for j in range(columnas):
            a+=str(matrizBooleana[k][j])+'\t'
        print (a)
        a=""
    matrizRevision =  fullPrePoda(matrizFinal)


#--------------------------------------------------------------------------------------         

#Funcion que obtiene del spinbox el tamano del kakuro----------------------------------
def obtener(): #Llama a funcion que crea la matriz
    if value.get()== "10x10":
        crearMatriz(10, 10)
    elif value.get()== "11x11":
        crearMatriz(11, 11)
    elif value.get()== "12x12":
        crearMatriz(12, 12)
    elif value.get()== "13x13":
        crearMatriz(13, 13)
    elif value.get()== "14x14":
        crearMatriz(14, 14)
    elif value.get()== "15x15":
        crearMatriz(15, 15)
    elif value.get()== "16x16":
        crearMatriz(16, 16)
    elif value.get()== "17x17":
        crearMatriz(17, 17)
    elif value.get()== "18x18":
        crearMatriz(18, 18)
    elif value.get()== "19x19":
        crearMatriz(19, 19)
        
    else:
        crearMatriz(20, 20)
#--------------------------------------------------------------------------------------

#Ventana principal del programa--------------------------------------------------------------------------------------------------------------------------------------
x1=10
y1=10
window = tk.Tk()
value = StringVar()
window.title("Solucionador de Kakuros")
window.geometry("1024x600")
gameframe = tk.Frame(window)
gameframe.pack()
kSize =  Spinbox(window,values = ("10x10","11x11","12x12","13x13","14x14","15x15","16x16","17x17","18x18","19x19","20x20"), textvariable= value).place(x=420, y= 500)
buttonCreate = Button(window, text= "Generar Kakuro", command = obtener).place(x=375, y=530)  
buttonSolve = Button(window, text = "Resolver Kakuro",command = lambda:revisaFilCol(matrizRevision)).place(x=475, y=530)
buttonGuardar = Button(window, text = "Guardar Kakuro Generado", command = lambda: saveFile(matrizKakuroFinal)).place(x=220, y=530)
buttonAbrir  = Button(window, text = "Abrir Kakuro Generado", command= lambda: openFile()).place(x=580, y=530)
mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------









