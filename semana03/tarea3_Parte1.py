#    --------------------   PRIMERA PARTE   --------------------   #


#Suponga que un hospital abre la atención de pacientes muy temprano. Uno a uno personas van llegando al hospital.
#Llega la primer persona y la secretaria apunta sus datos personas y la razón de la consulta.

# Para definir la agenda del hospital
agenda_hospital = []
persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')

# agregamos una persona
agenda_hospital.append(persona)

# viene otra persona
persona = ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')

# agregamos otra persona
agenda_hospital.append(persona)


# suponga que vienen 5 personas mas

persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]


# Podemos agregar esas personas que vienen todos de una sola vez
agenda_hospital.extend(persona)


#Primera pregunta:  Cuantos pacientes llegaron en total?

total_pacientes = len(agenda_hospital)
print('El total de pacientes es ', total_pacientes)


#=============================================================================================================#

#Segunda pregunta: Cuantas personas llegaron por dolor?

acumulador = 0

for paciente in agenda_hospital:
    if paciente[5] == 'dolor':     #profe aqui usé un if, porque fue lo único que se me ocurrió :S
        acumulador += 1

print('Las personas que llegaron por dolor son ', acumulador)

#=============================================================================================================#

#Tercera pregunta: Suponga que se atienden con orden de prioridad por edad, empezando por el adulto mayor.
# Ordene la lista desde el más adulto al más joven

# funcion para ordenar tuplas

def ordenar_tupla(tup):

    # reverse = para q vaya de mayor a de mayor a menor
    # key para seleccionar los elementos de la tupla, no la tupla completa

    tup.sort(key=lambda x: x[3], reverse=True) #pongo el numero 3 porque el tercer valor  de la tupla es la edad.
    return tup

for paciente in ordenar_tupla(agenda_hospital):
    print(paciente)

#=============================================================================================================#


#Cuarta Pregunta: Cuantos pacientes son mayores de edad? cuantos menores?

acumulador = 0

for paciente in agenda_hospital:
    edad = paciente[3]

    if edad >= 18:
        acumulador += 1

print('El total de personas mayores de edad es ', acumulador)

#=============================================================================================================#

#Quinta Pregunta: Suponga que se atienden con orden de prioridad por gravedad de consulta,
# empezando por los que tienen dolor y luego por edad (mas viejo al joven), empezando por el adulto mayor.
#  Ordene la lista empenzando por los que tienen mayor prioridad.



def ordenar_tupla(tup):

    # reverse = para q vaya de mayor a de mayor a menor
    # key para seleccionar los elementos de la tupla, no la tupla completa

    tup.sort(key=lambda x: x[3], reverse=True)
    return tup


agenda_prioridad = []

#agregar primero en orden de prioridad los q tienen dolor, pero de una vez ordenados de mayor a menor
for paciente in ordenar_tupla(agenda_hospital):
    if paciente[5] == 'dolor':
        agenda_prioridad += (paciente, )


#agregar el resto de personas, igual de mayor a menor
for paciente in ordenar_tupla(agenda_hospital):

    if paciente[5] != 'dolor':
        agenda_prioridad += (paciente, )

#imprimir la lista prioridad
for paciente in agenda_prioridad:
    print(paciente)


#=============================================================================================================#

#Sexta pregunta: Suponga que los que tienen dolor mueren :(
# Como queda la lista de pacientes vivos por atender ordenados por orden de edad desde el joven al viejo.


for paciente in agenda_hospital:
    if paciente[5] == 'dolor':
        agenda_hospital.remove(paciente) #aqui no me queda claro porqué no saca a Pedro de la lista...

for paciente in agenda_hospital:
    print(paciente)



