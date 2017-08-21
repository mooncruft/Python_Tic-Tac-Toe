import sys
from tkinter import *

#
#GameBoard for Python Tick-Tac-Toe
#
#Created By Matthew Beckwith And Help From Bradley Beckwith
#               aka - kodahScripts
# 

#import random for the AI
import random

def Start_Screen():
    root_1 = Tk()

    button_1 = Button(root_1, text='Play',fg='black',bg='blue',command=choose)
    button_2 = Button(root_1, text='Quit',fg='blue',bg='black',command=quit)

    entry_1 = Entry(root_1)
    entry_2 = Entry(root_1)

    label_1 = Label(root_1,text='Username')
    label_2 = Label(root_1,text='Password')
    
    button_1.grid(row=0,column=2)
    button_2.grid(row=1,column=2)

    entry_1.grid(row=0,column=1)
    entry_2.grid(row=1,column=1)

    label_1.grid(row=0,column=0)
    label_2.grid(row=1,column=0)
    
def Single_Player():
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

    #make a board that the code can=board = [
board = [    
        0,0,0,
        0,0,0,
        0,0,0
    ]

#Make a Board that the player can see

#we reuse this code a lot so we make it a function
def choose():

    Single_Player()
    
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

Start_Screen()
