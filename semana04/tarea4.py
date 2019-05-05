#La hoja de cálculo

#Suponga que se tiene una lista de listas que se tiene diversas cantidades por persona.
# La primera columna con números representa la cantidad en miles de colones que tienen en la cuenta del banco,
# la segunda columna la cantidad en crédito en miles de colones y la tercer columna en miles de colones en deuda.

hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]

#Suponga que se dispone de una función que procesa la lista
# para obtener la transpuesta(cambiar las columnas por las filas)

def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]
b = transpuesta(hoja_calculo)


#RESULTADO

b #sea b la tabla resultante luego de aplicar transpuesta
[['carlos', 'juan', 'luis'],
 [54.54, 5.54, 9.54],
 [6.57, 9.57, 7.57],
 [3.64, 4.64, 1.64]]


#Por otro lado, se puede aplicar matemática o cualquier otra operación a alguna fila en específico.
# Por ejemplo: dividir todos los números entre 10. Obteniendo:

''' 
b[1] = list(map(lambda x: x/10, b[1]))


#RESULTADO

b
[['carlos', 'juan', 'luis'],
 [5.454, 0.554, 0.954],
 [6.57, 9.57, 7.57],
 [3.64, 4.64, 1.64]]
'''
#========================================================================================================#

#----------------   PARTE 1   ----------------#

#Contruya un diccionario de funciones matematicas (utilizando funciones lambda)
# entre todos los números de la lista tales como: promedio, suma, multiplicacion

from functools import reduce

funciones_matematicas = {
                        'suma': lambda lista: sum(lista),
                        #'resta': lambda a, b: a - b,
                        'mult': lambda a, b: a * b,
                        #'division': lambda a, b: a / b,
                        'promedio': lambda lista: sum(lista) / len(lista)  # suma de todos los  valores de la lista, entre la cantidad de elementos de la misma.
                         }

#----------------   PARTE 2   ----------------#

#Obtenga utilizando el diccionario de funciones:

#1. El promedio de la cantidad miles de colones en débito: cuánto tienen en promedio todas las personas.

obtener_promedio = funciones_matematicas['promedio']
promedio_debito = obtener_promedio(b[1])

print( 'El promedio de todos los clientes es: ', promedio_debito)



#2. La suma de todas las deudas

obtener_suma = funciones_matematicas['suma']
suma_deudas = obtener_suma(b[3])

print( 'La suma de todas las deudas es: ', suma_deudas)




#3. la multiplicación de todos los crédito entre si

from functools import reduce

mult_creditos = reduce((funciones_matematicas['mult']), b[2])

print( 'La multiplicacion de todos los creditos es: ', mult_creditos)


#----------------   PARTE 3   ----------------#

#Actualice (en la tabla general)los valores de los créditos aplicando un impuesto del 20%
# (esto es multiplicar por 1.2) a toda la fila de créditos usando el diccionario de funciones.

impuesto_al_credito = []
obtener_mult =  funciones_matematicas['mult']

for credito in b[2]:
    impuesto_al_credito.append( obtener_mult(credito, 1.2))

print( 'Los creditos con impuesto del 20% son: ', impuesto_al_credito)