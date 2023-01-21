# Ejercicio 3
# Escribe un programa en donde pidas por teclado el nombre y el año de nacimiento de la persona y muestre como resultado el siguiente mensaje:
# {nombre} debe cumplir o cumplio {edad} años este año 

nombre = str(input("Por favor, ingresa tu nombre: "))
año_nacimiento = int(input("Ingresa el año en que naciste: "))
if año_nacimiento >= 1923:
    edad = 2023 - año_nacimiento
    print(f"{nombre} debe cumplir o cumplió {edad} años este año.")
else:
    print("año inválido")