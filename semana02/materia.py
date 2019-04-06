'''
*** usos de python

framework de python
django - back end web
anaconda - data science
flask - web develop
SQL archemy - bases de datos

tambien se usa para bussiness analysis.


 ---------------------------------------------

 *** tipos de datos comunes (son datos inmutables, no se puede remplazar el contenido)


 int --- numeros enteros -0, 5, 4 binarios (0b010), octales (Oo642), hexa. (0xF3)

 float ---- numeros con decimal (0.234), notacion cientifica (-1.7e-6)

 bool --- True, False, 0, 1

 str ----  "cadenas de texto"

 bytes ----- b"toto\xfe\775  ----hexadecimal, octal.

  ---------------------------------------------

*** tipado dinamico : quiere decir que se puede convertir una variable entera a una variable flotante
  con solo cambiar el valor, ya que en python no se declara el tipo de dato, python lo interpreta solo.

  ---------------------------------------------

*** Identifiers (convencion de nombres de variables)

  usar solo caracteres simples, mayusculas, minusculas, numeros.
  El sistema es sensible a las mayusculas.
  no empezar variables con numeros, ni palabras reservadas del lenguaje.


*** Variables assigment

  x = 1.2+8+sin(y)
  a=b=b= 0
  y,z, r = 9.2, 7, 0
  a,b = b, a    # Estas son para hacer switch de valores


#unpacking of secuence in item and list
  a, *b=seq
  *a, b = seq

ejemplo 1
  a, b* = [0,1,2,3]
  a= 0
  b= [1,2,3]

ejemplo 2
  *a, b = [0,1,2,3]
  a= [0,1,2]
  b= 3


    ---------------------------------------------
incrementacion
  x += 3 #incrementar de 3 en 3
  x-= 2  #decrementar de 2 en 2

tambien se puede con
  *=
  /=
  %=

  x = None  #constante indefinida
  del x  # para borrar

    ---------------------------------------------

Conversiones

    si tengo un string ("15") lo puedo convertir a entero int("15")
    y asi con todos los datos.

redondear: float(round(0.344533))

    chr(64)  ----> @

listas
    list('abc') ----> ['a' 'b', 'c']

diccionarios
    dict [(3, 'three'), (1, 'one')]  ----> { 1: 'one', 3: 'three' }

x = dict ([(A', a'), ('B,' 'b')])

x(B)  -----> 'b'=


bool
    da false cuando se usa bool(0)   , bool(0.0),    bool(None),     bool(')'
    da true en cualquier otra circunstancia


set # tambien se conoce como conjuntos
    set ["one, "two"] ----> {'one', 'two'}


truncar: (remover la parte decimal)
    int(12.224)

da error:
    int('12.224') #no puede ser cadena de texto, debe ser float.


separar una lista de palabras

    'la casa es mia'.split('_') -----> ['la', 'casa', 'es', 'mia' ]


'''

