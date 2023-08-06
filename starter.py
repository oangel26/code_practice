import random
 
#juegos son todos los títulos de juegos que el programa puede usar; los participantes pueden dar sus propias propuestas
games = ["Pokemon(1)", "Fortnite(2)", "Minecraft(3)", "CS(4)"]
#lista_de_juegos_a_adivinar es la variable donde insertamos la contraseña a adivinar
list_of_games_to_guess = []
#lista_de_juegos_ingresados es una lista de juegos ingresados por el usuario
list_of_entered_games = []
###TODO LO DE ARRIBA ES UN PROYECTO INICIAL


###INICIAL
#mostramos las instrucciones 
print("Bienvenido al juego MasterMind")
print("Tu objetivo es adivinar los 4 juegos que el ordenador ha elegido lo más rápido posible.")
print("El orden de los juegos es relevante al adivinar.")
print("¡Ten en cuenta que los juegos pueden ser duplicados!")
print("Este es el conjunto de juegos utilizado por el ordenador")
print(games)
