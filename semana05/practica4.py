# creacion de instancias

class Animal:
    def __init__(self, e, a):

        self.especie = e
        self.edad = a

    def correr(self):
        print('Soy un {}. '
              'Estoy corriendo.'.format(self.especie))

    def crecer(self, edad = 0):
        if (self.edad + edad) > 14:
            self.vivo = False  #atributos pueden o no ser parametros.

        else:
            self.edad += edad
            self.vivo = True


un_animal = Animal(e='caballo', a=3)


un_animal.crecer(12)  #aumentarle la edad

print('hola soy un {} , tengo {} anios'.format(un_animal.especie, un_animal.edad))


if un_animal.vivo:
    print('hola soy un {} , tengo {} anios'.format(un_animal.especie, un_animal.edad) )

else:
    print('...Me mori... RIP')

