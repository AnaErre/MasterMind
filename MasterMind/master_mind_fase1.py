#Juega el PC: Generar un solo numero secreto entre el 1 y el 7
from random import randint

secret_number = randint(1, 7)
print(f"el numero secreto ha sido: {secret_number}")


# Interviene player:
print("Hola! Adivina los 5 numeros (del 1 al 7) [Tienes 5 intentos]")
contador_intentos = 1
print(f"Introduce los numeros [Intento {contador_intentos}]")
player_number1 = int(input("Numero 1: "))

while contador_intentos < 5:
    contador_intentos = contador_intentos + 1
    if secret_number != player_number1:
        print("No es correcto")
        print(f"Introduce los numeros [Intento {contador_intentos}]")
        player_number1 = int(input("Numero 1: "))
    else:
        print("Correcto! has ganado :)")
        break
else:
    print("Has perdido")


