zoologico = []

def enjaular_animales(animal):
    zoologico.append(
        {
            'animal':animal,
            'alimentacion':{
                'manhana':0,
                'tarde':0,
                'noche':0
            }
        }
    )

enjaular_animales('dinosaurio')
enjaular_animales('pollo')
enjaular_animales('chiguire')
enjaular_animales('vaca')


def alimentar_animal(animal_type, morning = 0, afternoon = 0, night = 0):
    
    for buscar_animal in zoologico:
        
        if buscar_animal['animal'] == animal_type:
            
            if morning == 'manhana':
                buscar_animal['alimentacion']['manhana'] += 1
            
            if afternoon == 'tarde':
                buscar_animal['alimentacion']['tarde'] += 1

            if night == 'noche':
                buscar_animal['alimentacion']['noche'] += 1


alimentar_animal('pollo','manhana','tarde')
alimentar_animal('pollo','manhana','tarde','noche')

print(zoologico)