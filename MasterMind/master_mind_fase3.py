#Juega el PC: Generar un solo numero secreto entre el 1 y el 7
from random import choices

def shuffle():
    sample = range(8)
    return choices(sample,k=5)

def player_turn(x, n):
    print(f"Introduce los numeros [Intento {x}]")
    numbers = range(n)
    player_choice=[]
    for i in numbers:
       N = int(input(f"Numero {i+1}:"))
       player_choice.append(N)
    return player_choice


def main():
    total_tries = 10
    secret_number = shuffle()
    try_counter = 1
    guess_num = 5
    print(f"Los numeros secretos son {secret_number}")
    print(f"Hola! Adivina los {guess_num} numeros (del 1 al 7) [Tienes {total_tries} intentos]")
    player_number = player_turn(try_counter, guess_num)
    while try_counter < total_tries:
        try_counter = try_counter + 1
        if secret_number != player_number:
            print("No es correcto")
            player_number = player_turn(try_counter, guess_num)
        else:
            print("Correcto! has ganado :)")
            break
    else:
        print("Has perdido")


main()







