
def funcionUno(matrizKakuro):
    for i in range(len(matrizKakuro[0])):
        for j in range(len(matrizKakuro[0])):
            if type(matrizKakuro[i][j])!= list: #Revisa si una casilla es diferente de negra
                if revisarFilaIzq(matrizKakuro, i, j, matrizKakuro[i][j])==True and revisarFilaDer(matrizKakuro, i, j, matrizKakuro[i][j])==True:
                    print("Numero no esta Repetido")
                else:
                    print("La otra condicion")
                
    
    
    
def revisarFilaIzq(matrizKakuro,i,j, numeroCasilla):
    while type(matrizKakuro[i][j])!= list: #List es una casilla negra
        j-=1
        if numeroCasilla== matrizKakuro[i][j]:
            return False
    return  True

def revisarFilaDer(matrizKakuro,i,j, numeroCasilla):
    while type(matrizKakuro[i][j])!= list: #List es una casilla negra
        j+=1
        if numeroCasilla== matrizKakuro[i][j]:
            return False
    return  True
            