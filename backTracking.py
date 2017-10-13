'''
Python class to get the solution of a kakuro puzzle
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

def cuentaEspacios(kakuro, i, j, direccion):
    # Si es para una fila
    if direccion == 1:
        contador = 0
        for x in range(j + 1, len(kakuro[i])):
            print("Fila")
            print("Elemnto" , i,x, "=", kakuro[i][x])
            if kakuro[i][x] == 0:
                contador += 1
            else:
                break # Para de contar espacios ya que no hay mas
        return contador
    
    # Si es para una columna
    elif direccion == 2:
        contador = 0
        for x in range(i + 1, len(kakuro)):
            print("Columna")
            print("Elemnto", x,j, "=", kakuro[x][j])
            if kakuro[x][j] == 0:
                contador += 1
            else:
                break
        return contador
    

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

        
    

