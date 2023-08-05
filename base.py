#!/usr/bin/python
import random
 
 
#games are all the titles of games that the program can use; participants can give their own propositions
games = ["Pokemon(1)", "Fortnite(2)", "Minecraft(3)", "CS(4)"]
#list_of_games_to_guess is the variable into which we insert the password to guess
list_of_games_to_guess = []
#list_of_entered_games is a list of games entered by the user
list_of_entered_games = []
###EVERYTHING ABOVE IS A STARTER PROJECT
 
 
#------- QUE ES UNA VARIABLE ---------

#round counter
number_of_attempts = 0 
 

#-----------QUE ES UN BUCLE - FOR LOOP--------

#we draw passwords to guess

for i in range(4):
 game_drawn = random.choice(games)

 #append means adding to the list

 list_of_games_to_guess.append(game_drawn)
 
#it is a good idea to display the generated password for testing purposes at this stage
#print(list_of_games_to_guess)
#this line has to be commented out so the player cannot see which games have been drawn. Displaying the list is only needed for testing
 
#--------- TEST---------------


###STARTER
#we display the instructions 
print("Welcome to the MasterMind game")
print("Your goal is to guess the 4 games that have been drawn by the computer as quickly as possible.")
print("The order of the games is relevant when guessing.")
print("Please note the games may be duplicated!!!")
print("Here is the set of games used by the computer")
print(games)




#the actual gameplay loop, which will not end until the correct set of games is entered
while list_of_entered_games != list_of_games_to_guess: 
 #every time we enter games again, we have to clear the list of entered games 
 list_of_entered_games = []
 #we mark a new attempt
 print("New attempt")
 print(games)

 #we create a loop that executes 4 times
 for i in range(4):
     #with input we enter the title of the next game
     game_entered = int(input(f"Enter a game no. {i+1}: "))
     #we search for the game the player has entered in the list of games
     game = games[game_entered-1]
     #append adds the game to the end of the list
     list_of_entered_games.append(game)
 
#------- TEST---------------------------

# ----------- QUE ES UNA CONDICION------------

 #four games so 4 loop runs
 for i in range(4):
     # checking that the games in the same positions match
     if list_of_entered_games[i] == list_of_games_to_guess[i]:
        print(f"{i+1} - {list_of_entered_games[i]} - Correct")
     else:
        print(f"{i+1} - {list_of_entered_games[i]} - Incorrect")
 number_of_attempts+=1
 print(f"number of attempts: {number_of_attempts}")


#------------ TEST------------------
