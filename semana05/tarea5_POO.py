'''
Basado en el ejemplo anterior, crear un Nieto Humano, basado en las habilidades
aprendidas por el abuelo humano y transmitidas al padre Humano.

Abuelo -> padre -> Nieto

El abuelo trabaja. El padre es contador y el nieto es analista de negocios

El nieto tiene que ir a trabajar, sabe de contabilidad es un analista de negocios
'''



# Misc classes
class misc:
    def __repr__(self):
        # return the clase name
        return self.__class__.__name__

    def __str__(self):
        # return the clase name
        return self.__class__.__name__



class Abuelo(misc):
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar(self):
        print(f'El {self} {self.nombre} tiene un trabajo')


#####
abuelo = Abuelo('Juan')
abuelo.trabajar()
#####

class Papa(Abuelo):

    def __init__(self, nombre, profesion):
        super().__init__(nombre=nombre)
        self.profesion = profesion

        
    def ocupacion(self):
        self.trabajar()
        print(f'{self.nombre} es {self.profesion}')

####
papa = Papa('Daniel', 'contador')
papa.ocupacion()
####

class Nieto(Papa):
    def __init__(self, nombre, profesion):
        super().__init__(nombre=nombre, profesion=profesion)

    def nieto_trabajo(self):
        self.ocupacion()
        print(f'{self.nombre} sabe de contabilidad')



####
nieto = Nieto('Rolando', 'analista de negocios')
nieto.nieto_trabajo()