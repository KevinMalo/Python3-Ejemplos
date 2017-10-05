zoologico = []

def enjaular_animal(animal_type):
    zoologico.append(
        {
            'animal':animal_type,
            'alimentacion':{
                'manhana':0,
                'tarde':0,
                'noche':0
            }
        }
    )

enjaular_animal('jirafa')
enjaular_animal('caballo')
enjaular_animal('dinosaurio')
enjaular_animal('chiguire')

def alimentar_animal(animal_type, morning = 0, afternoon = 0, night = 0):
    
    for buscar in zoologico:
        if buscar['animal'] == animal_type:
            if morning == 'morning':           
                buscar['alimentacion']['manhana'] += 1
            if afternoon == 'afternoon':
                buscar['alimentacion']['tarde'] += 1
            if night == 'night':
                buscar['alimentacion']['noche'] += 1

alimentar_animal('dinosaurio', 'morning', 'afternoon', 'night' )
alimentar_animal('dinosaurio', 'morning', 'afternoon', 'night' )

print(zoologico)