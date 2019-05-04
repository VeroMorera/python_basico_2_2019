
mis_frutas = ['mango', 'kiwi', 'manzana', 'naranja', 'fresa', 'uva']
print(mis_frutas)

# consultar si elemento X esta en la lista, en este caso banano.
'banano' in mis_frutas


# consultar si elemento X NO esta en la lista, en este caso banano.
'banano' not in mis_frutas

#agregar una nueva fruta a la lista
mis_frutas.append('banano')


#agregar varios tipos de datos a la lista
mis_frutas.append('') #palabra vacia
mis_frutas.append(None)
mis_frutas.append(123)

otra_lista = []
mis_frutas.append(otra_lista)

print(mis_frutas)


pass  # significa do nothing


