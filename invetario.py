inventario = []

def llenar_invetario(id_par, marca_par):
    inventario.append(
        {
            'id':id_par,
            'marca':marca_par,
            'Fecha':[

            ]
        }
    )

llenar_invetario( 5, 'Dell' )
llenar_invetario( 0, 'Asus' )
llenar_invetario( 3, 'Apple' )
llenar_invetario( 7, 'Google' )
llenar_invetario( 10, 'Pepito' )

print(
    inventario[0]['Fecha']
)

def fecha_invetario(marca_par, date):
    
    for buscar_marca in inventario:
        
        if buscar_marca['marca'] == marca_par:
            buscar_marca['Fecha'].append(
                    date
            )

fecha_invetario( 'Pepito', '01/10/17')
fecha_invetario( 'Pepito', '02/10/17')

print(inventario)