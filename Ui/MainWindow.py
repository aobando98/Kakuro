
#--------------------------------------------------
import random
import Tkinter as tk
from Tkinter import StringVar, Tk, Spinbox, Button
from _tkinter import mainloop
from cgitb import text
from __builtin__ import str
from pipes import stepkinds
from _ast import Str
from getpass import fallback_getpass




#------------------------------------------------------------------------
def redraw(matrix):
    global gameframe
    board = [ [None]*len(matrix[0]) for _ in range(len(matrix[0])) ]
    gameframe = tk.Frame(window)
    gameframe.pack()

    for i,row in enumerate(matrix):
        for j,column in enumerate(row):
            if matrix[i][j]==0:   
                L = tk.Label(gameframe,text='    ',bg= "gray")
                L.grid(row=i,column=j,padx='1',pady='1')
            else:
                L = tk.Label(gameframe,text='    ',bg= "black")
                L.grid(row=i,column=j,padx='1',pady='1')
#---------------------------------------------------------------------------------------------------------
'''
def generarTuplas(matrizFinal):
    sumaFila = 0
    sumaColumna = 0
    
    for i in range(1,len(matrizFinal[0])):
        for j in range(1,len(matrizFinal[0])):
            if matrizFinal[i][j]==0:
                matrizFinal[i][j]= (0,0)
                
    return matrizFinal
                
'''

#---------------------------------------------------------------------------------------------------------
def revisarCasillasBlanca1(matrizFinal):

    for i in range(1,len(matrizFinal[0])):
        for j in range(1, len(matrizFinal[0])):
            flag = True
            while matrizFinal[i][j]!=0 and flag==True:
                numeroCasilla  = random.randint(1,9)
                if verificarSumaFila(matrizFinal, i, j, numeroCasilla)==True and verificarSumaColumna(matrizFinal, i, j, numeroCasilla)==True: 
                    matrizFinal[i][j]=numeroCasilla
                    flag =False
                else:
                    pass
    return matrizFinal
#---------------------------------------------------------------------------------------------------------

#Funciones que verifican cuales valores se posicionan en la tupla-----------------------------------------------------------------
def verificarSumaFila1(matrizFinal,i,j,numeroCasilla):
        while matrizFinal[i][j]!=0:
            j-=1
        j+=1
        while matrizFinal[i][j]!=0 :
            print ("Error puede estar en la celda: "+"Fila: "+ str(i)+" Columna: "+ str(j))
            if matrizFinal[i][j]== numeroCasilla:
                return False
            else:
                j+=1
        return True

        
def verificarSumaColumna1(matrizFinal,i,j,numeroCasilla):
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


#---------------------------------------------------------------------------------------------------------
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
    #matrizBack= eliminarRepeticiones(matrizFinal)
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
#---------------------------------------------------------------------------------------------------------------------------------    
    
    
#Revisa si existen casillas blancas entre dos negras y la elimina-----------------------------------------

def revisarAdyacencias(matrizAdyacencias):
    
    for i in range(1,len(matrizAdyacencias[0])-1):
        for j in range(1,len(matrizAdyacencias[0])-1):
            if matrizAdyacencias[i][j]==1 and matrizAdyacencias[i][j-1]==0 and matrizAdyacencias[i][j+1]==0 and matrizAdyacencias[i-1][j]==0 and matrizAdyacencias[i+1][j]==0:
                print ("Cambio de casilla por adyacencia en: "+ "Fila: "+ str(i)+ "Columna: "+str(j) )
                matrizAdyacencias[i][j]=0
              
    matrizTupla = revisarCasillasBlanca(matrizAdyacencias, len(matrizAdyacencias[0]))
    return matrizTupla

#--------------------------------------------------------------------------------------------------------

#Valida si una fila o una columna tiene mas de 9 casillas------------------------------------------
def validar9Casillas(matrizKakuro):

    for i in range(1,len(matrizKakuro[0])):
        numeroBlancasFila =0
        for j in range(1,len(matrizKakuro[0])):
            if matrizKakuro[i][j]== 1 :
                numeroBlancasFila+=1
                if numeroBlancasFila>9:
                    print ("Cambio casilla blanca por negra en  "+ "Fila: "+ str(i)+ "Columna:"+ str(j))
                    matrizKakuro[i][j]=0
                    numeroBlancasFila = 0
                else:
                    pass
            else:
                numeroBlancasFila=0     


    for i in range(1,len(matrizKakuro[0])):
        numeroBlancasColumna= 0
        for j in range(1,len(matrizKakuro[0])):
            if matrizKakuro[j][i]==1:
                numeroBlancasColumna+=1
                if numeroBlancasColumna>9:
                    print ("Cambio casilla blanca por negra en  "+ "columna: "+ str(j)+ "fila:"+ str(i))
                    matrizKakuro[j][i]=0
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
    
#Funcion que una matriz del tamano dado----------------------------------------------------------------
def crearMatriz(filas, columnas):
    matrizInicial = []
    a = ""
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
            
    for i in range(1,len(matrizInicial[0])):
        for j in range(1,len(matrizInicial[0])):
            if matrizInicial[i][j]=='1':
                matrizInicial[i][j]=1
            else:
                matrizInicial[i][j]=0             
    
    #Llama a funcion para validar espacios        
    matrizFinal =  validar9Casillas(matrizInicial)
    
    
    #Imprime matriz en consola        
    for k in range(filas):
        for j in range(columnas):
            a+=str(matrizFinal[k][j])+'\t'
        print (a)
        a=""
    
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

#Ventana principal del programa--------------------------------------------------------

window = tk.Tk()
value = StringVar()
window.title("Solucionador de Kakuros")
window.geometry("1024x600")
kSize =  Spinbox(window,values = ("10x10","11x11","12x12","13x13","14x14","15x15","16x16","17x17","18x18","19x19","20x20"), textvariable= value).place(x=420, y= 500)
buttonCreate = Button(window, text= "Generar Kakuro", command = obtener).place(x=375, y=530)  
buttonSolve = Button(window, text = "Resolver Kakuro").place(x=475, y=530)

mainloop()









