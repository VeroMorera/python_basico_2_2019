'''
lista de compras

verduras: tomate, papas, cebollas, ajos

frutas: piña, sandia, naranja

carnes: jamon, pollo, costilla de cerdo

limpieza: jabon, cloro, shampoo


1-crear una lista individual de cada categoria.
2-crear lista de compras



'''
''' 
#lista general
lista_compras = []
lista_comprasTest = []


#listas internas
verduras = ['tomate', 'papas', 'cebollas', 'ajos']
frutas = ['piña', 'sandía', 'naranja']
carnes = ['jamón', 'pollo', 'costilla de cerdo']
limpieza = ['jabón', 'cloro', 'shampoo']


#agregar listas internas a lista general

#OPCION 1
lista_comprasTest.extend( [verduras, frutas, carnes, limpieza] )
#extend solo se puede usar metiendo una lista completa de listas

print(lista_comprasTest)


#OPCION 2
#append de cada elemento
lista_compras.append(verduras)
lista_compras.append(frutas)
lista_compras.append(carnes)
lista_compras.append(limpieza)

print(lista_compras)


#OPCION 3

#listas internas
verduras = ['tomate', 'papas', 'cebollas', 'ajos']
frutas = ['piña', 'sandía', 'naranja']
carnes = ['jamón', 'pollo', 'costilla de cerdo']
limpieza = ['jabón', 'cloro', 'shampoo']

#lista general
lista_compras2 = [verduras, frutas, carnes, limpieza]

print (lista_compras2)

#----------------------------------------------------------------#

# 3- Cuantos elementos hay en la lista (total)?


#OPCION 1

cantidad = 0 #acumulador

for categoria in lista_compras:

    cantidad += len(categoria)


print ('la cantidad total de artículos es ', cantidad)

#OPCION 2

#esta es una version con mayor rendimiento

mi_lista = []

for categoria in lista_compras:
    mi_lista.extend(categoria)
    print(mi_lista)

print('la cantidad total de artículos es ', len(mi_lista))

#----------------------------------------------------------------#
'''
# 4- agregar verdura:chile. fruta: mango
''' 

#OPCION 1
#lista_compras[0].append('chile') #agregar a esa lista
#lista_compras[1].append('mango')

#print(lista_compras)



#OPCION 2
#listas internas
verduras = ['tomate', 'papas', 'cebollas', 'ajos']
frutas = ['piña', 'sandía', 'naranja']
carnes = ['jamón', 'pollo', 'costilla de cerdo']
limpieza = ['jabón', 'cloro', 'shampoo']

lista_compras = [verduras, frutas, carnes, limpieza]

verduras.append('chile')
frutas.append('mango')

print(lista_compras)

#=---------------------------------------------------------#
'''

# 5- Eliminar verduras de la lista.

#listas internas
verduras = ['tomate', 'papas', 'cebollas', 'ajos']
frutas = ['piña', 'sandía', 'naranja']
carnes = ['jamón', 'pollo', 'costilla de cerdo']
limpieza = ['jabón', 'cloro', 'shampoo']

lista_compras = [verduras, frutas, carnes, limpieza]

#opcion 1
verduras.clear()

#opcion 2
del verduras[:]

#del verduras #no funciona
#verduras=[]  #no funciona



print(lista_compras)


