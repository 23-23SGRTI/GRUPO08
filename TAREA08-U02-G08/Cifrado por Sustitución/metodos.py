from pathlib import Path
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

def encriptar(archivo, shift):
    with open(archivo, 'r') as file:
        file_content = file.read()

    encrypted_content = ''
    for char in file_content:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_content += encrypted_char
        else:
            encrypted_content += char

    with open(archivo, 'w') as file:
        file.write(encrypted_content)

def desencriptar(archivo, shift):
    with open(archivo, 'r') as file:
        file_content = file.read()

    decrypted_content = ''
    for char in file_content:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_content += decrypted_char
        else:
            decrypted_content += char

    with open(archivo, 'w') as file:
        file.write(decrypted_content)
