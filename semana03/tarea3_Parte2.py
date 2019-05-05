#    --------------------   SEGUNDA PARTE   --------------------   #

'''
1- Escriba un programa que permita crear una lista de palabras.
Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista.
Por último, el programa tiene que escribir la lista.
'''

#instrucciones
print('Instrucciones: este programa crea una lista de palabras de la longitud que usted requiera')

print()
lista_de_palabras = []
cantidad_palabras = int(input('Por favor digite el número de palabras en su lista  '))

for i in range(cantidad_palabras):
    palabra = str(input('Por favor digite la palabra ' + str(i+1)))
    lista_de_palabras.append(palabra)

print('La lista creada es: ', lista_de_palabras)

cantidad_palabras_en_lista = int(input('Dígame cuántas palabras tiene la lista: '))

#condicional para coroborar respuesta de usuario
if cantidad_palabras_en_lista != len(lista_de_palabras):
    print('¡Imposible!')
else:
    print('¡Correcto!')


#=============================================================================================================#



#2-Escriba un programa que permita crear una lista de palabras y que,
# a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

#instrucciones
print('Instrucciones: este programa crea una lista de palabras de la longitud que usted requiera y busca repetidos')

print()
lista_de_palabras2 = []
cantidad_palabras2 = int(input('Por favor digite el número de palabras en su lista  '))

for i in range(cantidad_palabras2):
    palabra2 = str(input('Por favor digite la palabra ' + str(i+1)))
    lista_de_palabras2.append(palabra2)

print('La lista creada es: ', lista_de_palabras2)

buscar_palabra = str(input('Dígame la palabra a buscar '))

#contar la palabra en la lista
def countX(list, x):
    return list.count(x)


total_veces = countX(lista_de_palabras2, buscar_palabra)

if total_veces > 0:

    print('La palabra "' + buscar_palabra + '" aparece ' +str(total_veces)+ ' veces en la lista')

else:
    print('La palabra "' + buscar_palabra + '" no aparece en la lista.')


#=============================================================================================================#


#3-Escriba un programa que permita crear una lista de palabras y que, a continuación,
 #pida dos palabras y sustituya la primera por la segunda en la lista.

#instrucciones
print('Instrucciones: este programa crea una lista de palabras de la longitud que usted requiera y busca repetidos')

print()
lista_de_palabras3 = []
cantidad_palabras3 = int(input('Por favor digite el número de palabras en su lista  '))

for i in range(cantidad_palabras3):
    palabra3 = str(input('Por favor digite la palabra ' + str(i+1)))
    lista_de_palabras3.append(palabra3)

print('La lista creada es: ', lista_de_palabras3)

palabra_a_sustituir = str(input('Sustituir la palabra:'))

palabra_nueva = str(input('Por la palabra:'))


#verificar si la palabra a sustituir esta dentro de la lista
if palabra_a_sustituir not in lista_de_palabras3:
    print('La palabra no está en la lista')

else:

    for i in range(len(lista_de_palabras3)):

        if palabra_a_sustituir == lista_de_palabras3[i]: # si la palabra existe en la lista y es igual a la de busqueda
            lista_de_palabras3[i] = palabra_nueva # reemplazar x palabra nueva


    print('La lista es ahora: ', lista_de_palabras3)


#=============================================================================================================#


#4- Escriba un programa que permita crear una lista de palabras y que, a continuación,
#pida una palabra y elimine esa palabra de la lista.

#instrucciones
print('Instrucciones: este programa crea una lista de palabras de la longitud que usted requiera y elimina una palabra')

print()
lista_de_palabras4 = []
cantidad_palabras4 = int(input('Por favor digite el número de palabras en su lista  '))

for i in range(cantidad_palabras4):
    palabra4 = str(input('Por favor digite la palabra ' + str(i+1)))
    lista_de_palabras4.append(palabra4)


print('La lista creada es: ', lista_de_palabras4)

palabra_a_eliminar = str(input('Eliminar la palabra:'))


if palabra_a_eliminar in lista_de_palabras4:  # si la palabra existe en la lista
    lista_de_palabras4.remove(palabra_a_eliminar)  # quitarla de la lista

else:
    print('La palabra no existe')

print('La lista es ahora: ', lista_de_palabras4)


#=============================================================================================================#


# 5-Escriba un programa que permita crear dos listas de palabras y que,
#  a continuación, elimine de la primera lista los nombres de la segunda lista.

print('Instrucciones: este programa crea dos listas de palabras, y elimina de la primera, las coincidencias de la segunda.')

print()
lista_de_palabrasA = []
lista_de_palabrasB = []
cantidad_palabrasA = int(input('Por favor digite el número de palabras en su lista A  '))
cantidad_palabrasB = int(input('Por favor digite el número de palabras en su lista B  '))

for i in range(cantidad_palabrasA):
    palabraA = str(input('Por favor digite la palabra ' + str(i+1) + ' de la lista A:  '))
    lista_de_palabrasA.append(palabraA)

print('La lista A es: ', lista_de_palabrasA)

for i in range(cantidad_palabrasB):
    palabraB = str(input('Por favor digite la palabra ' + str(i+1)+ ' de la lista B:  '))
    lista_de_palabrasB.append(palabraB)

print('La lista B es: ', lista_de_palabrasB)

for i in range(len(lista_de_palabrasB)):
    if lista_de_palabrasB[i] in lista_de_palabrasA:
        lista_de_palabrasA.remove(lista_de_palabrasB[i])
        

print('La nueva listaA, sin los repetidos de la lista B es: ', lista_de_palabrasA)


#=============================================================================================================#



# 6-Escriba un programa que permita crear una lista de palabras y que,
# a continuación, cree una segunda lista igual a la primera, pero al revés

print('Instrucciones: este programa crea una lista y un duplicado de la misma pero invertido.')

print()
lista_de_palabrasOriginal = []
lista_de_palabrasInvertida = []
cantidad_palabras_original = int(input('Por favor digite el número de palabras en su lista  '))


for i in range(cantidad_palabras_original):
    palabra_orig = str(input('Por favor digite la palabra ' + str(i+1) + ' de la lista:  '))
    lista_de_palabrasOriginal.append(palabra_orig)
    lista_de_palabrasInvertida.append(palabra_orig)


lista_de_palabrasInvertida.reverse()


print('La lista original es ', lista_de_palabrasOriginal)
print('La lista invertida es ', lista_de_palabrasInvertida)


#=============================================================================================================#

# 7-Escriba un programa que permita crear una lista de palabras y que, a continuación,
# elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).

#instrucciones
print('Instrucciones: este programa crea una lista de palabras y elimina los repetidos')

print()
lista_de_palabras7 = []
cantidad_palabras7 = int(input('Por favor digite el número de palabras en su lista  '))

for i in range(cantidad_palabras7):
    palabra7 = str(input('Por favor digite la palabra ' + str(i+1)))
    lista_de_palabras7.append(palabra7)

print('La lista creada es: ', lista_de_palabras7)

#crear un diccionario y convertirlo en lista
lista_de_palabras7 = list(dict.fromkeys(lista_de_palabras7)) # que contenga solo valores unicos (keys)

print('La lista sin repeticiones es: ', lista_de_palabras7)


#=============================================================================================================#

# 8-Escriba un programa que permita crear dos listas de palabras y que, a continuación,
# escriba las siguientes listas (en las que no debe haber repeticiones):
#Lista de palabras que aparecen en las dos listas.
#Lista de palabras que aparecen en la primera lista, pero no en la segunda.
#Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.


print('Instrucciones: este programa crea dos listas de palabras, y crea lista de intersecciones entre ellas.')

print()


#Crear primero las dos listas
lista_de_palabras1 = []
lista_de_palabras2 = []
listas_combinadas = []
cantidad_palabras1 = int(input('Por favor digite el número de palabras de su primera lista  '))

for i in range(cantidad_palabras1):
    palabra1 = str(input('Por favor digite la palabra ' + str(i+1) + ' de la primera lista:  '))
    lista_de_palabras1.append(palabra1)
    listas_combinadas.append(palabra1)

print('La primera lista es: ', lista_de_palabras1)


cantidad_palabras2 = int(input('Por favor digite el número de palabras de su segunda lista  '))

for i in range(cantidad_palabras2):
    palabra2 = str(input('Por favor digite la palabra ' + str(i+1)+ ' de la segunda lista:  '))
    lista_de_palabras2.append(palabra2)
    listas_combinadas.append(palabra2)

print('La segunda lista es: ', lista_de_palabras2)

#Obtener las mismas listas sin repetidos
lista_de_palabras1 = list(dict.fromkeys(lista_de_palabras1))
lista_de_palabras2 = list(dict.fromkeys(lista_de_palabras2))
listas_combinadas = list(dict.fromkeys(listas_combinadas))


#sacar intersecciones:
#Lista de palabras que aparecen en las dos listas.

def interseccion(plista1, plista2): #plista1, plista2 son parametros
    a = set(plista1)
    b = set(plista2)

    return list(a & b)

lista_palabras_en_ambas_listas = interseccion(lista_de_palabras1, lista_de_palabras2)

print('Palabras que aparecen en las dos listas: ', lista_palabras_en_ambas_listas)


#Lista de palabras que aparecen en la primera lista, pero no en la segunda.
def returnNotMatches(plista1, plista2):
    a = set(plista1)
    b = set(plista2)
    return [list(b - a), list(a - b)]

solo_en_la_primera = returnNotMatches(lista_de_palabras1, lista_de_palabras2)[1]
solo_en_la_segunda = returnNotMatches(lista_de_palabras1, lista_de_palabras2)[0]

print('Palabras que sólo aparecen en la primera lista ', solo_en_la_primera)
print('Palabras que sólo aparecen en la segunda lista ', solo_en_la_segunda)

print('Todas las palabras: ', listas_combinadas)




