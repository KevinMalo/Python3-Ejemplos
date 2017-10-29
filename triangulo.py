triangulo = []

def triangulo_funcion(nivel = 0):
    
    for i in range(nivel):

        triangulo.append([])

        for k in range(i):
            
            triangulo[i].append(k)          

        if 0 < len(triangulo):
            triangulo[i].append(i)
        
triangulo_funcion(8)

print(triangulo)