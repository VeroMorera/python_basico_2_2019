#crear un codigo que calcule las soluciones  de la ecuacion cuadratica de

#    ax^2 + bx + c = 0

#para resolver se usa:
#   x1 = (-b + math.sqrt(bˆ2 - 4ac)) / 2a


#    x2 = (-b - sqrt(bˆ2 - 4ac)) / 2a

# sqrt es raiz cuadrada
# 2 ** 2 es para hacer potencia


import math


a = float(input('Ingrese el valor de "a"   '))  #1

b = float(input('Ingrese el valor de "b"   '))   #2

c = float(input('Ingrese el valor de "c"   '))   #1


#mi solucion:
#x1 =  (-b + math.sqrt((b ** 2) - 4 *(a * c))) / (2 * a)
# print('x1: ', x1)


# x2 =  (-b - math.sqrt((b ** 2) - 4 *(a * c))) / (2 * a)
# print('x2: ', x2)


#OTRA SOLUCION (profe)

discriminante = b ** 2 - 4*a*c  #no hace falta parentesis, python entiende ordenes aritmeticos


if discriminante < 0:
    raiz = math.sqrt(-discriminante) * complex(0, 1) #numeros complejos i, j... se usan cuando hay raices negativas

else:
    raiz = math.sqrt(discriminante)

x1= (-b + raiz) / 2*a
x2= (-b - raiz) / 2*a

print(x1, x2)
