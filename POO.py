class Animal:
    patas = 0
    tipo = ''
    nombre = ''
    def comer(self, alimento):
        print('El ' + self.nombre +  ' come ' + alimento)
        self.dormir('en la cama')
    def dormir(self, lugar):
        print('Se va a dormir en ' + lugar)

gato = Animal()
gato.nombre = 'Macu'
gato.comer('purina')
