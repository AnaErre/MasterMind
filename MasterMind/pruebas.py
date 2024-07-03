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

secret_numbers = [1, 2, 3, 5, 6]
candidate_numbers = [8, 2, 1, 5, 6]

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



secret_number = [2,3,4,2]
player_number = [1,2,3,3]


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



print("Negras:", exact_numbers(secret_number, player_number))
print("Blancas:", present_numbers(secret_number, player_number))



#for i in range(4):
    #for j in range(4):
        #print(f"secret_number = {secret_number[i]}, player_number = {player_number[j]}")
