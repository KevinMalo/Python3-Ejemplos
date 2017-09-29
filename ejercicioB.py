canciones = [
    {
        'nombre':'Mucho gusto',
        'anho':'2010',
        'genero':'RAP'
    },
    {
        'nombre':'Cest la Mort',
        'anho':'2012',
        'genero':'RAP'
    },
    {
        'nombre':'In The End',
        'anho':'2000',
        'genero':'ROCK'
    },
    {
        'nombre':'Highway to Hell',
        'anho':'1979',
        'genero':'ROCK'
    },
    {
        'nombre':'Pedro Navaja',
        'anho':'1978',
        'genero':'SALSA'
    },
    {
        'nombre':'Rebelion',
        'anho':'1986',
        'genero':'SALSA'
    },
]

def crear_cancion(name, year, genre):
    canciones.append(
        {
            'nombre':name,
            'anho':year,
            'genero':genre
        }
    )

crear_cancion('Ula Ula','2018','Pop')
crear_cancion('Pedrito','2019','rap')

def buscador(genre):
    
    for i in canciones:
        
        if i['genero'] == genre:
            print(i['nombre'])


crear_cancion('Ejemplo','2015','SALSA')

buscador('SALSA')