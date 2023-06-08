from pathlib import Path
import random
import string
import math
import time

def borrar_contenido_archivo(nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write('')  # Escribe una cadena vacía

def LeerArchivo(archivo):
    with open(archivo, "r") as file:
        print(file.read())

def escribirArchivo(linea, archivo):
    with open(archivo, "a") as file: 
        file.write(" " + linea)

def generar_palabra(longitud):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for _ in range(longitud))

def rellenarArchivo(archivo, numero):
    with open(archivo, "a") as file:
        for _ in range(numero):
            palabra = generar_palabra(random.randint(3, 10))
            file.write(palabra + " ")

def encriptar_transposicion(archivo, key):
    with open(archivo, 'r') as file:
        file_content = file.read()

    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(file_content):
            ciphertext[col] += file_content[pointer]
            pointer += key

    encrypted_content = ''.join(ciphertext)

    with open(archivo, 'w') as file:
        file.write(encrypted_content)

def desencriptar_transposicion(key, archivo):
    # Lee el contenido del archivo
    with open(archivo, 'r') as file:
        file_content = file.read()

    # Calcula el número de columnas en nuestra tabla
    numOfColumns = math.ceil(len(file_content) / key)
    numOfRows = key
    # Calcula el número de cajas sombreadas en la última columna de nuestra tabla
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(file_content)

    # Cada cadena de texto en plaintext representa una columna dentro de nuestra tabla
    plaintext = [''] * numOfColumns

    # Las variables col y row señalan el punto en la tabla donde irá el próximo carácter del mensaje cifrado
    col = 0
    row = 0

    for symbol in file_content:
        plaintext[col] += symbol
        col += 1

        # Si no hay más columnas o estamos en un lugar sombreado, volver a la primera columna y la siguiente fila
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    # Une el contenido de las columnas en una sola cadena y obtén el mensaje descifrado
    decrypted_content = ''.join(plaintext)

    # Guarda el mensaje descifrado en el archivo
    with open(archivo, 'w') as file:
        file.write(decrypted_content)



