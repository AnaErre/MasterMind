# Mastermind
'''
Juego en el que un jugador elige en secreto 5 numeros del 1 al 7, 
y el otro jugador trata de adivinarlos, recibiendo en cada intento información 
sobre como lo ha hecho. El jugador gana si lo adivina antes de 10 intentos.
'''

## El juego:

#Generar un solo numero secreto entre el 1 y el 7
from random import randint
secret_number = randint(1, 7)
print(secret_number)

#Mientras que no se adivine el secreto:
#   Pedir al usuario un nuevo intento
#   Leer el nuevo intento
# Decirle al usuario que ha ganado

player_number = int(input("Escoge un número del 1 al 7: "))

print(f'Tu numero elegido es el {player_number}')


while secret_number != player_number:
    player_number = int(input("No es correcto, elige un nuevo numero: "))
else: 
    print("Correcto! has ganado :)")



