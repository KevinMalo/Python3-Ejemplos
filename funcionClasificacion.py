clasificacion = {
    'ninhos': 0,
    'adolescentes': 0,
    'jovenes': 0,
    'adultos': 0,
    'adulto mayor': 0
}

def clasificar( edad ):
    global clasificacion
    if edad <= 12:
        clasificacion['ninhos'] += 1
    elif edad > 12 and edad < 19 :
        clasificacion['adolescentes'] += 1
    elif edad > 19 and edad < 26 :
        clasificacion['jovenes'] += 1
    elif edad > 25 and edad < 61 :
        clasificacion['adultos'] += 1
    elif edad > 60 :
        clasificacion['adulto mayor'] += 1   

clasificar(10)
clasificar(50)
clasificar(25)
clasificar(45)
clasificar(21)
clasificar(87)
clasificar(15)
clasificar(35)
clasificar(4)

print(clasificacion)