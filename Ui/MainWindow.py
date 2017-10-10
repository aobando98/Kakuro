
#--------------------------------------------------
import random
import Tkinter as tk
from Tkinter import StringVar, Tk, Spinbox, Button
from _tkinter import mainloop
from cgitb import text




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
#------------------------------------------------------------------------


#Valida si una fila o una columna tiene mas de 9 casillas------------------------------------------
def validar9Casillas(matrix):
    numeroBlancasFila =0
    numeroBlancasColumna= 0
    for i in range(1,len(matrix[0])):
        for j in range(1,len(matrix[0])):
            if matrix[i][j]==1:
                numeroBlancasFila+=1
                if numeroBlancasFila==9:
                    matrix[i][j]=0
                else:
                    pass
            else:
                pass                      
                    
    for i in range(1,len(matrix[0])):
        for j in range(1,len(matrix[0])):
            if matrix[j][i]==1:
                numeroBlancasColumna+=1
                if numeroBlancasColumna==9:
                    matrix[j][i]=0
                else:
                    pass
            else:
                pass
            
    return matrix  
#------------------------------------------------------------------------                

#Genera casillas aleatorias con una pequena probabilidad---------------------------------------------
def generateRndm():
    casillas1 = [(0,0),1]
    casillas =['0','1']
    pesos = [0.2,0.8]
    resultado= []
    
    for e, p in zip(casillas, pesos):
        resultado += [e] * int(p * 100)
        
    return random.choice(resultado)
        
        
        
        
        
#Funcion que una matriz del tamano dado----------------------------------------------------------------
def crearMatriz(filas, columnas):
    matrizKakuro = []
    a = ""
    #Crea la matriz del tamano indicado
    for k in range(filas):
        matrizKakuro.append([1]*columnas)
    #Inicializa toda la primera columna y fila con campos en negro    
    for i in range(filas):
        matrizKakuro[0][i]=0
        matrizKakuro[i][0]=0
        
    #Genera espacios aleatorios en el kakuro    
    for k in range(1,filas):
        for j in range(1,columnas):
            matrizKakuro[k][j]= generateRndm()
    #Llama a funcion para validar espacios        
    matrizFinal =  validar9Casillas(matrizKakuro)
    
    
    #Imprime matriz en consola        
    for k in range(filas):
        for j in range(columnas):
            a+=str(matrizFinal[k][j])+'\t'
        print (a)
        a=""
        
    #redraw(matrizKakuro)
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









