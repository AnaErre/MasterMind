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



def exact_numbers (secret_num, player_num):
    black_counter = 0 
    exact_aux = []   
    for i in range(len(secret_num)):
        if (secret_num[i]  == player_num[i]) & (player_num[i] != exact_aux[i]):
            black_counter = black_counter + 1
            exact_aux.insert(i, player_num[i])
    return(black_counter)
        

def present_numbers (secret_num, player_num):
    white_counter = 0
    present_aux = []
    for i in range(len(secret_num)):
        for j in range(len(player_num)):
            if (secret_num[i] == player_num[j]) & (i != j):
                white_counter = white_counter + 1
                break  
    return(white_counter)

print("Negras:", exact_numbers(secret_number, player_number))
#print("Blancas:", present_numbers(secret_number, player_number))


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


#print(combined(secret_number, player_number))
