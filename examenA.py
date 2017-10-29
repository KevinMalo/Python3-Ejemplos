agenda = [
    {
        'nombre':'Kevin Bueno',
        'telefono':'3144879954',
        'correo':'kean.solano@gmail.com'
    },
     {
        'nombre':'Orfa Archila',
        'telefono':'3204888554',
        'correo':'orfa.archila@gmail.com'
    }, 
    {
        'nombre':'Natalia Palomino',
        'telefono':'3005549954',
        'correo':'napal@gmail.comm'
    }
]

#agenda[0]['nombre'] = 'Prueba'

def crear_contacto( name, phone, email ):
    agenda.append(
        {
        'nombre':name,
        'telefono':phone,
        'correo':email
        }
    )

def editar_contacto(location, name, phone, email):
    agenda.pop(location)
    agenda.insert(location, 
        {
        'nombre':name,
        'telefono':phone,
        'correo':email
        }
    )

#editar_contacto( 0, 'juan', 'pedro', 'r' )

"""def editar_contacto(location, name, phone, email):
    agenda[location]['nombre'] = name,
    agenda[location]['nombre'] = phone,
    agenda[location]['nombre'] = email
    

editar_contacto(0, 'pepe', 'pepa', 'ess')"""

print(agenda)