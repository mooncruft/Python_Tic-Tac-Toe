#
#GameBoard for Python Tick-Tac-Toe
#
#Created By Matthew Beckwith
#               aka - kodahScripts
#

#import random for the AI
import random


#Make a Board that the player can see
print("""
      TIC-TAC-TOE

        |    |
        |    |
    ----|----|----
        |    |
    ----|----|----
        |    |
        |    |
""")

#make a board that the code can check
board = [
    0,0,0,
    0,0,0,
    0,0,0
]

#we reuse this code a lot so we make it a function
def choose():
    choice = int(input("Pick a place to start (1-9)"))
    
    if(board[choice] > 0):
        print("This has already been picked.... Please pick another")
        choose()
    else:
        drawBoard(1,choice)
        computerChoice()

#Give the player an Enemy
def computerChoice():
    choice = random.randint(1,9)#a random number between 1 and 9

    if(board[choice] > 0):          #computer picks a box already choosen
       choice = random.randint(1,9) #try again

    else:
       drawBoard(2,choice)

#Will handle showing the modified board to the user
def drawBoard(player,choice):
    print("Draw Board - Player: " + str(player) + ", Choice: " + str(choice))

choose()
