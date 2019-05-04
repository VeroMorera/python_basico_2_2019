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


'''


#AUN ME FALTA TERMINAR ESTA PARTE   :(




Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Alberto
Dígame la palabra 2: Carmen
Dígame la palabra 3: Carmen
Dígame la palabra 4: Benito
La lista creada es: ['Alberto', 'Carmen', 'Carmen', 'Benito']
Palabra a eliminar: Carmen
La lista es ahora: ['Alberto', 'Benito']




Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.
Dígame cuántas palabras tiene la lista: 5
Dígame la palabra 1: Carmen
Dígame la palabra 2: Carmen
Dígame la palabra 3: Alberto
Dígame la palabra 4: Benito
Dígame la palabra 5: David
La lista creada es: ['Carmen', 'Carmen', 'Alberto', 'Benito', 'David']
Dígame cuántas palabras tiene la lista de palabras a eliminar: 3
Dígame la palabra 1: Benito
Dígame la palabra 2: Juan
Dígame la palabra 3: Carmen
La lista de palabras a eliminar es: ['Benito', 'Juan', 'Carmen']
La lista es ahora: ['Alberto', 'David']




Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Alberto
Dígame la palabra 2: Carmen
Dígame la palabra 3: Benito
Dígame la palabra 4: Daniel
La lista creada es: ['Alberto', 'Carmen', 'Benito', 'Daniel']
La lista inversa es: ['Daniel', 'Benito', 'Carmen', 'Alberto']



Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Alberto
Dígame la palabra 2: Carmen
Dígame la palabra 3: Benito
Dígame la palabra 4: Carmen
La lista creada es: ['Alberto', 'Carmen', 'Benito', 'Carmen']
La lista sin repeticiones es: ['Alberto', 'Carmen', 'Benito']



Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):
Lista de palabras que aparecen en las dos listas. Lista de palabras que aparecen en la primera lista, pero no en la segunda. Lista de palabras que aparecen en la segunda lista, pero no en la primera. Lista de palabras que aparecen en ambas listas. Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.

Dígame cuántas palabras tiene la primera lista: 4
Dígame la palabra 1: Carmen
Dígame la palabra 2: Alberto
Dígame la palabra 3: Benito
Dígame la palabra 4: Carmen
La primera lista es: ['Carmen', 'Alberto', 'Benito', 'Carmen']
Dígame cuántas palabras tiene la segunda lista: 3
Dígame la palabra 1: Benito
Dígame la palabra 2: Juan
Dígame la palabra 3: Carmen
La segunda lista es: ['Benito', 'Juan', 'Carmen']
Palabras que aparecen en las dos listas: ['Carmen', 'Benito']
Palabras que sólo aparecen en la primera lista: ['Alberto']
Palabras que sólo aparecen en la segunda lista: ['Juan']
Todas las palabras: ['Carmen', 'Benito', 'Alberto', 'Juan']
'''


