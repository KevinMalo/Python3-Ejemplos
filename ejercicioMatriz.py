import random
from random import randrange
from time import sleep

matriz = []
longitudx = 10
longitudy = 10

#Creamos la funcion que recibe 2 parametros X y Y
def crear_matriz( x = 0, y = 0 ):

    for i in range(x):
        matriz.append([])
        for j in range(y):
            azar = random.randrange(0,100)
            matriz[i].append(azar)
                    

crear_matriz(longitudx, longitudy)

def imprimir_matriz():
    longitud = len(matriz)
    for i in range(longitud):
        print(matriz[i])

def llenar_derecha():
    y = longitudy - 1
    x = -1

    for i in range(y, 0, -1):

        x = x + 1

        matriz[x][i] = randrange(2000)
        imprimir_matriz()

def llenar_izquierda():
    for i in range(longitudx):
        matriz[i][i] = randrange(100)
        imprimir_matriz()
        print('')   
        

llenar_derecha()
llenar_izquierda()
    