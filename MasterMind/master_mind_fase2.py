#Juega el PC: Generar un solo numero secreto entre el 1 y el 7
from random import randint

def shuffle():
    return randint(1, 7)

def player_turn(x):
    print(f"Introduce los numeros [Intento {x}]")
    N1 = int(input("Numero 1: "))
    return N1


def main():
    secret_number = shuffle()
    try_counter = 1
    print(f"El numero secreto es {secret_number}")
    print("Hola! Adivina los 5 numeros (del 1 al 7) [Tienes 5 intentos]")
    player_number1 = player_turn(try_counter)
    while try_counter < 5:
        try_counter = try_counter + 1
        if secret_number != player_number1:
            print("No es correcto")
            player_number1 = player_turn(try_counter)
        else:
            print("Correcto! has ganado :)")
            break
    else:
        print("Has perdido")



main()

