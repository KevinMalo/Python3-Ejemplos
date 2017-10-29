import math

grilla = [];

def crear_grilla(filas = 1, col = 1):    
    filas = filas + 1

    for i in range(filas):
        grilla.append(['-'])
    
        for k in range(col):
            grilla[i].append('-')

    def crear_rombo(elemento, posicion):

        grilla[elemento].pop(posicion)
        grilla[elemento].insert(posicion,'*')
    
    crear_rombo(0,3)
    crear_rombo(1,2)
    crear_rombo(1,4)
    crear_rombo(2,1)
    crear_rombo(2,5)
    crear_rombo(3,0)
    crear_rombo(3,6)
    crear_rombo(4,1)
    crear_rombo(4,5)
    crear_rombo(5,2)
    crear_rombo(5,4)
    crear_rombo(6,3)

crear_grilla(6, 6);

print(grilla)
