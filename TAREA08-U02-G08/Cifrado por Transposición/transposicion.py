import string
import time
import metodos

archivo = "archivo.txt"
opcion = 0

while opcion != 6:
    print("\nSelecciona una Opcion")
    print("1. Leer Archivo")
    print("2. Agregar Texto al Archivo")
    print("3. Encriptar")
    print("4. Desencriptar")
    print("5. Vaciar Txt")
    print("6. Salir")
    opcion = int(input("Ingresa una Opcion: "))

    if opcion == 1:
        inicio = time.time()
        print("El Contenido del Archivo es:")
        metodos.LeerArchivo(archivo) 
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

    elif opcion == 2:
        numero = int(input("Ingrese el número de palabras que desea agregar al archivo: "))
        inicio = time.time()
        metodos.rellenarArchivo(archivo, numero)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

    elif opcion == 3:
        #key = 'KEY'
        key = int(input("Introducir Key [2-%s]: " % (len(archivo) - 1)))
        inicio = time.time()
        metodos.encriptar_transposicion(archivo, key)
        print("¡¡¡ Archivo Encriptado Correctamente!!!")
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

    elif opcion == 4:
        inicio = time.time()
        key = int(input("Ingresa la clave (key) [2-%s]: " % (len(archivo) - 1)))
        # metodos.desencriptar_transposicion(key, archivo)  # Intercambia el orden de los argumentos
        metodos.desencriptar_transposicion(key, archivo)
        print("¡Proceso de Desencriptación exitoso!")
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")


    elif opcion == 5:
        metodos.borrar_contenido_archivo(archivo)
        print("¡Archivo vaciado con éxito!")

    else:
        print("\n¡Usted salió de la app!")

