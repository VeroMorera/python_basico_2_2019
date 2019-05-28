'''

Se propone crear una aplicación escrita en Python que permita la gestión de pacientes de una clínica.

a saber información clásica de paciente como:

identificación
Nombre
Apellido
teléfono
dirección
lista de enfermedades tratadas
lista de medicamentos que toma
Operaciones:

Ingreso de un paciente nuevo
Borrado de un paciente
Agregar más enfermedades en un paciente en particular
Agregar más medicamentos en un paciente en particular
Generar reporte de las enfermedades tratadas en la clínica
Generar reporte de los medicamentos entregados en la clínica
Comparar 2 pacientes en particular: cuales enfermedades tienen en común. Cuales no?. Lo mismo con los medicamentos.

'''
dictAgenda ={}
dictPaciente={}


persona=[]

def paciente(pnombre, papellido, ptel, pdireccion, penfermedades, pmedicamentos):


    lista_enfermedades = []
    lista_medicinas = []

    persona.append(pnombre)
    persona.append( papellido)
    persona.append(ptel)
    persona.append( pdireccion)
    persona.append( penfermedades)
    persona.append( pmedicamentos)



salir = False
while (salir == False):


    print('Instrucciones: ingrese los datos del paciente')

    print()
    id = int(input('Por favor digite la CEDULA del paciente'))
    nombre = input('Por favor digite el NOMBRE del paciente')
    apellido = input('Por favor digite el APELLIDO del paciente')
    telefono = int(input('Por favor digite el TELEFONO del paciente'))
    direccion = input('Por favor digite la DIRECCION del paciente')
    num_enfermedades = int(input('Por favor digite la CANTIDAD de ENFERMEDADES del paciente'))

    for i in range(num_enfermedades):

        enfermedad= input('Por favor ingrese la' + str(i+1) + ' enfermedad del paciente')
        lista_enfermedades.append(enfermedad)

    num_medicamentos = int(input('Por favor  digite la CANTIDAD de MEDICAMENTOS del paciente'))

    for i in range(num_medicamentos):
        medicina = input('Por favor digite la enfermedad ' + str(i + 1) + ' del paciente')
        lista_medicinas.append(medicina)


    paciente( nombre, apellido, telefono, direccion, lista_enfermedades, lista_medicinas)

    dictPaciente = {id: persona}
    dictAgenda.update(dictPaciente)

    cerrarPrograma = int(input('Desea agregar otro paciente? 1= si   0 = no'))
    if cerrarPrograma == 1:
        pass
    else: salir= True



print(dictAgenda)