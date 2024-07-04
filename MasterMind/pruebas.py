secret_numbers = [8, 2, 3, 5, 6]
candidate_numbers = [8, 2, 3, 5, 6]


def imprimir (secret_numbers):
    for numero in secret_numbers:
       print(numero)
    

def imprimir_pares (secret_numbers):
    for numero in secret_numbers:
        if numero % 2 == 0:
            print(numero)
       


def contador (secret_numbers):
    contador = 0
    for numero in secret_numbers:
       contador = contador + 1
       print(contador)


def contador_pares (secret_numbers):
    contador = 0
    for numero in secret_numbers:
        if numero % 2 == 0:
            contador = contador + 1
    return(contador)

def recorrer (secret_numbers):
    numerador = 0
    for numerador, numero in enumerate(secret_numbers, start = 1):
        print(numerador, numero)


#### PRÁCTICA MASTER-MIND ####


def comparador_exacto (secret_numbers, candidate_numbers):
    contador = 0    
    for indice, secret_numbers[indice] in enumerate(secret_numbers):
        if secret_numbers[indice]  == candidate_numbers[indice]:
            contador = contador + 1
    return(contador)
        

def comparador_presencia (secret_numbers, candidate_numbers):
    contador = 0
    for indice, secret_numbers[indice] in enumerate(secret_numbers):
        if secret_numbers[indice]  in candidate_numbers:
            contador = contador + 1
    return(contador)



def exact_numbers (secret_num, player_num):
    black_counter = 0    
    for i in range(4):
        if secret_num[i]  == player_num[i]:
            black_counter = black_counter + 1
    return(black_counter)
        

def present_numbers (secret_num, player_num):
    white_counter = 0
    for i in range(4):
        for j in range(4):
            if (secret_num[i] == player_num[j]) & (i != j):
                white_counter = white_counter + 1
                break  
    return(white_counter)


secret_number = [2,2,3,1]
player_number = [1,2,4,5]

def combined(secret_num, player_num):
    black = 0
    white = 0
    player_num_copy = player_num.copy()
    for i in range(len(secret_num)):
        for j in range(len(player_num_copy)):
            if (secret_num[i] == player_num[i]):
                black = black + 1
                player_num_copy[i] = None
                break
            elif (secret_num[i] == player_num_copy[j]) & (i!=j):
                white = white + 1
                player_num_copy[j] = None
                break
            print(f"secret_number = {secret_number[i]}, player_number = {player_num_copy[j]}, B={black}, W={white}, {player_num_copy}")
    return (black, white)


test_cases = [
    ([2,2,3,1],
     [1,4,3,6], (1, 1)),  
    ([2,2,3,1], 
     [1,2,4,5], (1, 1)),  
    ([2,2,3,1], 
     [2,3,1,6], (1, 2)),  
    ([2,2,3,1], 
     [2,3,3,2], (2, 1)),  
    ([2,2,3,1],
     [2,4,3,1], (3, 0)),   
    ([2,2,3,1],
     [2,2,3,1], (4, 0)),  
]



#results = [combined(secret, player) == expected for secret, player, expected in test_cases]
#print(results)


print(combined(secret_number, player_number))
#print("Blancas:", present_numbers(secret_number, player_number))


