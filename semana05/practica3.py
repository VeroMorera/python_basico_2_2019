
'''
1- crear una clase 'Bebe'
2- declarar cuatro acciones: respirar, comer, llorar, dormir
3- simular un dia normal de un bebe.
'''


class Bebe:

    def __init__(self, nombre):
        self.nombre_bebe = nombre
        self.edad = 1

    def respirar(self):
        print('* Snif-snif *')

    def comer(self):
        print('ñom, ñom, ñom...')

    def llorar(self):
        print('buaaah, buaahhh')

    def dormir(self):
        print('zzzZZZ')

    def crecer(self, edad=1):
        print(edad)



jaime = Bebe('Jaime')


print('El nombre del bebe se llama: ', jaime.nombre_bebe)

print('Mi edad es: ', jaime.edad)

print('Mi edad en un par de anios va a ser es: ' )
jaime.crecer(3)

print('En un día normal, despierto a las 7am, y lloro')
jaime.llorar()

print('Respiro y huelo algo rico... ¡comida!')
jaime.respirar()

print('Me gusta comer la comida que me preparan')
jaime.comer()

print('Ya estoy lleno, así que vuelvo a dormir...')
jaime.dormir()

