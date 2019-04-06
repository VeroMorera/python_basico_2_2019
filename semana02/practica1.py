#pruebas con numeros

'''
hacer un codigo que calcule el area de un rectangulo


area es  largo * ancho
'''

#variables
largo = 10
ancho = 5

areaRectangulo = (10 * 5)

print('El area del rectangulo es: ', areaRectangulo)



#practica1, version dinamica


print('Instrucciones: este programa calcula el area de un rectangulo')

print()
largo = float(input('Por favor digite el largo del rectangulo   ')) #se pone float para que convierta el string a float
#print ('El valor del largo es', largo, 'el tipo de largo es', type(largo))

print()
ancho = float(input('Por favor digite el ancho del rectangulo   ')) #se pone float para que convierta el string a float
#print ('El valor del ancho es', ancho, 'el tipo de ancho es', type(ancho))


areaRectangulo = (largo * ancho)


print()
print ('El area del rectangulo es', areaRectangulo)

