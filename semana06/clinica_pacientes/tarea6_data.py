import json
import semana06.clinica_pacientes.tarea6 as tools


data = {}
data['pacientes'] = []
paciente = {}
lista_enfermedades = []
lista_medicinas =[]

salir = False
while (salir == False):

    print('Menu: Elija un número'+ '\n' + '\n'
        '1- registrar paciente' + '\n'
        '2- listar pacientes' + '\n'
        '3- borrar pacientes' + '\n'
        '4- agregar medicamentos' + '\n'
        '5- agregar enfermedades' + '\n'
        '6- enfermedades tratadas' + '\n'
        '7- medicamentos recetados' + '\n'
        '8- comparar pacientes' + '\n'
        '9- salir' + '\n')

    response = int(input(''))

    if response == 1:

        def registrar_paciente():

            print('Instrucciones: ingrese los datos del paciente')

            id = int(input('Por favor digite la CEDULA del paciente'))
            nombre = input('Por favor digite el NOMBRE del paciente')
            apellido = input('Por favor digite el APELLIDO del paciente')
            telefono = int(input('Por favor digite el TELEFONO del paciente'))
            direccion = input('Por favor digite la DIRECCION del paciente')
            num_enfermedades = int(input('Por favor digite la CANTIDAD de ENFERMEDADES del paciente'))
            for i in range(num_enfermedades):
                enfermedad = input('Por favor ingrese la' + str(i + 1) + ' enfermedad del paciente')
                lista_enfermedades.append(enfermedad)

            num_medicamentos = int(input('Por favor  digite la CANTIDAD de MEDICAMENTOS del paciente'))

            for i in range(num_medicamentos):
                medicina = input('Por favor digite la enfermedad ' + str(i + 1) + ' del paciente')
                lista_medicinas.append(medicina)

            id = {'identificación': id, 'Nombre': nombre, 'Apellido': apellido, 'teléfono': telefono,
                  'dirección': direccion, 'lista_de_enfermedades_tratadas': lista_enfermedades,
                  'lista_de_medicamentos_que_toma': lista_medicinas}


            data['pacientes'].append(
                tools.la_clinica.agregar_paciente(**id)
            )

    elif response == 2:

        def listar_paciente():


            with open('clinica_pacientes/base_datos_clinica.txt', 'w') as outfile:
                json.dump(data, outfile)

            # ABRIR BASE DE DATOS
            from pprint import pprint

            with open('clinica_pacientes/base_datos_clinica.txt') as json_file:
                json_data = json.load(json_file)
                pprint(json_data)

        listar_paciente()

    elif response == 3:
        id = int(input('Por favor digite la CEDULA del paciente'))
        tools.la_clinica.borrar_paciente(id)


    elif response == 4:
        id = int(input('Por favor digite la CEDULA del paciente'))
        med =input('Por favor digite el nuevo MEDICAMENTO del paciente')
        tools.la_clinica.agregar_medicinas(identificacion=id,nuevo_medicamento=med)


    elif response == 5:
        id = int(input('Por favor digite la CEDULA del paciente'))
        enf = input('Por favor digite la nueva ENFERMEDAD del paciente')
        tools.la_clinica.agregar_enfermedades(identificacion=id,nuevo_medicamento=enf)


    elif response == 6:
        reporte_enfermedades_tratadas = la_clinica.enfermedades_tratadas()
        print(reporte_enfermedades_tratadas)

    elif response == 7:
        reporte_medicamentos_recetados = tools.la_clinica.medicamentos_recetados()
        print(reporte_medicamentos_recetados)

    elif response == 8:
        id1 = int(input('Por favor digite la CEDULA del paciente 1'))
        id2 = int(input('Por favor digite la CEDULA del paciente 2'))
        tools.la_clinica.comparar_pacientes(id1, id2)

    elif response == 9:
        print('Gracias por usar esta aplicación')
        salir == True
        break

    else:
        print('Opción Inválida')
