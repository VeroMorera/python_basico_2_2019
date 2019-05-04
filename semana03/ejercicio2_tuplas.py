'''
1- crear una tupla de mango, uvas, manzana, pera
'''

#mis_frutas = ('mango', 'uvas', 'manzana', 'pera')


#print(mis_frutas)

#-----------------------------------------------------------------


#2- agregar piña a la tupla de frutas

mis_frutas = ('mango', 'uvas', 'manzana', 'pera') + ('piña', )

#print(mis_frutas)

#-----------------------------------------------------------------

#3- indice (numero primos)

lista_pares = mis_frutas[1::2]

print('lista de pares ', lista_pares)

lista_impares = mis_frutas[0::2]

print('lista de impares ', lista_impares)