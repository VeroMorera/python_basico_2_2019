a = [1,3,4,8,9,2]


f = lambda x : x * 10

[f(i) for i in a]


#mas pythonico, escribir la funcion, el for, incluso un if al final.
[(lambda x: x * 10)(i) for i in a if i > 5]


# en este caso la funcion es muy simple se podria resolver


[i*10 for i in a]


#--------------------------------------------------------------------------------------------#

#Programacion orientada a objetos.

''' 
Para crear nuestros propios tipos de datos.

La clase mas sencilla que se puede crear es

class First:
    pass
    
una vez q se tiene la clase definida, se crea un objeto utilizando la linea de codigo

a = First()


'''