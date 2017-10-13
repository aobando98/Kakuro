
def revisarCasillasBlanca(matrizFinal, numeroFilas):
    
    listaRevision = [0]*(numeroFilas+1)
    for i in range(numeroFilas):
        matrizFinal[i].append(0)
    matrizFinal.append(listaRevision)

    
    for i in range(1,len(matrizFinal[0])):
        for j in range(1, len(matrizFinal[0])):
            flag = True
            while matrizFinal[i][j]==1 and flag==True:
                numeroCasilla  = random.randint(1,9)
                if verificarSumaFila(matrizFinal, i, j, numeroCasilla)==True and verificarSumaColumna(matrizFinal, i, j, numeroCasilla)==True: 
                    matrizFinal[i][j]=numeroCasilla
                    flag =False
                else:
                    pass
    matrizBack= eliminarRepeticiones(matrizFinal)
    return matrizFinal
#---------------------------------------------------------------------------------------------------------

#Funciones que verifican cuales valores se posicionan en la tupla-----------------------------------------------------------------
def verificarSumaFila(matrizFinal,i,j,numeroCasilla):
        while matrizFinal[i][j]!=0:
            j-=1
        j+=1
        while matrizFinal[i][j]!=0 :
            print ("Error puede estar en la celda: "+"Fila: "+ str(i)+" Columna: "+ str(j))
            if numeroCasilla ==1:
                return True
            else:
                if matrizFinal[i][j]== numeroCasilla:
                    return False
                else:
                    j+=1
        return True

        
def verificarSumaColumna(matrizFinal,i,j,numeroCasilla):
    while matrizFinal[i][j]!=0:
        i-=1
    i+=1
    while matrizFinal[i][j]!=0:
        if numeroCasilla==1:
            return True
        else:
            if matrizFinal[i][j]== numeroCasilla:
                return False
            else:
                i+=1
            
            
    return True