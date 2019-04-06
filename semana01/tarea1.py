'''
TAREA1
Estudiante: Veronica Morera

Crear un archivo llamado tarea_1.py
Escribir un código en Python que imprima en pantalla lo siguiente:
* 3.1415926 ** 3.141592 *** 3.14159 **** 3.1415 ***** 3.141 ****** 3.14

usando el operador % para definir la cantidad de digitos decimales de PI y la cantidad de asteriscos.

'''

# SOLUCION 1:

#variables
pi = 3.1415926
asteriscos = '******'

#formateo usando % para pi y slices para los asteriscos
print()
print('#SOLUCION 1')
print ( asteriscos[:1], '%.7f' % pi , asteriscos[:2], '%.6f' % pi, asteriscos[:3], '%.5f' % pi,
        asteriscos[:4], '%.4f' % pi, asteriscos[:5], '%.3f' % pi, asteriscos[:6], '%.2f' % pi  )

#==============================================================================================================#

#SOLUCION 2: Usando solo formateo, reduccion de codigo

print()
print('#SOLUCION 2')
print ( '%.1s %.7f' % (asteriscos, pi), '%.2s %.6f' % (asteriscos, pi), '...etc, etc') #etc, aqui el problema es
# que el formateo de floats me redondea el numero (Igual que en solucion1)

#==============================================================================================================#

#SOLUCION 3: Convertir pi a cadena de texto:

#variables
piStr = '3.1415926'
asteriscos = '******'

print()
print('#SOLUCION 3')
print ( '%.1s %.9s' % (asteriscos, piStr), '%.2s %.8s' % (asteriscos, piStr), '%.3s %.7s' % (asteriscos, piStr),
        '%.4s %.6s' % (asteriscos, piStr), '%.5s %.5s' % (asteriscos, piStr), '%.6s %.4s' % (asteriscos, piStr)    )

