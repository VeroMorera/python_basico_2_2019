'''

PROBLEMAS

1- crear un str con la palabra hola y el anio 2019

2- crear el decimal 3.14 basado en el str '3' y el str 0.14'

3- crear una lista de palabras usando la frase 'Hola_a_todos'

4- Crear un conjunto (set) de letras usando la frase 'Bienvenido'

'''
print()
#SOLUCION PROBLEMA 1

anio = 2019
saludo = 'Hola '

concatenado = saludo +  str(anio)
print(concatenado, type(concatenado))


#SOLUCION PROBLEMA 2
print()

enteroStr = '3'
decimalStr = '0.14'

pi = int(enteroStr) + float(decimalStr)
print( pi, type(pi))


#SOLUCION PROBLEMA 3
print()

frase = 'Hola_a_todos'

listaPalabras = frase.split('_')
print( listaPalabras, type(listaPalabras))


#SOLUCION PROBLEMA 4
print()

letras = set ('BIENVENIDOS')

print(letras, type(letras))



