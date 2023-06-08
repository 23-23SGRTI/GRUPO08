import string
import time
import metodos
import time
opcion = 0

archivo = "archivo.txt"
while opcion !=6:
    print("\nSelecciona una Opcion")
    print("1.Leer Archivo\n2.Agregar Texto al Archivo\n3.Encriptar\n4.Desencriptar\n5.Vaciar Txt\n6.salir")
    opcion = int(input("Ingresa Una Opcion: ")) 

    if opcion == 1:
        inicio = time.time()
        print("El Contenido del Archivo es:")
        metodos.LeerArchivo(archivo) 
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")     
    elif opcion == 2:
         #linea = input("Ingrese el Texto que desea agrgar al Archivo: ")
         #metodos.escribirArchivo(linea, archivo)
         numero = int(input("Ingrese el numero de palabras que desea agregar al Archivo: "))
         inicio = time.time()
         metodos.rellenarArchivo(archivo, numero)
         fin = time.time()
         tiempo_ejecucion = fin - inicio
         print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

    elif opcion == 3:
        inicio = time.time()
        metodos.encriptar(archivo,3)
        print("¡¡¡ Archivo Encriptado Correctamente!!!")

        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

    elif opcion ==4:
        inicio = time.time()
        metodos.desencriptar(archivo,3)
        print("¡¡¡ Proceso de Desencriptacion exitoso !!!")
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

    elif opcion ==5:
        metodos.borrar_contenido_archivo(archivo)
        print("¡¡¡ Archivo vaciado con exito !!!")

    else:  
        print("\n¡¡¡ Usted salio de la app¡¡¡")