#!/usr/bin/python
import random
 
 
#juegos son todos los títulos de juegos que el programa puede usar; los participantes pueden dar sus propias propuestas
games = ["Pokemon(1)", "Fortnite(2)", "Minecraft(3)", "CS(4)"]
#lista_de_juegos_a_adivinar es la variable donde insertamos la contraseña a adivinar
list_of_games_to_guess = []
#lista_de_juegos_ingresados es una lista de juegos ingresados por el usuario
list_of_entered_games = []
###TODO LO DE ARRIBA ES UN PROYECTO INICIAL
 
 
#------- QUÉ ES UNA VARIABLE ---------

#contador de rondas
number_of_attempts = 0 
 

#-----------QUÉ ES UN BUCLE - FOR LOOP--------

#elegimos contraseñas para adivinar

for i in range(4):
 game_drawn = random.choice(games)

 #append significa agregar a la lista

 list_of_games_to_guess.append(game_drawn)
 
#es una buena idea mostrar la contraseña generada para propósitos de prueba en esta etapa
#print(list_of_games_to_guess)
#esta línea debe ser comentada para que el jugador no pueda ver qué juegos han sido elegidos. Mostrar la lista solo es necesario para pruebas
 
#--------- PRUEBA---------------


###INICIAL
#mostramos las instrucciones 
print("Bienvenido al juego MasterMind")
print("Tu objetivo es adivinar los 4 juegos que el ordenador ha elegido lo más rápido posible.")
print("El orden de los juegos es relevante al adivinar.")
print("¡Ten en cuenta que los juegos pueden ser duplicados!")
print("Este es el conjunto de juegos utilizado por el ordenador")
print(games)




#el bucle de juego actual, que no terminará hasta que se introduzca el conjunto correcto de juegos
while list_of_entered_games != list_of_games_to_guess: 
 #cada vez que ingresamos juegos nuevamente, tenemos que limpiar la lista de juegos ingresados
 list_of_entered_games = []
 #marcamos un nuevo intento
 print("Nuevo intento")
 print(games)

 #creamos un bucle que se ejecuta 4 veces
 for i in range(4):
     #con input ingresamos el título del próximo juego
     game_entered = int(input(f"Ingresa el juego no. {i+1}: "))
     #buscamos el juego que el jugador ha introducido en la lista de juegos
     game = games[game_entered-1]
     #append agrega el juego al final de la lista
     list_of_entered_games.append(game)
 
#------- PRUEBA---------------------------

# ----------- QUÉ ES UNA CONDICIÓN------------

 #cuatro juegos por lo que 4 bucles corren
 for i in range(4):
     #verificando que los juegos en las mismas posiciones coincidan
     if list_of_entered_games[i] == list_of_games_to_guess[i]:
        print(f"{i+1} - {list_of_entered_games[i]} - Correcto")
     else:
        print(f"{i+1} - {list_of_entered_games[i]} - Incorrecto")
 number_of_attempts+=1
 print(f"número de intentos: {number_of_attempts}")


#------------ PRUEBA------------------
