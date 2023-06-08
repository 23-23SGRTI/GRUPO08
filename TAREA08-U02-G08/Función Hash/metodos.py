from pathlib import Path
import hashlib
import random
import string

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

#def encriptar(archivo,clave):
def encriptar(archivo):
    # Leer el contenido del archivo
    with open(archivo, 'r') as file:
        file_content = file.read()

    # Calcular el hash del contenido del archivo
    hash_object = hashlib.sha256(file_content.encode())  # Puedes usar otros algoritmos como md5, sha1, etc.
    file_hash = hash_object.hexdigest()

    # Reescribir el archivo con el hash generado
    with open(archivo, 'w') as file:
        file.write(file_hash)
