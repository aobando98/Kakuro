'''
Python class to get the solution of a kakuro puzzle
'''
'''
import random
import Tkinter as tk
from Tkinter import StringVar, Tk, Spinbox, Button
from _tkinter import mainloop
from cgitb import text
from __builtin__ import str
from pipes import stepkinds
from _ast import Str
from getpass import fallback_getpass
import tkFileDialog
import tkMessageBox

#Variables globales--------------

global matrizBooleana
global gameframe
#--------------------------------
matrizKakuroFinal =""
'''

###############################################################
'''
Function to get the posible combinations using x given spaces
'''
def posCombinations(spaces):
    result = 1
    currentMultiplier = 9

    for x in range(0, spaces):
        result = result * currentMultiplier
        currentMultiplier -= 1

    return result
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
x dentro de lst en la posición i.
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
###############################################################

"""
Calcula y devuelve una lista con todas las
permutaciones posibles que se pueden hacer
con los elementos contenidos en c.
"""
def permuta(c):
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
               [])
###############################################################

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
###############################################################

'''
Funcion para ejecutar toda la pre poda
antes 
'''
def fullPrePoda(kakuro):
    kakuro = preBackTracking(kakuro)
    kakuro_comb = kakuro
    # Desde uno porque en la primera fila no se pueden poner numeros 
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
################################################################################

def posibles(i_entrada, j_entrada, kakuro):
    nuevo_conjunto = set()
    new_i = i_entrada - 1
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
                conjunto_temp = kakuro[new_i][j_entrada][0][1][x]
                if type(conjunto_temp) == int:
                    conjunto_temp = {conjunto_temp}
                else:
                    conjunto_temp = set(conjunto_temp)
                # Unimos los conjuntos
                nuevo_conjunto = nuevo_conjunto | conjunto_temp
    new_j = j_entrada - 1
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
                conjunto_temp = kakuro[i_entrada][new_j][1][1][x]
                if type(conjunto_temp) == int:
                    conjunto_temp = {conjunto_temp}
                else:
                    conjunto_temp = set(conjunto_temp)
                # Unimos los conjuntos
                nuevo_conjunto = nuevo_conjunto | conjunto_temp
    return nuevo_conjunto
################################################################################

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

def verificarTuplaCol(kakuro, i, j, sumaColumna):
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
    
def verificarTuplaFila(kakuro, i, j, sumaFila):
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
                    if verificarTuplaCol(kakuro, i, j, kakuro[i][j][0][0]):
                        pass
                    else:
                        return False
                if kakuro[i][j][1] == 0:
                    pass
                else:
                    # Se ejecuta la revision de la fila
                    if verificarTuplaFila(kakuro, i, j, kakuro[i][j][1][0]):
                        pass
                    else:
                        return False
    return True
            
             
            
        

        
    

