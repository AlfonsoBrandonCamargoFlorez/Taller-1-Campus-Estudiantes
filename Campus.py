import json


def menuPrograma():

    pregunta = int(input("1.Si desea cargar la información. \n2.Si desea ingresar un nuevo estudiante \n¿Qué opción desea ingresar?: "))

    match pregunta:

        case 1:

            file = open("Diccionario.json")

            users = json.load(file)

            for user in users:
                print("documento: ", user["documento"], "nombre: ", user["nombre"])


        case 2:
            print("Usted eligió la opción 2")

        case 3:
            print("Hasta luego, que tenga un buen día")
            

menuPrograma()