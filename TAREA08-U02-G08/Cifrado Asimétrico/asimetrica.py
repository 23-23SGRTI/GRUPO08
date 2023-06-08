#GENERAR UNA CLAVE PÚBLICA Y PRIVADA

import time
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import metodos

#UTILIZAR LIBRERÍA PYCRIPTODOME
def generar_claves():

    key = RSA.generate(2048)

    private_key = key.export_key() #FUNCION PARA CREAR LA CLAVE PRIVADA
    #CREACION DEL ARCHIVO
    file_out = open("private.pem", "wb") #PRIVATE.PEM ES ARCHIVO DE CLAVE PRIVADA

    file_out.write(private_key)

    file_out.close()
    public_key = key.publickey().export_key()   #FUNCION PARA CREAR LA CLAVE PUBLICA

    file_out = open("receiver.pem", "wb")       #RECEIVER.PEM ES EL NOMBRE DEL ARCHIVO DE CLAVE PUBLICA

    file_out.write(public_key)                  #SE ESCRIBE LA CLAVE PUBLICA EN EL ARCHIVO

    file_out.close()

#ENCRIPTACIÓN

def encriptar():
    data = open("archivo.txt", "rb").read()#LECTURA DEL ARCHIVO texto.txt

    file_out = open("encrypted_data.txt", "wb")

    recipient_key = RSA.import_key(open("receiver.pem").read()) #LECTURA DE LA CLAVE DEL ARCHIVO RECEIVER PEM PONIENDOLO EN LA CLAVE DE RECIPIENTE

    session_key = get_random_bytes(16)                          #SESSION KEY DE RANDOM BYTE

    # ENCRIPTACION DE LA SESION CON LA CLAVE PUBLICA
    cipher_rsa = PKCS1_OAEP.new(recipient_key)

    enc_session_key = cipher_rsa.encrypt(session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)

    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()


def desencriptar():
    file_in = open("encrypted_data.txt", "rb")
    print(file_in)
    private_key = RSA.import_key(open("private.pem").read())
    enc_session_key, nonce, tag, ciphertext = \
   [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
    # Descencriptamos la sesion con nuestra clave privada (RSA)
    cipher_rsa = PKCS1_OAEP.new(private_key)    
    session_key = cipher_rsa.decrypt(enc_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    print(data.decode("utf-8"))

opcion = 0
archivo = "archivo.txt"
while opcion !=7:
    print("\nSelecciona una Opcion")
    print("1.crear claves \n2 Leer el archivo\n3.Agregar Texto al Archivo\n4.Encriptar\n5.Desencriptar\n6.Vaciar Txt\n7.salir")
    opcion = int(input("Ingresa Una Opcion: "))

 

    if opcion == 1:
        inicio = time.time()
        print("Las claves han sido generadas con exito:")
        generar_claves()
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")     
    elif opcion == 2:
         inicio = time.time()
         print("El Contenido del Archivo es:")
         metodos.LeerArchivo(archivo) 
         fin = time.time()
         tiempo_ejecucion = fin - inicio
         print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")
         
    elif opcion == 3:
         
         numero = int(input("Ingrese el numero de palabras que desea agregar al Archivo: "))
         
         metodos.rellenarArchivo(archivo, numero)
 

    elif opcion ==4:
        inicio = time.time()
        encriptar()
        print("¡¡¡ Archivo Encriptado Correctamente!!!")
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

 

    elif opcion ==5:
        inicio = time.time()
        desencriptar()
        print("¡¡¡ Proceso de Desencriptacion exitoso !!!")
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

    elif opcion ==6:
        metodos.borrar_contenido_archivo(archivo)
        print("¡¡¡ Archivo vaciado con exito !!!")

    else:  
        print("\n¡¡¡ Usted salio de la app¡¡¡")