'''
TAREA1
Estudiante: Veronica Morera

Crear un archivo llamado tarea_1.py
Escribir un código en Python que imprima en pantalla lo siguiente:
* 3.1415926 ** 3.141592 *** 3.14159 **** 3.1415 ***** 3.141 ****** 3.14

usando el operador % para definir la cantidad de digitos decimales de PI y la cantidad de asteriscos.

'''




#variables
pi = 3.1415926
asteriscos = '******'

#formateo usando % para pi y slices para los asteriscos

print ( asteriscos[:1], '%.7f' % pi , asteriscos[:2], '%.6f' % pi, asteriscos[:3], '%.5f' % pi,
        asteriscos[:4], '%.4f' % pi, asteriscos[:5], '%.3f' % pi, asteriscos[:6], '%.2f' % pi  )
