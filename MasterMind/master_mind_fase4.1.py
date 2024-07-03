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

def is_not_finished(round, final, player_num, secret_num):
    return (round < final) & (player_num != secret_num)

def finished(player_num, secret_num):
    if player_num == secret_num:
        print("Correcto! Has ganado :)")
    else: 
        print("Has perdido :(") 


def exact_numbers (secret_num, player_num):
    black_counter = 0    
    for i, secret_num[i] in enumerate(secret_num):
        if secret_num[i]  == player_num[i]:
            black_counter = black_counter + 1
    return(black_counter)
        

def present_numbers (secret_num, player_num):
    white_counter = 0
    for i, secret_num[i] in enumerate(secret_num):
        if secret_num[i] in player_num:
            white_counter = white_counter + 1
    return(white_counter)


def main():
    total_tries = 10
    secret_number = shuffle()
    try_counter = 1
    guess_num = 5
    print(f"Los numeros secretos son {secret_number}")
    print(f"Hola! Adivina los {guess_num} numeros (del 1 al 7) [Tienes {total_tries} intentos]")
    player_number = player_turn(try_counter, guess_num)
    while is_not_finished(try_counter, total_tries, secret_number, player_number):
        try_counter = try_counter + 1
        print("Blancas:", present_numbers(secret_number, player_number))
        print("Negras:", exact_numbers(secret_number, player_number))
        player_number = player_turn(try_counter, guess_num)
    finished(secret_number, player_number)
    print(f"El número secreto era: {secret_number}")

main()



