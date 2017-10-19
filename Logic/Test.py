import copy

def backtracking(tablero):
    chkTablero = copy.deepcopy(tablero)
    if checkKakuro(modificarTablero(chkTablero)):
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
'''
def juegoPerdido2(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if(matrizBooleana[i][j]==0):
                if(chkRow2(tablero,i,j)==False or chkCol2(tablero,i,j)==False):
                    return True
    return False
'''
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
                #print(tablero[i][j])
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
'''
#tablero = [[[0, 0], [3, 0], [0, 0], [14, 0], [6, 0], [0, 0], [5, 0], [17, 0], [10, 0], [9, 0], [0, 0]], [[0, 3], 0, [33, 13], 0, 0, [44, 24], 0, 0, 0, 0, [0, 0]], [[0, 0], [35, 17], 0, 0, 0, 0, [20, 17], 0, 0, [0, 0], [0, 0]], [[0, 13], 0, 0, [29, 0], [14, 7], 0, 0, [32, 0], [12, 0], [7, 0], [0, 0]], [[0, 45], 0, 0, 0, 0, 0, 0, 0, 0, 0, [0, 0]], [[0, 45], 0, 0, 0, 0, 0, 0, 0, 0, 0, [0, 0]], [[0, 43], 0, 0, 0, 0, 0, 0, 0, 0, [0, 0], [0, 0]], [[0, 16], 0, 0, 0, [5, 7], 0, [0, 3], 0, [0, 0], [0, 0], [0, 0]], [[0, 4], 0, [9, 13], 0, 0, 0, [6, 7], 0, [0, 0], [6, 0], [0, 0]], [[0, 33], 0, 0, 0, 0, 0, 0, [0, 0], [0, 6], 0, [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
#matrizBooleana = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#tablero = reemplazar(tablero)
#tablero[4][5] = 5
#talbero = podaX(tablero,4,5,5)
xxx = backtracking(tablero)
for l in xxx:
    print(l)

for x in range(len(tablero)):
    print(tablero[4][x])
print('---------------------------------')
for x in range(len(tablero)):
    print(tablero[x][5])

'''
#########################################################################

matrizBooleana = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

tablero1 = [[[0, 0], [0, 0], [5, 0], [0, 0], [13, 0], [21, 0], [45, 0], [12, 0], [7, 0], [14, 0], [0, 0]], [[0, 0], [17, 5], 0, [16, 27], 0, 0, 0, 0, 0, 0, [0, 0]], [[0, 3], 0, [0, 36], 0, 0, 0, 0, 0, 0, 0, [0, 0]], [[0, 9], 0, [9, 25], 0, 0, 0, 0, [19, 0], [28, 0], [18, 0], [0, 0]], [[0, 8], 0, 0, [0, 0], [0, 29], 0, 0, 0, 0, 0, [0, 0]], [[0, 0], [13, 6], 0, [11, 0], [16, 27], 0, 0, 0, 0, 0, [0, 0]], [[0, 4], 0, [0, 8], 0, 0, [14, 17], 0, 0, 0, 0, [0, 0]], [[0, 1], 0, [6, 32], 0, 0, 0, 0, 0, 0, [3, 0], [0, 0]], [[0, 14], 0, 0, [7, 18], 0, 0, 0, [8, 8], 0, 0, [0, 0]], [[0, 0], [0, 0], [0, 7], 0, [0, 17], 0, 0, 0, [0, 1], 0, [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]

matrizPrePoda = [[[0, 0], [0, 0], [[5, [5]], 0], [0, 0], [[13, [[1, 3, 9], [1, 4, 8], [1, 5, 7], [2, 3, 8], [2, 4, 7], [2, 5, 6], [3, 4, 6]]], 0], [[21, [[1, 2, 3, 6, 9], [1, 2, 3, 7, 8], [1, 2, 4, 5, 9], [1, 2, 4, 6, 8], [1, 2, 5, 6, 7], [1, 3, 4, 5, 8], [1, 3, 4, 6, 7], [2, 3, 4, 5, 7]]], 0], [[45, [[1, 2, 3, 4, 5, 6, 7, 8, 9]]], 0], [[12, [[3, 9], [4, 8], [5, 7]]], 0], [[7, [[1, 6], [2, 5], [3, 4]]], 0], [[14, [[5, 9], [6, 8]]], 0], [0, 0]], [[0, 0], [[17, [[1, 7, 9], [2, 6, 9], [2, 7, 8], [3, 5, 9], [3, 6, 8], [4, 5, 8], [4, 6, 7]]], [5, [5]]], [5], [[16, [[7, 9]]], [27, [[1, 2, 3, 4, 8, 9], [1, 2, 3, 5, 7, 9], [1, 2, 3, 6, 7, 8], [1, 2, 4, 5, 6, 9], [1, 2, 4, 5, 7, 8], [1, 3, 4, 5, 6, 8], [2, 3, 4, 5, 6, 7]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0]], [[0, [3, [3]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, [36, [[1, 2, 3, 6, 7, 8, 9], [1, 2, 4, 5, 7, 8, 9], [1, 3, 4, 5, 6, 8, 9], [2, 3, 4, 5, 6, 7, 9]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0]], [[0, [9, [9]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[9, [[1, 8], [2, 7], [3, 6], [4, 5]]], [25, [[1, 7, 8, 9], [2, 6, 8, 9], [3, 5, 8, 9], [3, 6, 7, 9], [4, 5, 7, 9], [4, 6, 7, 8]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[19, [[1, 2, 7, 9], [1, 3, 6, 9], [1, 3, 7, 8], [1, 4, 5, 9], [1, 4, 6, 8], [1, 5, 6, 7], [2, 3, 5, 9], [2, 3, 6, 8], [2, 4, 5, 8], [2, 4, 6, 7], [3, 4, 5, 7]]], 0], [[28, [[1, 3, 7, 8, 9], [1, 4, 6, 8, 9], [1, 5, 6, 7, 9], [2, 3, 6, 8, 9], [2, 4, 5, 8, 9], [2, 4, 6, 7, 9], [2, 5, 6, 7, 8], [3, 4, 5, 7, 9], [3, 4, 6, 7, 8]]], 0], [[18, [[1, 8, 9], [2, 7, 9], [3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]]], 0], [0, 0]], [[0, [8, [[1, 7], [2, 6], [3, 5]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8], [0, 0], [0, [29, [[1, 4, 7, 8, 9], [1, 5, 6, 8, 9], [2, 3, 7, 8, 9], [2, 4, 6, 8, 9], [2, 5, 6, 7, 9], [3, 4, 5, 8, 9], [3, 4, 6, 7, 9], [3, 5, 6, 7, 8]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0]], [[0, 0], [[13, [[1, 3, 9], [1, 4, 8], [1, 5, 7], [2, 3, 8], [2, 4, 7], [2, 5, 6], [3, 4, 6]]], [6, [6]]], [1, 2, 3, 4, 5, 6, 7, 8], [[11, [[2, 9], [3, 8], [4, 7], [5, 6]]], 0], [[16, [[1, 6, 9], [1, 7, 8], [2, 5, 9], [2, 6, 8], [3, 4, 9], [3, 5, 8], [3, 6, 7], [4, 5, 7]]], [27, [[1, 2, 7, 8, 9], [1, 3, 6, 8, 9], [1, 4, 5, 8, 9], [1, 4, 6, 7, 9], [1, 5, 6, 7, 8], [2, 3, 5, 8, 9], [2, 3, 6, 7, 9], [2, 4, 5, 7, 9], [2, 4, 6, 7, 8], [3, 4, 5, 6, 9], [3, 4, 5, 7, 8]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0]], [[0, [4, [4]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, [8, [[1, 7], [2, 6], [3, 5]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[14, [[1, 4, 9], [1, 5, 8], [1, 6, 7], [2, 3, 9], [2, 4, 8], [2, 5, 7], [3, 4, 7], [3, 5, 6]]], [17, [[1, 2, 5, 9], [1, 2, 6, 8], [1, 3, 4, 9], [1, 3, 5, 8], [1, 3, 6, 7], [1, 4, 5, 7], [2, 3, 4, 8], [2, 3, 5, 7], [2, 4, 5, 6]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0]], [[0, [1, [1]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[6, [6]], [32, [[1, 2, 5, 7, 8, 9], [1, 3, 4, 7, 8, 9], [1, 3, 5, 6, 8, 9], [1, 4, 5, 6, 7, 9], [2, 3, 4, 6, 8, 9], [2, 3, 5, 6, 7, 9], [2, 4, 5, 6, 7, 8]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[3, [[1, 2]]], 0], [0, 0]], [[0, [14, []]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [6], [[7, [7]], [18, [[1, 8, 9], [2, 7, 9]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [[8,[8]], [8, [[1, 7], [2, 6]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 6, 7], [0, 0]], [[0, 0], [0, 0], [0, [7, [7]]], [7], [0, [17, [[1, 7, 9], [2, 6, 9], [2, 7, 8]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 6, 7, 8, 9], [0, [1, [1]]], [1, 2], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]

for i in range(len(tablero1)):
    for j in range(len(tablero1)):
        if(tablero1[i][j]==0):
            tablero1[i][j]=matrizPrePoda[i][j]
for cvb in matrizBooleana:
    print(cvb)
for cvb in tablero1:
    print(cvb)

temporalp = copy.deepcopy(tablero1)

resultado = backtracking(temporalp)
if(type(resultado)!=list):
    print(resultado)
else:
    for row in resultado:
        print(row)
'''
kResuelto = [[[0,0],[5,0],[7,0],[0,0],[0,0],[7,0],[3,0],[0,0],[0,0]],
             [[0,7], 3, 4,[0,0],[10,3],2,1,[8,0],[6,0]],
             [[0,3], 2,1,[3,15],1,5,2, 4,3],
             [[0,0], [0,7],2,1, 4,[10,0],[0,4],3,1],
             [[0,0], [6,0],[9,6], 2, 3,1,[4,3],1, 2],
             [[0,4], 3, 1, [0,6],2,3,1, [7,0],[0,0]],
             [[0,3], 1, 2,[3,0],[4,6],2, 3, 1,[8,0]],
             [[0,16], 2,6,1,3,4,[0,11],4,7],
             [[0,0], [0,0],[0,3],2, 1,[0,0],[0,3],2,1]]

matrizBooleana = copy.copy(kResuelto)

for i in range(len(kResuelto)):
    for j in range(len(kResuelto)):
        if((kResuelto[i][j])==list):
            matrizBooleana[i][j] = 0
        else:
            matrizBooleana[i][j] = 1
'''
#print(isSolved(kResuelto))
#backtracking(tablero1)


t1 = [[[0,0],[5,0],[7,0],[0,0],[0,0],[7,0],[3,0],[0,0],[0,0]],[[0,7], 0, 0,[0,0],[10,3],0,0,[8,0],[6,0],[[0,3], 0,0,[3,15],0,0,0, 0,0],[[0,0], [0,7],0,0, 0,[10,0],[0,4],0,0],[[0,0], [6,0],[9,6], 0, 0,0,[4,3],0, 0],[[0,4], 0, 0, [0,6],0,0,0, [7,0],[0,0]],[[0,3], 0, 0,[3,0],[4,6],0, 0, 0,[8,0]],[[0,16], 0,0, 0, 0,0,[0,11],0,0],[[0,0], [0,0],[0,3],0, 0,[0,0],[0,3],0,0]]]

matrizBooleana = copy.deepcopy(t1)

for i in range(len(matrizBooleana)):
    for j in range(len(matrizBooleana)):
        if(matrizBooleana[i][j]==0):
            matrizBooleana[i][j]=1
        else:
            matrizBooleana[i][j]=0

solucion = [[[0,0],[5,0],[7,0],[0,0],[0,0],[7,0],[3,0],[0,0],[0,0]],
[[0,7], 3, 4,[0,0],[10,3],2,1,[8,0],[6,0]],
[[0,3], 2,1,[3,15],1,5,2, 4,3],
[[0,0], [0,7],2,1, 4,[10,0],[0,4],3,1],
[[0,0], [6,0],[9,6], 2, 3,1,[4,3],1, 2],
[[0,4], 3, 1, [0,6],2,3,1, [7,0],[0,0]],
[[0,3], 1, 2,[3,0],[4,6],2, 3, 1,[8,0]],
[[0,16], 2,6,1,3,4,[0,11],4,7],
[[0,0], [0,0],[0,3],2, 1,[0,0],[0,3],2,1]]


