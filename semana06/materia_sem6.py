'''
datos: listas, tuplas, sets, diccionarios

clases: herencia, polimorfismo

funciones: lambdas, comunes.

modulos:  tema de hoy* (elementos de librerias que se pueden crear u obtener para el codigo propio)

archivos: txt, csv, pickle (permite la serializacion)    tema de hoy*

expresiones regulares: expresiones que permiten reemplazar, validar elementos, entre otros.


'''

#ARCHIVOS

f = open('mis_datos.txt')

#from os import path


""" 

#home/usuario/directorio/archivo.txt

ruta_archivo = path.joint('directorio', 'archivo.txt') #ver ejemplo linea 24

archivo = open(ruta_archivo)
contenido = archivo.read()
archivo.close()  #es requerido cerrar un archivo.
contenido


#ESCRITURA

archivo = open('texto.txt', 'w')
#se escriben algunas lineas
archivo.write('primera linea \n')
archivo.write('segunda linea \n')

#y se cierra el archivo para q el sistema lo actualice.
archivo.close()


#se recomienda usar 'with', el with hace close automaticamente


with open('data.txt', 'w') as f:
    f.write('Hello\n')
                                        
#LECTURA

with open('data.txt', 'r') as f:  #la r no es necesaria, pero se usa para documentar el hecho de que esta leyendo. 
                                 # El programa lo hace por defecto.
    text = f.read()

"""