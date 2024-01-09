
import json
from funcionesMenu import cargarEstudiantes, crearNuevoEstudiante, registroPrueba, rutaestudio, informaciondocentes

def menuPrograma():
    print("¡Bienvenido al Programa de Gestión de Estudiantes!")

    salir = False
    lista_estudiantes = cargarEstudiantes()  # Puedes cargar los estudiantes una vez al inicio del programa

    while not salir:
        try:
            pregunta = int(input("\n1. Consultar información de los estudiantes."
                                "\n2. Ingresar un nuevo estudiante."
                                "\n3. Registrar la prueba."
                                "\n4. Elegir ruta de estudio."
                                "\n5. Informacion de los docentes."
                                "\n6. Salir"
                                "\n¿Qué opción desea ingresar?: "))

            match pregunta:
                case 1:
                    cargarEstudiantes()
                case 2:
                    crearNuevoEstudiante()
                case 3:
                    registroPrueba()
                case 4:
                    rutaestudio()
                case 5:
                    informaciondocentes(lista_estudiantes)
                case 6:
                    print("Hasta luego, que tenga un buen día")
                    salir = True
                case _:
                    print("Opción no válida. Inténtelo de nuevo.")

        except ValueError:
            print("Por favor, ingrese un número válido.")

menuPrograma()



#import json
#
#from funcionesMenu import cargarEstudiantes, crearNuevoEstudiante, registroPrueba, rutaestudio
#
#def menuPrograma():
#
#    salir = False
#    lista_estudiantes = cargarEstudiantes()
#
#    while  not salir:
#
#        pregunta = int(input("\n1.Si desea consultar información de los estudiantes."
#                            "\n2.Si desea ingresar un nuevo estudiante."
#                            "\n3.Para registrar la prueba. "
#                            "\n4.Elegir ruta de estudio. "
#                            "\n5.Para Salir" 
#                            "\n¿Qué opción desea ingresar?: "))
#
#        match pregunta:
#
#            case 1:
#
#                cargarEstudiantes()
#
#            case 2:
#
#                crearNuevoEstudiante()
#
#            case 3:
#
#
#                registroPrueba()
#
#            case 4:
#                
#                rutaestudio()
#
#            case 5:
#                print("Hasta luego, que tenga un buen día")
#                salir = True
#
#
#menuPrograma()