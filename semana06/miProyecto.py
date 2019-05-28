#esto es un proyecto que usa otros modulos.



from semana06.archivo1 import suma_resta
from semana06.archivo2 import mi_lista, mi_diccionario


#opcion 1
resultado = suma_resta(a=10, b=3, c=2)

#opcion 2
resultado = suma_resta(10, 3, 2)


print(resultado)

print(mi_lista, mi_diccionario)


print('esto es un ejemplo')

from semana06.subfolder.archivo3 import Pato

pass

donald = Pato ()
donald.camina()
