
import json

capacidad_actual = {
    "Ruta NodeJS - Salon 1 - 06:00 AM - 10:00 AM": 0,
    "Ruta NodeJS - Salon 1 - 10:00 AM - 12:00 PM": 0,
    "Ruta NodeJS - Salon 1 - 12:00 PM - 04:00 PM": 0,
    "Ruta NodeJS - Salon 1 - 04:00 PM - 06:00 PM": 0,
    "Ruta NodeJS - Salon 1 - 06:00 PM - 10:00 PM": 0,
    "Ruta Java - Salon 2 - 06:00 AM - 10:00 AM": 0,
    "Ruta Java - Salon 2 - 10:00 AM - 12:00 PM": 0,
    "Ruta Java - Salon 2 - 12:00 PM - 04:00 PM": 0,
    "Ruta Java - Salon 2 - 04:00 PM - 06:00 PM": 0,
    "Ruta Java - Salon 2 - 06:00 PM - 10:00 PM": 0,
    "Ruta NetCore - Salon 3 - 06:00 AM - 10:00 AM": 0,
    "Ruta NetCore - Salon 3 - 10:00 AM - 12:00 PM": 0,
    "Ruta NetCore - Salon 3 - 12:00 PM - 04:00 PM": 0,
    "Ruta NetCore - Salon 3 - 04:00 PM - 06:00 PM": 0,
    "Ruta NetCore - Salon 3 - 06:00 PM - 10:00 PM": 0
}

def cargarEstudiantes():
    estudiantes = []

    try:
        with open("estudiantes.json") as file:
            estudiantes = json.load(file)

        if estudiantes is not None:
            salir = False
            while not salir:
                ask = int(input("\n1.Desea ver información básica de los estudiantes. "
                                "\n2.Saber el estado y en qué ruta de estudio está. "
                                "\n3.Conocer horario de estudio. "
                                "\n4.Ver estudiantes que solo aprobaron el examen inicial."
                                "\n5.Ver menú completo. "))

                match ask:
                    case 1:
                        for estudiante in estudiantes:
                            print("Nombre:", estudiante["nombre"], "Edad:", estudiante["edad"], "Celular:", estudiante["telefono Celular"])
                    case 2:
                        for estudiante in estudiantes:
                            print("Nombre:", estudiante["nombre"], "Estado:", estudiante["estado"], "Ruta:", estudiante["ruta"])
                    case 3:
                        for estudiante in estudiantes:
                            print("Nombre:", estudiante["nombre"])
                    case 4:
                        EstAprobadosOAsignados(estudiantes)
                    case 5:
                        print("Regresando al menú anterior. ")
                        salir = True
                    case _:
                        print("Opción no válida. Por favor, elija una opción del 1 al 4.")

            return estudiantes
        else:
            print("El archivo 'estudiantes.json' está vacío o tiene un formato incorrecto.")
            return []

    except FileNotFoundError:
        print("El archivo 'estudiantes.json' no existe. Puede que aún no haya estudiantes guardados.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
        return []
    except Exception as e:
        print("Error desconocido:", e)
        return []


def EstAprobadosOAsignados(estudiantes):
    estudiantes_filtrados = [estudiante for estudiante in estudiantes if estudiante["estado"].lower() in ["aprobado", "asignado"]]

    if estudiantes_filtrados:
        print("\nEstudiantes con estado 'Aprobado' o 'Asignado':")
        for estudiante in estudiantes_filtrados:
            print("Nombre:", estudiante["nombre"], "Estado:", estudiante["estado"], "Ruta:", estudiante["ruta"])
    else:
        print("\nNo hay estudiantes con estado 'Aprobado' o 'Asignado'.")

def EstudiantesNaruto(estudiantes):
    EstudiantesNaruto = [estudiante for estudiante in estudiantes if estudiante["docente"].lower() == "naruto"]

    if EstudiantesNaruto:
        print("\nEstudiantes a cargo de Naruto y sus horarios:")
        for estudiante in EstudiantesNaruto:
            print("Nombre:", estudiante["nombre"], "Horario:", estudiante["horario"])
    else:
        print("\nEste docente aún no tiene estudiantes")

def EstudiantesItachi(estudiantes):
    EstudiantesItachi = [estudiante for estudiante in estudiantes if estudiante["docente"].lower() in ["itachi"]]

    if EstudiantesItachi:
        print("\nEstudiantes a cargo de Itachi y sus horarios:")
        for estudiante in EstudiantesItachi:
            print("Nombre:", estudiante["nombre"], "Horario:", estudiante["horario"])
    else:
        print("\nEste docente aun no tiene estudiantes")

def EstudiantesSakura(estudiantes):
    EstudiantesSakura = [estudiante for estudiante in estudiantes if estudiante["docente"].lower() in ["sakura"]]

    if EstudiantesSakura:
        print("\nEstudiantes a cargo de Sakura y sus horarios:")
        for estudiante in EstudiantesSakura:
            print("Nombre:", estudiante["nombre"], "Horario:", estudiante["horario"])
    else:
        print("\nEste docente aun no tiene estudiantes")

def EstudiantesEdward(estudiantes):
    EstudiantesEdward = [estudiante for estudiante in estudiantes if estudiante["docente"].lower() in ["edward"]]

    if EstudiantesEdward:
        print("\nEstudiantes a cargo de Edward y sus horarios:")
        for estudiante in EstudiantesEdward:
            print("Nombre:", estudiante["nombre"], "Horario:", estudiante["horario"])
    else:
        print("\nEste docente aun no tiene estudiantes")

def EstudiantesAlphonse(estudiantes):
    EstudiantesAlphonse = [estudiante for estudiante in estudiantes if estudiante["docente"].lower() in ["alphonse"]]

    if EstudiantesAlphonse:
        print("\nEstudiantes a cargo de Alphonse y sus horarios:")
        for estudiante in EstudiantesAlphonse:
            print("Nombre:", estudiante["nombre"], "Horario:", estudiante["horario"])
    else:
        print("\nEste docente aun no tiene estudiantes")

def EstudiantesRoy(estudiantes):
    EstudiantesRoy = [estudiante for estudiante in estudiantes if estudiante["docente"].lower() in ["roy"]]

    if EstudiantesRoy:
        print("\nEstudiantes a cargo de Roy y sus horarios:")
        for estudiante in EstudiantesRoy:
            print("Nombre:", estudiante["nombre"], "Horario:", estudiante["horario"])
    else:
        print("\nEste docente aun no tiene estudiantes")

def EstudiantesLuffy(estudiantes):
    EstudiantesLuffy = [estudiante for estudiante in estudiantes if estudiante["docente"].lower() in ["luffy"]]

    if EstudiantesLuffy:
        print("\nEstudiantes a cargo de Luffy y sus horarios:")
        for estudiante in EstudiantesLuffy:
            print("Nombre:", estudiante["nombre"], "Horario:", estudiante["horario"])
    else:
        print("\nEste docente aun no tiene estudiantes")


def EstudiantesZoro(estudiantes):
    EstudiantesZoro = [estudiante for estudiante in estudiantes if estudiante["docente"].lower() in ["zoro"]]

    if EstudiantesZoro:
        print("\nEstudiantes a cargo de Zoro y sus horarios:")
        for estudiante in EstudiantesZoro:
            print("Nombre:", estudiante["nombre"], "Horario:", estudiante["horario"])
    else:
        print("\nEste docente aun no tiene estudiantes")

def EstudiantesChopper(estudiantes):
    EstudiantesChopper = [estudiante for estudiante in estudiantes if estudiante["docente"].lower() in ["chopper"]]

    if EstudiantesChopper:
        print("\nEstudiantes a cargo de Chopper y sus horarios:")
        for estudiante in EstudiantesChopper:
            print("Nombre:", estudiante["nombre"], "Horario:", estudiante["horario"])
    else:
        print("\nEste docente aun no tiene estudiantes")

def informaciondocentes(estudiantes):
    
    try:
        with open("estudiantes.json") as file:
            estudiantes = json.load(file)

        if estudiantes is not None:
            salir = False
            while not salir:
                ask = int(input("\n1.Docentes trabajando con nostros. "
                                "\n2.Estudiantes a cargo. "
                                "\n3.Ver menú completo. "))

                match ask:
                    case 1:
                        print("\n------- Ruta NodeJS-------"
                              "\nNaruto - Itachi - Sakura"
                              "\n------- Ruta NetCore-------"
                              "\nEdward - Alphonse - Roy"
                              "\n------- Ruta Java-------"
                              "\nLuffy - Zoro - Chopper")
                    case 2:
                        qask =int(input("\n¿Con que docente?"
                                        "\n1. Naruto. "
                                        "\n2. Itachi. "
                                        "\n3. Sakura. "
                                        "\n4. Edward. "
                                        "\n5. Alphonse. "
                                        "\n6. Roy. "
                                        "\n7. Luffy. "
                                        "\n8. Zoro. "
                                        "\n9. Chopper. "
                                        "\n10. Salir. "))
                        match qask:

                            case 1:
                                EstudiantesNaruto(estudiantes)
                            case 2:
                                EstudiantesItachi(estudiantes)
                            case 3:
                                EstudiantesSakura(estudiantes)
                            case 4:
                                EstudiantesEdward(estudiantes)
                            case 5:
                                EstudiantesAlphonse(estudiantes)
                            case 6:
                                EstudiantesRoy(estudiantes)
                            case 7:
                                EstudiantesLuffy(estudiantes)
                            case 8:
                                EstudiantesZoro(estudiantes)
                            case 9:
                                EstudiantesChopper(estudiantes)
                            case 10:
                                print("Regresando al menú anterior.")
                                salir = True
                            case _:
                                print("Opción no válida. Por favor, elija una opción del 1 al 10.")
                    case 3:
                        print("Regresando al menú anterior. ")
                        salir = True
                    case _:
                        print("Opción no válida. Por favor, elija una opción del 1 al 4.")

            return estudiantes
        else:
            print("El archivo 'estudiantes.json' está vacío o tiene un formato incorrecto.")
            return []

    except FileNotFoundError:
        print("El archivo 'estudiantes.json' no existe. Puede que aún no haya estudiantes guardados.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
        return []
    except Exception as e:
        print("Error desconocido:", e)
        return []


    

def cargarCapacidad():
    capacidad_actual_local = {
        "Ruta NodeJS - Salon 1 - 06:00 AM - 10:00 AM": 0,
        "Ruta NodeJS - Salon 1 - 10:00 AM - 12:00 PM": 0,
        "Ruta NodeJS - Salon 1 - 12:00 PM - 04:00 PM": 0,
        "Ruta NodeJS - Salon 1 - 04:00 PM - 06:00 PM": 0,
        "Ruta NodeJS - Salon 1 - 06:00 PM - 10:00 PM": 0,
        "Ruta Java - Salon 2 - 06:00 AM - 10:00 AM": 0,
        "Ruta Java - Salon 2 - 10:00 AM - 12:00 PM": 0,
        "Ruta Java - Salon 2 - 12:00 PM - 04:00 PM": 0,
        "Ruta Java - Salon 2 - 04:00 PM - 06:00 PM": 0,
        "Ruta Java - Salon 2 - 06:00 PM - 10:00 PM": 0,
        "Ruta NetCore - Salon 3 - 06:00 AM - 10:00 AM": 0,
        "Ruta NetCore - Salon 3 - 10:00 AM - 12:00 PM": 0,
        "Ruta NetCore - Salon 3 - 12:00 PM - 04:00 PM": 0,
        "Ruta NetCore - Salon 3 - 04:00 PM - 06:00 PM": 0,
        "Ruta NetCore - Salon 3 - 06:00 PM - 10:00 PM": 0
    }

    try:
        with open("capacidad.json") as file:
            capacidad_actual_local = json.load(file)
    except FileNotFoundError:
        print("El archivo 'capacidad.json' no existe. Se utilizará la capacidad inicial.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON 'capacidad.json'. Se utilizará la capacidad inicial.")
    except Exception as e:
        print("Error desconocido:", e)

    return capacidad_actual_local

def guardarCapacidad(capacidad_actual):
    try:
        with open("capacidad.json", 'w') as archivo_json:
            json.dump(capacidad_actual, archivo_json, indent=2)
            print("La capacidad actual de las aulas ha sido guardada")
    except Exception as e:
        print("Error al guardar la capacidad actual:", e)

# Cargar la capacidad actual desde el archivo
capacidad_actual = cargarCapacidad()

lista_estudiantes = cargarEstudiantes()


def guardar_json(lista_estudiantes):
    try:
        with open("estudiantes.json", 'w') as archivo_json:
            json.dump(lista_estudiantes, archivo_json, indent=2)
            print("La lista de estudiantes ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya estudiantes guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:", e)


def crearNuevoEstudiante():
    global lista_estudiantes

    nuevoEstudiante = {}

    nuevoEstudiante["nombre"] = input("Ingrese el nombre del estudiante: ")
    nuevoEstudiante["edad"] = int(input("Ingrese la edad del estudiante: "))
    nuevoEstudiante["telefono Celular"] = int(input("Ingrese el número de celular: "))
    nuevoEstudiante["acudiente"] = (input("Nombre y número de contacto"))
    nuevoEstudiante["No Identificacion"] = int(input("Ingrese el número de documento: "))
    nuevoEstudiante["direccion"] = (input("Ingrese la dirección"))
    nuevoEstudiante["estado"] = "inscrito"
    nuevoEstudiante["ruta"] = "Sin asignar"
    nuevoEstudiante["docente"] = "Sin asignar"
    nuevoEstudiante["aula"] = "Sin asignar"
    nuevoEstudiante["horario"] = "Sin asignar"
    

    lista_estudiantes.append(nuevoEstudiante)

    guardar_json(lista_estudiantes)


def registroPrueba():
    global lista_estudiantes

    for estudiante in lista_estudiantes:
        if estudiante["estado"].lower() == "inscrito":
            print("{} Usted puede presentar la prueba ya que su estado es {}".format(estudiante["nombre"], estudiante["estado"]))

            notaTeorica = int(input("Cuál es el resultado de su nota teórica: "))
            notaPractica = int(input("Cuál es el resultado de su nota práctica: "))

            promedio = (notaPractica + notaTeorica) / 2

            if promedio >= 60:
                estudiante["estado"] = "Aprobado"
                print("Usted logró superar el promedio de la prueba con un {}".format(promedio))
            else:
                estudiante["estado"] = "Reprobado"
                print("Usted no logró superar el promedio su nota fue {} ".format(promedio))
        else:
            print("{} no puedes presentar la prueba porque su estado es {}".format(estudiante["nombre"], estudiante["estado"]))

    guardar_json(lista_estudiantes)




def rutaestudio():
    global lista_estudiantes
    global capacidad_actual

    for estudiante in lista_estudiantes:
        print("\nCapacidad Actual:")
        for ruta, capacidad in capacidad_actual.items():
            print(f"{ruta}: {capacidad} estudiantes")

        if estudiante["estado"].lower() == "aprobado":
            print("{} Usted puede elegir la ruta de entrenamiento".format(estudiante["nombre"]))

            salir = False
            while not salir:
                print("\n1. Clases de Ruta NodeJS."
                      "\n2. Clases de Ruta Java."
                      "\n3. Clases de Ruta NetCore."
                      "\n4. Elegir mi ruta más tarde.")

                opcion_ruta = int(input("Seleccione la ruta (1-4): "))

                if opcion_ruta == 1:
                    print("\nClases de Ruta NodeJS:"
                          "\n1. Con el Docente: Naruto, Salon 1, de 06:00 AM a 10:00 AM."
                          "\n2. Con el Docente: Naruto, Salon 1, de 10:00 AM a 12:00 PM."
                          "\n3. Con el Docente: Itachi, Salon 1, de 12:00 PM a 04:00 PM."
                          "\n4. Con el Docente: Itachi, Salon 1, de 04:00 PM a 06:00 PM."
                          "\n5. Con la Docente: Sakura, Salon 1, de 06:00 PM a 10:00 PM."
                          "\n6. Elegir mi horario luego.")

                    opcion_horario = int(input("Seleccione una opción (1-6): "))
                    if 1 <= opcion_horario <= 5:
                        estudiante["ruta"] = "Ruta NodeJS"
                        estudiante["estado"] = "asignado"
                        estudiante["docente"] = "Naruto" if opcion_horario in [1, 2] else "Itachi" if opcion_horario in [3, 4] else "Sakura"
                        estudiante["aula"] = "Salon 1"
                        estudiante["horario"] = [
                            "06:00 AM - 10:00 AM",
                            "10:00 AM - 12:00 PM",
                            "12:00 PM - 04:00 PM",
                            "04:00 PM - 06:00 PM",
                            "06:00 PM - 10:00 PM"
                        ][opcion_horario - 1]
                        
                        # Verificar si hay más de 33 por aula
                        ruta_actual = estudiante["ruta"] + " - " + estudiante["aula"] + " - " + estudiante["horario"]
                        if capacidad_actual.get(ruta_actual, 0) < 33:
                            capacidad_actual[ruta_actual] += 1
                            salir = True
                        else:
                            print("La capacidad máxima de estudiantes en esta ruta, aula y horario se ha alcanzado. Elija otra opción.")

                    elif opcion_horario == 6:
                        print("Aún no has elegido tu horario.")
                        salir = True
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")

                elif opcion_ruta == 2:
                    print("\nClases de Ruta Java:"
                          "\n1. Con el Docente: Luffy, Salon 2, de 06:00 AM a 10:00 AM."
                          "\n2. Con el Docente: Luffy, Salon 2, de 10:00 AM a 12:00 PM."
                          "\n3. Con el Docente: Zoro, Salon 2, de 12:00 PM a 04:00 PM."
                          "\n4. Con el Docente: Zoro, Salon 2, de 04:00 PM a 06:00 PM."
                          "\n5. Con el Docente: Chopper, Salon 2, de 06:00 PM a 10:00 PM."
                          "\n6. Elegir mi horario luego.")

                    opcion_horario = int(input("Seleccione una opción (1-6): "))
                    if 1 <= opcion_horario <= 5:
                        estudiante["ruta"] = "Ruta Java"
                        estudiante["estado"] = "asignado"
                        estudiante["docente"] = "Luffy" if opcion_horario in [1, 2] else "Zoro" if opcion_horario in [3, 4] else "Chopper"
                        estudiante["aula"] = "Salon 2"
                        estudiante["horario"] = [
                            "06:00 AM - 10:00 AM",
                            "10:00 AM - 12:00 PM",
                            "12:00 PM - 04:00 PM",
                            "04:00 PM - 06:00 PM",
                            "06:00 PM - 10:00 PM"
                        ][opcion_horario - 1]

                        # Verificar si hay más de 33 por aula
                        ruta_actual = estudiante["ruta"] + " - " + estudiante["aula"] + " - " + estudiante["horario"]
                        if capacidad_actual.get(ruta_actual, 0) < 33:
                            capacidad_actual[ruta_actual] += 1
                            salir = True
                        else:
                            print("La capacidad máxima de estudiantes en esta ruta, aula y horario se ha alcanzado. Elija otra opción.")

                    elif opcion_horario == 6:
                        print("Aún no has elegido tu horario.")
                        salir = True
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")

                elif opcion_ruta == 3:
                    print("\nClases de Ruta NetCore:"
                          "\n1. Con el Docente: Edward, Salon 3, de 06:00 AM a 10:00 AM."
                          "\n2. Con el Docente: Edward, Salon 3, de 10:00 AM a 12:00 PM."
                          "\n3. Con el Docente: Alphonse, Salon 3, de 12:00 PM a 04:00 PM."
                          "\n4. Con el Docente: Alphonse, Salon 3, de 04:00 PM a 06:00 PM."
                          "\n5. Con el Docente: Roy, Salon 3, de 06:00 PM a 10:00 PM."
                          "\n6. Elegir mi horario luego.")

                    opcion_horario = int(input("Seleccione una opción (1-6): "))
                    if 1 <= opcion_horario <= 5:
                        estudiante["ruta"] = "Ruta NetCore"
                        estudiante["estado"] = "asignado"
                        estudiante["docente"] = "Edward" if opcion_horario in [1, 2] else "Alphonse" if opcion_horario in [3, 4] else "Roy"
                        estudiante["aula"] = "Salon 3"
                        estudiante["horario"] = [
                            "06:00 AM - 10:00 AM",
                            "10:00 AM - 12:00 PM",
                            "12:00 PM - 04:00 PM",
                            "04:00 PM - 06:00 PM",
                            "06:00 PM - 10:00 PM"
                        ][opcion_horario - 1]

                        # Verificar si hay más de 33 por aula
                        ruta_actual = estudiante["ruta"] + " - " + estudiante["aula"] + " - " + estudiante["horario"]
                        if capacidad_actual.get(ruta_actual, 0) < 33:
                            capacidad_actual[ruta_actual] += 1
                            salir = True
                        else:
                            print("La capacidad máxima de estudiantes en esta ruta, aula y horario se ha alcanzado. Elija otra opción.")

                    elif opcion_horario == 6:
                        print("Aún no has elegido tu horario.")
                        salir = True
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")

                elif opcion_ruta == 4:
                    print("\nElegir mi ruta más tarde.")
                    salir = True

                else:
                    print("Opción no válida. Inténtalo de nuevo.")
                    # Verificar si hay más de 33 por aula
                    ruta_actual = estudiante["ruta"] + " - " + estudiante["aula"] + " - " + estudiante["horario"]
                    if capacidad_actual.get(ruta_actual, 0) < 33:
                        capacidad_actual[ruta_actual] += 1
                        salir = True
                    else:
                        print("La capacidad máxima de estudiantes en esta ruta, aula y horario se ha alcanzado. Elija otra opción.")

    # Guardar datos después de asignar rutas
    guardar_json(lista_estudiantes)
    guardarCapacidad(capacidad_actual)

# Llamar a la función rutaestudio para ejecutar el código
rutaestudio()




#def rutaestudio():
#    global lista_estudiantes
#    global capacidad_actual
#
#    for estudiante in lista_estudiantes:
#        print("\nCapacidad Actual:")
#        for ruta, capacidad in capacidad_actual.items():
#            print(f"{ruta}: {capacidad} estudiantes")
#
#        if estudiante["estado"].lower() == "aprobado":
#            print("{} Usted puede elegir la ruta de entrenamiento".format(estudiante["nombre"]))
#
#            salir = False
#            while not salir:
#                print("\n1. Clases de Ruta NodeJS."
#                      "\n2. Clases de Ruta Java."
#                      "\n3. Clases de Ruta NetCore."
#                      "\n4. Elegir mi ruta más tarde.")
#
#                opcion_ruta = int(input("Seleccione la ruta (1-4): "))
#
#                if opcion_ruta == 1:
#                    print("\nClases de Ruta NodeJS:"
#                          "\n1. Con el Docente: Naruto, Salon 1, de 06:00 AM a 10:00 AM."
#                          "\n2. Con el Docente: Naruto, Salon 1, de 10:00 AM a 12:00 PM."
#                          "\n3. Con el Docente: Itachi, Salon 1, de 12:00 PM a 04:00 PM."
#                          "\n4. Con el Docente: Itachi, Salon 1, de 04:00 PM a 06:00 PM."
#                          "\n5. Con la Docente: Sakura, Salon 1, de 06:00 PM a 10:00 PM."
#                          "\n6. Elegir mi horario luego.")
#
#                    opcion_horario = int(input("Seleccione una opción (1-6): "))
#                    if 1 <= opcion_horario <= 5:
#                        estudiante["ruta"] = "Ruta NodeJS"
#                        estudiante["estado"] = "asignado"
#                        estudiante["docente"] = "Naruto" if opcion_horario in [1, 2] else "Itachi" if opcion_horario in [3, 4] else "Sakura"
#                        estudiante["aula"] = "Salon 1"
#                        estudiante["horario"] = [
#                            "6:00 AM - 10:00 AM",
#                            "10:00 AM - 12:00 PM",
#                            "12:00 PM - 04:00 PM",
#                            "04:00 PM - 06:00 PM",
#                            "06:00 PM - 10:00 PM"
#                        ][opcion_horario - 1]
#                        if estudiante["cod"].count("n11") < 33:
#                            estudiante["cod"].append("n11")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("n12") < 33:
#                            estudiante["cod"].append("n12")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("i13") < 33:
#                            estudiante["cod"].append("i13")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("i14") < 33:
#                            estudiante["cod"].append("i14")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("s15") < 33:
#                            estudiante["cod"].append("s15")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#
#                        estudiante["cod"] = [
#                            "n11",
#                            "n12",
#                            "i13",
#                            "i14",
#                            "s15"
#                        ][opcion_horario - 1]
#                        
#                        salir = True
#                    elif opcion_horario == 6:
#                        print("Aún no has elegido tu horario.")
#                        salir = True
#                    else:
#                        print("Opción no válida. Inténtalo de nuevo.")
#                    # Verificar si hay más de 33 por aula
#                    ruta_actual = estudiante["ruta"] + " - " + estudiante["aula"]
#                    if capacidad_actual[ruta_actual] < 33:
#                        capacidad_actual[ruta_actual] += 1
#                        salir = True
#                    else:
#                        print("La capacidad máxima de estudiantes en esta ruta y aula se ha alcanzado. Elija otra opción.")
#
#                elif opcion_ruta == 2:
#                    print("\nClases de Ruta Java:"
#                          "\n1. Con el Docente: Luffy, Salon 2, de 06:00 AM a 10:00 AM."
#                          "\n2. Con el Docente: Luffy, Salon 2, de 10:00 AM a 12:00 PM."
#                          "\n3. Con el Docente: Zoro, Salon 2, de 12:00 PM a 04:00 PM."
#                          "\n4. Con el Docente: Zoro, Salon 2, de 04:00 PM a 06:00 PM."
#                          "\n5. Con el Docente: Chopper, Salon 2, de 06:00 PM a 10:00 PM."
#                          "\n6. Elegir mi horario luego.")
#
#                    opcion_horario = int(input("Seleccione una opción (1-6): "))
#                    if 1 <= opcion_horario <= 5:
#                        estudiante["ruta"] = "Ruta Java"
#                        estudiante["estado"] = "asignado"
#                        estudiante["docente"] = "Luffy" if opcion_horario in [1, 2] else "Zoro" if opcion_horario in [3, 4] else "Chopper"
#                        estudiante["aula"] = "Salon 2"
#                        estudiante["horario"] = [
#                            "6:00 AM - 10:00 AM",
#                            "10:00 AM - 12:00 PM",
#                            "12:00 PM - 04:00 PM",
#                            "04:00 PM - 06:00 PM",
#                            "06:00 PM - 10:00 PM"
#                        ][opcion_horario - 1]
#                        if estudiante["cod"].count("l21") < 33:
#                            estudiante["cod"].append("l21")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("l22") < 33:
#                            estudiante["cod"].append("l22")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("z23") < 33:
#                            estudiante["cod"].append("z23")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("z24") < 33:
#                            estudiante["cod"].append("z24")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("c25") < 33:
#                            estudiante["cod"].append("c25")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        estudiante["cod"] = [
#                            "l21",
#                            "l22",
#                            "z23",
#                            "z24",
#                            "c25"
#                        ][opcion_horario - 1]
#                        salir = True
#                    elif opcion_horario == 6:
#                        print("Aún no has elegido tu horario.")
#                        salir = True
#                    else:
#                        print("Opción no válida. Inténtalo de nuevo.")
#                    # Verificar si hay más de 33 por aula
#                    ruta_actual = estudiante["ruta"] + " - " + estudiante["aula"]
#                    if capacidad_actual[ruta_actual] < 33:
#                        capacidad_actual[ruta_actual] += 1
#                        salir = True
#                    else:
#                        print("La capacidad máxima de estudiantes en esta ruta y aula se ha alcanzado. Elija otra opción.")
#
#                elif opcion_ruta == 3:
#                    print("\nClases de Ruta NetCore:"
#                          "\n1. Con el Docente: Edward, Salon 3, de 06:00 AM a 10:00 AM."
#                          "\n2. Con el Docente: Edward, Salon 3, de 10:00 AM a 12:00 PM."
#                          "\n3. Con el Docente: Alphonse, Salon 3, de 12:00 PM a 04:00 PM."
#                          "\n4. Con el Docente: Alphonse, Salon 3, de 04:00 PM a 06:00 PM."
#                          "\n5. Con el Docente: Roy, Salon 3, de 06:00 PM a 10:00 PM."
#                          "\n6. Elegir mi horario luego.")
#
#                    opcion_horario = int(input("Seleccione una opción (1-6): "))
#                    if 1 <= opcion_horario <= 5:
#                        estudiante["ruta"] = "Ruta NetCore"
#                        estudiante["estado"] = "asignado"
#                        estudiante["docente"] = "Edward" if opcion_horario in [1, 2] else "Alphonse" if opcion_horario in [3, 4] else "Roy"
#                        estudiante["aula"] = "Salon 3"
#                        estudiante["horario"] = [
#                            "6:00 AM - 10:00 AM",
#                            "10:00 AM - 12:00 PM",
#                            "12:00 PM - 04:00 PM",
#                            "04:00 PM - 06:00 PM",
#                            "06:00 PM - 10:00 PM"
#                        ][opcion_horario - 1]
#                        if estudiante["cod"].count("e31") < 33:
#                            estudiante["cod"].append("e31")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("e32") < 33:
#                            estudiante["cod"].append("e32")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("a33") < 33:
#                            estudiante["cod"].append("a33")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("a34") < 33:
#                            estudiante["cod"].append("a34")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        if estudiante["cod"].count("r35") < 33:
#                            estudiante["cod"].append("r35")
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes con código 'e31' se ha alcanzado. Elija otra opción.")
#                        estudiante["cod"] = [
#                            "e31",
#                            "e32",
#                            "a33",
#                            "a34",
#                            "r35"
#                        ][opcion_horario - 1]
#                        salir = True
#                    elif opcion_horario == 6:
#                        print("Aún no has elegido tu horario.")
#                        salir = True
#                    else:
#                        print("Opción no válida. Inténtalo de nuevo.")
#                    # Verificar si hay más de 33 por aula
#                    ruta_actual = estudiante["ruta"] + " - " + estudiante["aula"]
#                    if capacidad_actual[ruta_actual] < 33:
#                        capacidad_actual[ruta_actual] += 1
#                        salir = True
#                    else:
#                        print("La capacidad máxima de estudiantes en esta ruta y aula se ha alcanzado. Elija otra opción.")
#
#                elif opcion_ruta == 4:
#                        print("\nElegir mi ruta más tarde.")
#                        salir = True
#
#                else:
#                        print("Opción no válida. Inténtalo de nuevo.")
#                        # Verificar si hay más de 33 por aula
#                        ruta_actual = estudiante["ruta"] + " - " + estudiante["aula"]
#                        if capacidad_actual[ruta_actual] < 33:
#                            capacidad_actual[ruta_actual] += 1
#                            salir = True
#                        else:
#                            print("La capacidad máxima de estudiantes en esta ruta y aula se ha alcanzado. Elija otra opción.")
#
#
#    guardar_json(lista_estudiantes)
#
## Llamar a la función rutaestudio para ejecutar el código
#rutaestudio()
#guardarCapacidad(capacidad_actual)
#
#
#
#
#
#


#import json
#
#capacidad_actual = {
#    "Ruta NodeJS - Salon 1": 0,
#    "Ruta Java - Salon 2": 0,
#    "Ruta NetCore - Salon 3": 0
#}
#
#def rutaestudio():
#    global lista_estudiantes
#    global capacidad_actual
#
#def cargarEstudiantes():
#    estudiantes=[]
#
#    try:
#        with open("estudiantes.json") as file:
#            estudiantes = json.load(file)
#
#        if estudiantes is not None:
#            salir = False
#            while not salir:
#                  
#
#                ask=int(input("\n1.Desea ver informacion basica de los estudiantes. "
#                            "\n2.Saber el estado y en que ruta de estudio esta. "
#                            "\n3.Conocer horario de estudio. "
#                            "\n4.Ver menu completo. "))
#
#                match ask:
#                
#                    case 1:
#                    
#                        for estudiante in estudiantes:
#                            print("Nombre:", estudiante["nombre"], "Edad:", estudiante["edad"], "Celular:", estudiante["telefono Celular"])
#                        return estudiantes
#
#                    case 2:
#                    
#                        for estudiante in estudiantes:
#                            print("Nombre:", estudiante["nombre"], "Estado:", estudiante["estado"], "Ruta:", estudiante["ruta"])
#                        return estudiantes
#
#                    case 3:
#                    
#                        for estudiante in estudiantes:
#                            print("Nombre:", estudiante["nombre"])
#                        return estudiantes
#
#                    case 4: 
#                    
#                        print("Regresando al menu anterior. ")
#                        salir = True
#
#
#            return estudiantes
#        else:
#            print("El archivo 'estudiantes.json' está vacío o tiene un formato incorrecto.")
#            return []
#
#    except FileNotFoundError:
#        print("El archivo 'estudiantes.json' no existe. Puede que aún no haya estudiantes guardados.")
#        return []
#    except json.JSONDecodeError:
#        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
#        return []
#    except Exception as e:
#        print("Error desconocido:", e)
#        return []
#                              
#
#
#lista_estudiantes= cargarEstudiantes()
#
#
#def guardar_json(lista_estudiantes):
#    try:
#        with open("estudiantes.json", 'w') as archivo_json:
#            json.dump(lista_estudiantes, archivo_json, indent=2)
#            print("La lista de estudiantes ha sido guardada")
#    except FileNotFoundError:
#        print("El archivo no existe. Puede que aún no haya estudiantes guardados.")
#    except json.JSONDecodeError:
#        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
#    except Exception as e:
#        print("Error desconocido:", e)
#
#
#def crearNuevoEstudiante():
#    global lista_estudiantes
#
#
#    nuevoEstudiante = {}
#
#    nuevoEstudiante["nombre"] = input("Ingrese el nombre del estudiante: ")
#    nuevoEstudiante["edad"] = int(input("Ingrese la edad del estudiante: "))
#    nuevoEstudiante["telefono Celular"] = int(input("Ingrese el número de celular: "))
#    nuevoEstudiante["acudiente"] = (input("nombre y numero de contacto"))
#    nuevoEstudiante["No Identificacion"] = int(input("Ingrese el número de documento: "))
#    nuevoEstudiante["direccion"] = (input("Ingrese la direccion"))
#    nuevoEstudiante["estado"] = "inscrito"
#    nuevoEstudiante["ruta"] = "Sin asignar"
#    nuevoEstudiante["docente"] = "Sin asignar"
#    nuevoEstudiante["aula"] = "Sin asignar"
#    nuevoEstudiante["horario"] = "Sin asignar"
#
#    
#    lista_estudiantes.append(nuevoEstudiante)
#    
#    guardar_json(lista_estudiantes)
#       
#
#    
#
#
#def registroPrueba():
#    global lista_estudiantes
#
#
#    for estudiante in lista_estudiantes:
#
#        if estudiante["estado"].lower() == "inscrito":
#
#            print("{} Usted puede presentar la prueba ya que su estado es {}".format(estudiante["nombre"], estudiante["estado"]))
#
#            notaTeorica = int(input("Cuál es el resultado de su nota teorica: "))
#            notaPractica = int(input("Cuál es el resultado de su nota practica: "))
#
#            promedio = (notaPractica + notaTeorica) / 2
#
#            if promedio >= 60:
#
#                estudiante["estado"] = "Aprobado"
#
#                print("Usted logró superar el promedio de la prueba con un {}".format(promedio))
#
#            else:
#
#                estudiante["estado"] = "Reprobado"
#
#                print("Usted no logró superar el promedio su nota fue {} ".format(promedio))
#
#        else:
#            print("{} no puedes presentar la prueba porque su estado es {}".format(estudiante["nombre"], estudiante["estado"]))
#
#    
#    guardar_json(lista_estudiantes)
#
#
#
#def rutaestudio():
#    global lista_estudiantes
#
#
#    for estudiante in lista_estudiantes:
#
#        print("\nCapacidad Actual:")
#        for ruta, capacidad in capacidad_actual.items():
#            print(f"{ruta}: {capacidad} estudiantes")
#
#
#        if estudiante["estado"].lower() == "aprobado":
#            print("{} Usted puede elegir la ruta de entrenamiento".format(estudiante["nombre"]))
#
#            salir = False
#
#            while not salir:
#                print("\n1. Clases de Ruta NodeJS."
#                      "\n2. Clases de Ruta Java."
#                      "\n3. Clases de Ruta NetCore."
#                      "\n4. Elegir mi ruta más tarde.")
#
#                opcion_ruta = int(input("Seleccione la ruta (1-4): "))
#
#                if opcion_ruta == 1:
#                    print("\nClases de Ruta NodeJS:"
#                          "\n1. Con el Docente: Naruto, Salon 1, de 06:00 AM a 10:00 AM."
#                          "\n2. Con el Docente: Naruto, Salon 1, de 10:00 AM a 12:00 PM."
#                          "\n3. Con el Docente: Itachi, Salon 1, de 12:00 PM a 04:00 PM."
#                          "\n4. Con el Docente: Itachi, Salon 1, de 04:00 PM a 06:00 PM."
#                          "\n5. Con la Docente: Sakura, Salon 1, de 06:00 PM a 10:00 PM."
#                          "\n6. Elegir mi horario luego.")
#
#                    opcion_horario = int(input("Seleccione una opción (1-6): "))
#                    if 1 <= opcion_horario <= 5:
#                        estudiante["ruta"] = "Ruta NodeJS"
#                        estudiante["estado"] = "asignado"
#                        estudiante["docente"] = "Naruto" if opcion_horario in [1, 2] else "Itachi" if opcion_horario in [3, 4] else "Sakura"
#                        estudiante["aula"] = "Salon 1"
#                        estudiante["horario"] = [
#                            "6:00 AM - 10:00 AM",
#                            "10:00 AM - 12:00 PM",
#                            "12:00 PM - 04:00 PM",
#                            "04:00 PM - 06:00 PM",
#                            "06:00 PM - 10:00 PM"
#                        ][opcion_horario - 1]
#                        salir = True
#                    elif opcion_horario == 6:
#                        print("Aún no has elegido tu horario.")
#                        salir = True
#                    else:
#                        print("Opción no válida. Inténtalo de nuevo.")
#                    #Verificar si hay mas 33 por aula
#                    ruta_actual = estudiante["ruta"] + " - " + estudiante["aula"]
#                    if capacidad_actual[ruta_actual] < 33:
#                        capacidad_actual[ruta_actual] += 1
#                        salir = True
#
#                    else:
#                        print("La capacidad máxima de estudiantes en esta ruta y aula se ha alcanzado. Elija otra opción.")
#
#                elif opcion_ruta == 2:
#                    print("\nClases de Ruta Java:"
#                          "\n1. Con el Docente: Luffy, Salon 2, de 06:00 AM a 10:00 AM."
#                          "\n2. Con el Docente: Luffy, Salon 2, de 10:00 AM a 12:00 PM."
#                          "\n3. Con el Docente: Zoro, Salon 2, de 12:00 PM a 04:00 PM."
#                          "\n4. Con el Docente: Zoro, Salon 2, de 04:00 PM a 06:00 PM."
#                          "\n5. Con el Docente: Chopper, Salon 2, de 06:00 PM a 10:00 PM."
#                          "\n6. Elegir mi horario luego.")
#
#                    opcion_horario = int(input("Seleccione una opción (1-6): "))
#                    if 1 <= opcion_horario <= 5:
#                        estudiante["ruta"] = "Ruta Java"
#                        estudiante["estado"] = "asignado"
#                        estudiante["docente"] = "Luffy" if opcion_horario in [1, 2] else "Zoro" if opcion_horario in [3, 4] else "Chopper"
#                        estudiante["aula"] = "Salon 2"
#                        estudiante["horario"] = [
#                            "6:00 AM - 10:00 AM",
#                            "10:00 AM - 12:00 PM",
#                            "12:00 PM - 04:00 PM",
#                            "04:00 PM - 06:00 PM",
#                            "06:00 PM - 10:00 PM"
#                        ][opcion_horario - 1]
#                        salir = True
#                    elif opcion_horario == 6:
#                        print("Aún no has elegido tu horario.")
#                        salir = True
#                    else:
#                        print("Opción no válida. Inténtalo de nuevo.")
#
#                    #Verificar si hay mas 33 por aula
#                    ruta_actual = estudiante["ruta"] + " - " + estudiante["aula"]
#                    if capacidad_actual[ruta_actual] < 33:
#                        capacidad_actual[ruta_actual] += 1
#                        salir = True
#                    else:
#                        print("La capacidad máxima de estudiantes en esta ruta y aula se ha alcanzado. Elija otra opción.")
#
#
#
#                elif opcion_ruta == 3:
#                    print("\nClases de Ruta NetCore:"
#                          "\n1. Con el Docente: Edward, Salon 3, de 06:00 AM a 10:00 AM."
#                          "\n2. Con el Docente: Edward, Salon 3, de 10:00 AM a 12:00 PM."
#                          "\n3. Con el Docente: Alphonse, Salon 3, de 12:00 PM a 04:00 PM."
#                          "\n4. Con el Docente: Alphonse, Salon 3, de 04:00 PM a 06:00 PM."
#                          "\n5. Con el Docente: Roy, Salon 3, de 06:00 PM a 10:00 PM."
#                          "\n6. Elegir mi horario luego.")
#
#                    opcion_horario = int(input("Seleccione una opción (1-6): "))
#                    if 1 <= opcion_horario <= 5:
#                        estudiante["ruta"] = "Ruta NetCore"
#                        estudiante["estado"] = "asignado"
#                        estudiante["docente"] = "Edward" if opcion_horario in [1, 2] else "Alphonse" if opcion_horario in [3, 4] else "Roy"
#                        estudiante["aula"] = "Salon 3"
#                        estudiante["horario"] = [
#                            "6:00 AM - 10:00 AM",
#                            "10:00 AM - 12:00 PM",
#                            "12:00 PM - 04:00 PM",
#                            "04:00 PM - 06:00 PM",
#                            "06:00 PM - 10:00 PM"
#                        ][opcion_horario - 1]
#                        salir = True
#                    elif opcion_horario == 6:
#                        print("Aún no has elegido tu horario.")
#                        salir = True
#                    else:
#                        print("Opción no válida. Inténtalo de nuevo.")
#
#                elif opcion_ruta == 4:
#                    print("\nElegir mi ruta mas tarde.")
#                    salir = True
#
#                else:
#                    print("Opción no válida. Inténtalo de nuevo.")
#                    #Verificar si hay mas 33 por aula
#                    ruta_actual = estudiante["ruta"] + " - " + estudiante["aula"]
#                    if capacidad_actual[ruta_actual] < 33:
#                        capacidad_actual[ruta_actual] += 1
#                        salir = True
#                    else:
#                        print("La capacidad máxima de estudiantes en esta ruta y aula se ha alcanzado. Elija otra opción.")
#
#    guardar_json(lista_estudiantes)
#
## Llamar a la función rutaestudio para ejecutar el código
#rutaestudio()
#
#
#
##def rutaestudio():
##    global lista_estudiantes
##
##
##    for estudiante in lista_estudiantes:
##        if estudiante["estado"].lower() == "aprobado":
#            print("{} Usted puede elegir la ruta de entrenamiento".format(estudiante["nombre"]))
#
#            salir = False
#
#            while not salir:
#                n = int(input("\n1.Horarios Ruta NodeJS."
#                              "\n2.Horarios Ruta Java."
#                              "\n3.Horarios Ruta NetCore"
#                              "\n4.Elegire mi ruta mas tarde."))
#                match n:
#                    case 1:
#                        x=int(input("\n--------Ruta NodeJS---------"
#                        "\nCon el Docente: Naruto, Salon 1"
#                        "\nOpcion 1: 06:00 AM - 10:00 PM "
#                        "\nOpcion 2: 10:00 AM - 12:00 PM"
#                        "\nCon el Docente: Itachi. Salon 1"
#                        "\nOpcion 3: 12:00 PM - 04:00 PM"
#                        "\nOpcion 4: 04:00 PM - 06:00 PM"
#                        "\nCon la Docente Sakura, Salon 1"
#                        "\nOpcion 5: 06:00 PM - 10:00 PM"
#                        "\nOpcion 6 Elegir mi horario luego. "))
#
#                        match x:
#                            case 1:
#
#                                estudiante["ruta"] = "Ruta NodeJS "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Naruto"
#                                estudiante["aula"] = "Salon 1"
#                                estudiante["horario"] = "6:00 AM - 10:00 AM"
#                                salir = True  
#
#                            case 2:
#                                estudiante["ruta"] = "Ruta NodeJS "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Naruto"
#                                estudiante["aula"] = "Salon 1"
#                                estudiante["horario"] = "10:00 AM - 12:00 PM"
#                                salir = True  
#
#                            case 3:
#                                estudiante["ruta"] = "Ruta NodeJS "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Itachi"
#                                estudiante["aula"] = "Salon 1"
#                                estudiante["horario"] = "12:00 PM - 04:00 PM"
#                                salir = True  
#
#                            case 4:
#                                estudiante["ruta"] = "Ruta NodeJS "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Itachi"
#                                estudiante["aula"] = "Salon 1"
#                                estudiante["horario"] = "04:00 PM - 06:00 PM"
#                                salir = True  
#
#                            case 5:
#                                estudiante["ruta"] = "Ruta NodeJS "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Sakura"
#                                estudiante["aula"] = "Salon 1"
#                                estudiante["horario"] = "06:00 PM - 10:00 PM"
#                                salir = True
#                            case 6:
#                                print("Aun no elijes tu horario.")
#                                salir = True
#                        salir = True 
#
#                    case 2:
#                        x=int(input("\n--------Ruta Java---------"
#                        "\nCon el Docente: Luffy, Salon 2"
#                        "\nOpcion 1: 06:00 AM - 10:00 PM "
#                        "\nOpcion 2: 10:00 AM - 12:00 PM"
#                        "\nCon el Docente: Zoro. Salon 2"
#                        "\nOpcion 3: 12:00 PM - 04:00 PM"
#                        "\nOpcion 4: 04:00 PM - 06:00 PM"
#                        "\nCon el Docente Chopper, Salon 2"
#                        "\nOpcion 5: 06:00 PM - 10:00 PM"
#                        "\nOpcion 6 Elegir mi horario luego. "))
#
#                        match x:
#
#                            case 1:
#
#                                estudiante["ruta"] = "Ruta Java "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Luffy"
#                                estudiante["aula"] = "Salon 2"
#                                estudiante["horario"] = "6:00 AM - 10:00 AM"
#                                salir = True  
#
#                            case 2:
#                                estudiante["ruta"] = "Ruta Java "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Luffy"
#                                estudiante["aula"] = "Salon 2"
#                                estudiante["horario"] = "10:00 AM - 12:00 PM"
#                                salir = True  
#
#                            case 3:
#                                estudiante["ruta"] = "Ruta Java "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Zoro"
#                                estudiante["aula"] = "Salon 2"
#                                estudiante["horario"] = "12:00 PM - 04:00 PM"
#                                salir = True  
#
#                            case 4:
#                                estudiante["ruta"] = "Ruta Java "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Zoro"
#                                estudiante["aula"] = "Salon 2"
#                                estudiante["horario"] = "04:00 PM - 06:00 PM"
#                                salir = True  
#
#                            case 5:
#                                estudiante["ruta"] = "Ruta Java "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Chopper"
#                                estudiante["aula"] = "Salon 2"
#                                estudiante["horario"] = "06:00 PM - 10:00 PM"
#                                salir = True
#                            case 6:
#                                print("Aun no elijes tu horario.")
#                                salir = True
#                        salir = True 
#
#
#                    case 3:
#                        x=int(input("\n--------Ruta NetCore---------"
#                        "\nCon el Docente: Edward, Salon 3"
#                        "\nOpcion 1: 06:00 AM - 10:00 PM "
#                        "\nOpcion 2: 10:00 AM - 12:00 PM"
#                        "\nCon el Docente: Alphonse. Salon 3"
#                        "\nOpcion 3: 12:00 PM - 04:00 PM"
#                        "\nOpcion 4: 04:00 PM - 06:00 PM"
#                        "\nCon el Docente Roy, Salon 3"
#                        "\nOpcion 5: 06:00 PM - 10:00 PM"
#                        "\nOpcion 6 Elegir mi horario luego. "))
#
#                        match x:
#                            case 1:
#
#                                estudiante["ruta"] = "Ruta NetCore "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Edward"
#                                estudiante["aula"] = "Salon 3"
#                                estudiante["horario"] = "6:00 AM - 10:00 AM"
#                                salir = True  
#
#                            case 2:
#                                estudiante["ruta"] = "Ruta NetCore "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Edward"
#                                estudiante["aula"] = "Salon 3"
#                                estudiante["horario"] = "10:00 AM - 12:00 PM"
#                                salir = True  
#
#                            case 3:
#                                estudiante["ruta"] = "Ruta NetCore "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Alphonse"
#                                estudiante["aula"] = "Salon 3"
#                                estudiante["horario"] = "12:00 PM - 04:00 PM"
#                                salir = True  
#
#                            case 4:
#                                estudiante["ruta"] = "Ruta NetCore "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Alphonse"
#                                estudiante["aula"] = "Salon 3"
#                                estudiante["horario"] = "04:00 PM - 06:00 PM"
#                                salir = True  
#
#                            case 5:
#                                estudiante["ruta"] = "Ruta NetCore "
#                                estudiante["estado"] = "asignado"
#                                estudiante["docente"] = "Roy"
#                                estudiante["aula"] = "Salon 3"
#                                estudiante["horario"] = "06:00 PM - 10:00 PM"
#                                salir = True
#                            case 6:
#                                print("Aun no elijes tu horario.")
#                                salir = True
#                        salir = True 
#                    case 4:
#                        print("\nElegire mi ruta mas tarde. ")
#                        salir = True  
#
#    guardar_json(lista_estudiantes)  
#
##def horarios():
##    global lista_estudiantes
#
#    print("\n--------Ruta NodeJS---------"
#          "\nCon el Docente: Naruto."
#        "\nOpcion 1: 06:00 AM - 10:00 PM "
#        "\nOpcion 2: 10:00 AM - 12:00 PM"
#        "\nCon el Docente: Itachi."
#        "\nOpcion 3: 12:00 PM - 04:00 PM"
#        "\nOpcion 4: 04:00 PM - 06:00 PM"
#        "\nCon la Docente Sakura."
#        "\nOpcion 5: 06:00 PM - 10:00 PM")
    



                    
                
                
                
                            
                
                

    