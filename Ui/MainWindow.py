
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
import tkFileDialog
import tkMessageBox

matrizKakuroFinal =""



#Manejo de archivos para abrir y guardar kakuros------------------------------------------------------------
def saveFile(matrizKakuro):
    f = tkFileDialog.asksaveasfile(mode= 'w', defaultextension= '.txt')
    if f is None:
        return
    txtSave = str(matrizKakuro)
    f.write(txtSave)
    f.close()
    tkMessageBox.showinfo("Manejo de Arhivos", "Kakuro Guardado")
    


def openFile():
    
    filename = tkFileDialog.askopenfile(filetypes=[("Text files","*.txt")])
    txt = filename.read()   
    print txt
    filename.close()
#------------------------------------------------------------------------------------------------------------

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
                
                
#Genera las tuplas correspondientes a la sumas de las filas y columnas---------------------------------------------------------------------------

def generarTuplas(matrizFinal):
    
    print(len(matrizFinal))
    for i in range(len(matrizFinal[0])):
        for j in range(len(matrizFinal[0])):
            if matrizFinal[i][j]==0 :
                matrizFinal[i][j]= [0,0]
            if matrizFinal[i][j]=='0':
                matrizFinal[i][j]= [0,0]
    print(len(matrizFinal))
                
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
def interseccion(listaRandomCol,listaRandomFila,matrizFinal):
    print ("lista RandomCol: "+ str(listaRandomCol))
    print ("lista RandomFila: "+ str(listaRandomFila))
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
                listaRandom = interseccion(listaRandomCol,listaRandomFila, matrizFinal)
                if len(listaRandom)==1:
                    numeroCasilla = 0
                else:
                    numeroCasilla = random.randint(0,(len(listaRandom))-1)
                matrizFinal[i][j]= listaRandom[numeroCasilla]

    matrizTuplas = generarTuplas(matrizFinal)
    return matrizTuplas
#-----------------------------------------------------------------------------------------------------------------------------------------------

#Funciones que verifican con cuales valores la suma es correcta-----------------------------------------------------------------
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
#---------------------------------------------------------------------------------------------------------------------------------    
    
    
#Revisa si existen casillas blancas entre dos negras y la elimina-----------------------------------------

def revisarAdyacencias(matrizAdyacencias):
    
    for i in range(1,len(matrizAdyacencias[0])-1):
        for j in range(1,len(matrizAdyacencias[0])-1):
            if matrizAdyacencias[i][j]=='1' and matrizAdyacencias[i][j-1]=='0' and matrizAdyacencias[i][j+1]=='0' and matrizAdyacencias[i-1][j]=='0' and matrizAdyacencias[i+1][j]=='0':
                print ("Cambio de casilla por adyacencia en: "+ "Fila: "+ str(i)+ "Columna: "+str(j) )
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
                    print ("Cambio casilla blanca por negra en  "+ "Fila: "+ str(i)+ "Columna:"+ str(j))
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
                    print ("Cambio casilla blanca por negra en  "+ "columna: "+ str(j)+ "fila:"+ str(i))
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
    global matrizKakuroFinal
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
     
    #Llama a funcion para validar espacios        
    
    matrizFinal=   validar9Casillas(matrizInicial)  
    matrizKakuroFinal = matrizFinal[:]
      
      
    
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
x1=10
y1=10
window = tk.Tk()
value = StringVar()
window.title("Solucionador de Kakuros")
window.geometry("1024x600")
kSize =  Spinbox(window,values = ("10x10","11x11","12x12","13x13","14x14","15x15","16x16","17x17","18x18","19x19","20x20"), textvariable= value).place(x=420, y= 500)
buttonCreate = Button(window, text= "Generar Kakuro", command = obtener).place(x=375, y=530)  
buttonSolve = Button(window, text = "Resolver Kakuro").place(x=475, y=530)
buttonGuardar = Button(window, text = "Guardar Kakuro Generado", command = lambda: saveFile(matrizKakuroFinal)).place(x=220, y=530)
buttonAbrir  = Button(window, text = "Abrir Kakuro Generado", command= lambda: openFile()).place(x=580, y=530)






mainloop()









