from cryptography.fernet import Fernet
from pathlib import Path
import random
import string
import time
def borrar_contenido_archivo(nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write('')  # Escribe una cadena vacía

def LeerArchivo(archivo):
    stream = open(archivo,"rt",encoding="utf-8")
    print(stream.read())

def escribirArchivo(linea,archivo):
        with open(archivo,"a") as file: #argumento a = append o agregar
            file.write("\n"+linea)
def generar_palabra(longitud):

    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for _ in range(longitud))

def rellenarArchivo(archivo,numero):
    with open(archivo, "a") as file:
        for _ in range(numero):
            palabra = generar_palabra(random.randint(3, 10))  # Longitud de palabra aleatoria entre 3 y 10 caracteres
            file.write(palabra + '\n')
def generar_clave():
    inicio = time.time()
    archivo = r"key.key"
    objetoArchivo = Path(archivo)
    if not objetoArchivo.is_file():
        clave = Fernet.generate_key()
        with open("key.key","wb") as key_file:
            key_file.write(clave)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos") 

def cargar_clave():
    return open("key.key","rb").read()

def encriptar(archivo,clave):
    f = Fernet(clave)
    with open(archivo,"rb") as file:
        file_data = file.read()
#Se encriptan los datos del archivo
    datos_encriptados = f.encrypt(file_data)

    with open(archivo,"wb") as file:
        file.write(datos_encriptados)

def desencriptar(archivo,clave):

    f=Fernet(clave)
    with open(archivo,"rb") as file:
        datos_encriptados = file.read()

    datos = f.decrypt(datos_encriptados)

    with open(archivo,"wb") as file:
        file.write(datos)