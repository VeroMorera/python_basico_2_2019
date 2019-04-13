'''

Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista.
Ejemplo

mis_valores = [5, 6, 10, 13, 3, 4]

Pueden usar cualquier estrategia pero que sea simple.

Considere si se tiene una lista que contiene las alturas de grupos de personas
todos = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135] # grupo 4

]

Escriba un código en python que determine cual grupo de personas contiene la mayor de todas las alturas de todas las personas

'''

#PRIMERA PARTE:

mis_valores = [5, 6, 10, 13, 3, 4]

mayor_valor = max(mis_valores)
print( 'El numero mayor de la lista "mis_valores" es', mayor_valor)


#SEGUNDA PARTE:

todos = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135] # grupo 4

]

def mayorDeVariasListas(listaCompleta):

    mayor_cada_grupo = [] #contenedor del mayor de cada grupo

    for lista in listaCompleta:

        mayor = max(lista) #sacar el mayor de cada grupo
        mayor_cada_grupo.append(mayor)  #agregar a la lista el mayor de cada grupo

    return mayor_cada_grupo

print('Los mayores de cada grupo en la lista "todos" son:', mayorDeVariasListas(todos))


mayor_de_todos = max(mayorDeVariasListas(todos))


print('El numero mayor de la lista "todos" es:', mayor_de_todos)


