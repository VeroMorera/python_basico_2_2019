'''
#EJEMPLO 1
class First:
    def __init__(self):   #init es un metodo especial, para poder controlar inicializacion de los objetos.
                        # Este metodo se llama automaticamente cuando se construye el objeto. (linea 7)
                        #si esto no se escribe, el programador no tiene el control sobre el codigo
        print('Constructor ejecutado')


a = First()  #se construye, se inicializa el objeto.
print(type(a))




#EJEMPLO 2
class Pato:
    def quack(self):  #el self siempre es requerido, porque son metodos de la instancia, internos,
                    # esto especifica que pertenecen al class Pato.
        print('Quaaack!')

    def walk(self):
        print('Caminar como pato.')


# nace un pato llamado Donald.
donald = Pato()


#darle caracteristicas de pato
donald.quack()
donald.walk()

'''


#EJEMPLO 3
class Pato:

    def __init__(self, nombre):
        self.pato_nombre = nombre

    def quack(self):  #el self siempre es requerido, porque son metodos de la instancia, internos,
                    # esto especifica que pertenecen al class Pato.
        print('Quaaack!')

    def walk(self):
        print('Caminar como pato.')


# nace un pato llamado Donald.
donald = Pato('Donald')


#darle caracteristicas de pato
donald.quack()
donald.walk()

print('¿Cuál es tu nombre? ', donald.pato_nombre)