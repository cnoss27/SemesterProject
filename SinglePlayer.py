import random #import necessary functions
from tkinter import * #import necessary functions
from tkinter import messagebox #import necessary functions


def PlayerFirst(): #setting the function for when the player moves first
    global TurnNumber
    TurnNumber = 1  # define turnnumber variable
    global Win
    Win = 0  # define win variable
    PlayerFirst = Tk() #initializing the window

    PlayerFirst.title("Player First") #setting the title
    Space1 = Button(PlayerFirst, text=" ", command=lambda: PlayerMove(Space1, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space1.grid(column=0, row=0) #making the first tile
    Space2 = Button(PlayerFirst, text=" ", command=lambda: PlayerMove(Space2, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space2.grid(column=0, row=1) #making the next tile
    Space3 = Button(PlayerFirst, text=" ", command=lambda: PlayerMove(Space3, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space3.grid(column=0, row=2) #making the next tile
    Space4 = Button(PlayerFirst, text=" ", command=lambda: PlayerMove(Space4, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space4.grid(column=1, row=0) #making the next tile
    Space5 = Button(PlayerFirst, text=" ", command=lambda: PlayerMove(Space5, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space5.grid(column=1, row=1) #making the next tile
    Space6 = Button(PlayerFirst, text=" ", command=lambda: PlayerMove(Space6, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space6.grid(column=1, row=2) #making the next tile
    Space7 = Button(PlayerFirst, text=" ", command=lambda: PlayerMove(Space7, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space7.grid(column=2, row=0) #making the next tile
    Space8 = Button(PlayerFirst, text=" ", command=lambda: PlayerMove(Space8, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space8.grid(column=2, row=1) #making the next tile
    Space9 = Button(PlayerFirst, text=" ", command=lambda: PlayerMove(Space9, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space9.grid(column=2, row=2) #making the next tile
    Button(PlayerFirst, text="Exit Game", command=lambda: PlayerFirst.destroy(), font=('Times New Roman', 40, 'bold'), height=1, width=8).grid(column=3, row=1) #making the exit button

    PossibleSpaces = [Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9] #making list of possible spaces for the bot to select from

    def PlayerMove(Space, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9): #making the function for when a player moves
        global Win
        if Win == 0: #if no one has won
            global TurnNumber
            if TurnNumber < 10: # if not all moves have been played
                AImoved = 0 #set it so
                if Space.cget("text") == " ":
                    Space.config(text="X")
                    if (Space1.cget("text") == "X" and Space2.cget("text") == "X" and Space3.cget("text") == "X" #Checks row 1
                            or Space4.cget("text") == "X" and Space5.cget("text") == "X" and Space6.cget("text") == "X" #Checks row 2
                            or Space7.cget("text") == "X" and Space8.cget("text") == "X" and Space9.cget("text") == "X" #Checks row 3
                            or Space1.cget("text") == "X" and Space4.cget("text") == "X" and Space7.cget("text") == "X" #Checks column 1
                            or Space2.cget("text") == "X" and Space5.cget("text") == "X" and Space8.cget("text") == "X" #Checks column 2
                            or Space3.cget("text") == "X" and Space6.cget("text") == "X" and Space9.cget("text") == "X" #Checks column 3
                            or Space1.cget("text") == "X" and Space5.cget("text") == "X" and Space9.cget("text") == "X" #Checks diagonal 1
                            or Space3.cget("text") == "X" and Space5.cget("text") == "X" and Space7.cget("text") == "X"): #Checks diagonal 2
                        messagebox.showinfo("Victory", "You Won!!")  # Checks for win, this line displays in case of win
                        Win = 1  # set it so that player can't move even if turnnumber below 10
                    TurnNumber += 1 #turn has been made
                    if Win == 0:
                        AImoved = 0
                        if TurnNumber < 9:
                            while AImoved == 0:
                                AIMove = random.choice(PossibleSpaces)
                                if AIMove.cget("text") == " ":
                                    if AIMove != Space:
                                        AIMove.config(text="O")
                                        if (Space1.cget("text") == "O" and Space2.cget("text") == "O" and Space3.cget("text") == "O"  # Checks row 1
                                                or Space4.cget("text") == "O" and Space5.cget("text") == "O" and Space6.cget("text") == "O"  # Checks row 2
                                                or Space7.cget("text") == "O" and Space8.cget("text") == "O" and Space9.cget("text") == "O"  # Checks row 3
                                                or Space1.cget("text") == "O" and Space4.cget("text") == "O" and Space7.cget("text") == "O"  # Checks column 1
                                                or Space2.cget("text") == "O" and Space5.cget("text") == "O" and Space8.cget("text") == "O"  # Checks column 2
                                                or Space3.cget("text") == "O" and Space6.cget("text") == "O" and Space9.cget("text") == "O"  # Checks column 3
                                                or Space1.cget("text") == "O" and Space5.cget("text") == "O" and Space9.cget("text") == "O"  # Checks diagonal 1
                                                or Space3.cget("text") == "O" and Space5.cget("text") == "O" and Space7.cget("text") == "O"):  # Checks diagonal 2
                                            messagebox.showinfo("Loss","You Lost.")  # Checks for loss, this line displays in case of win
                                            Win = 1  # set it so that player can't move even if turnnumber below 10
                                        AImoved = 1
                                        TurnNumber += 1  # turn has been made
            if Win == 0:
                if TurnNumber > 9:
                    messagebox.showinfo("Tie", "This Round ended in a tie")

    PlayerFirst.mainloop() #run the player moves first board

def PlayerSecond(): #setting the function for when the player moves second
    global TurnNumber
    TurnNumber = 1  # define turnnumber variable
    global Win
    Win = 0  # define win variable
    PlayerSecond = Tk() #initializing the window

    PlayerSecond.title("Player Second") #setting the title
    Space1 = Button(PlayerSecond, text=" ", command=lambda: PlayerMove(Space1, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space1.grid(column=0, row=0)
    Space2 = Button(PlayerSecond, text=" ", command=lambda: PlayerMove(Space2, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space2.grid(column=0, row=1)
    Space3 = Button(PlayerSecond, text=" ", command=lambda: PlayerMove(Space3, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space3.grid(column=0, row=2)
    Space4 = Button(PlayerSecond, text=" ", command=lambda: PlayerMove(Space4, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space4.grid(column=1, row=0)
    Space5 = Button(PlayerSecond, text=" ", command=lambda: PlayerMove(Space5, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space5.grid(column=1, row=1)
    Space6 = Button(PlayerSecond, text=" ", command=lambda: PlayerMove(Space6, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space6.grid(column=1, row=2)
    Space7 = Button(PlayerSecond, text=" ", command=lambda: PlayerMove(Space7, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space7.grid(column=2, row=0)
    Space8 = Button(PlayerSecond, text=" ", command=lambda: PlayerMove(Space8, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space8.grid(column=2, row=1)
    Space9 = Button(PlayerSecond, text=" ", command=lambda: PlayerMove(Space9, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space9.grid(column=2, row=2)
    Button(PlayerSecond, text="Exit Game", command=lambda: PlayerSecond.destroy(), font=('Times New Roman', 40, 'bold'), height=1, width=8).grid(column=3, row=1) # making exit button

    PossibleSpaces = [Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9] #setting list of possible moves for the bot

    AIMove = random.choice(PossibleSpaces) #this section is so the bot makes one move before the player
    if AIMove.cget("text") == " ": #this section is so the bot makes one move before the player
        AIMove.config(text="O") #this section is so the bot makes one move before the player

    def PlayerMove(Space, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9): #define the function for when the player moves
        global Win
        if Win == 0: #if no one has won
            global TurnNumber
            if TurnNumber < 10: # if not all moves have been played
                AImoved = 0 #set it so
                if Space.cget("text") == " ":
                    Space.config(text="X")
                    if (Space1.cget("text") == "X" and Space2.cget("text") == "X" and Space3.cget("text") == "X" #Checks row 1
                            or Space4.cget("text") == "X" and Space5.cget("text") == "X" and Space6.cget("text") == "X" #Checks row 2
                            or Space7.cget("text") == "X" and Space8.cget("text") == "X" and Space9.cget("text") == "X" #Checks row 3
                            or Space1.cget("text") == "X" and Space4.cget("text") == "X" and Space7.cget("text") == "X" #Checks column 1
                            or Space2.cget("text") == "X" and Space5.cget("text") == "X" and Space8.cget("text") == "X" #Checks column 2
                            or Space3.cget("text") == "X" and Space6.cget("text") == "X" and Space9.cget("text") == "X" #Checks column 3
                            or Space1.cget("text") == "X" and Space5.cget("text") == "X" and Space9.cget("text") == "X" #Checks diagonal 1
                            or Space3.cget("text") == "X" and Space5.cget("text") == "X" and Space7.cget("text") == "X"): #Checks diagonal 2
                        messagebox.showinfo("Victory", "You Won!!")  # Checks for win, this line displays in case of win
                        Win = 1  # set it so that player can't move even if turnnumber below 10
                    TurnNumber += 1 #turn has been made
                    if Win == 0:
                        AImoved = 0
                        while AImoved == 0:
                            AIMove = random.choice(PossibleSpaces)
                            if AIMove.cget("text") == " ":
                                if AIMove != Space:
                                    AIMove.config(text="O")
                                    if (Space1.cget("text") == "O" and Space2.cget("text") == "O" and Space3.cget("text") == "O"  # Checks row 1
                                            or Space4.cget("text") == "O" and Space5.cget("text") == "O" and Space6.cget("text") == "O"  # Checks row 2
                                            or Space7.cget("text") == "O" and Space8.cget("text") == "O" and Space9.cget("text") == "O"  # Checks row 3
                                            or Space1.cget("text") == "O" and Space4.cget("text") == "O" and Space7.cget("text") == "O"  # Checks column 1
                                            or Space2.cget("text") == "O" and Space5.cget("text") == "O" and Space8.cget("text") == "O"  # Checks column 2
                                            or Space3.cget("text") == "O" and Space6.cget("text") == "O" and Space9.cget("text") == "O"  # Checks column 3
                                            or Space1.cget("text") == "O" and Space5.cget("text") == "O" and Space9.cget("text") == "O"  # Checks diagonal 1
                                            or Space3.cget("text") == "O" and Space5.cget("text") == "O" and Space7.cget("text") == "O"):  # Checks diagonal 2
                                        messagebox.showinfo("Loss","You Lost.")  # Checks for loss, this line displays in case of win
                                        Win = 1  # set it so that player can't move even if turnnumber below 10
                                    AImoved = 1
                                    TurnNumber += 1  # turn has been made
            if TurnNumber > 8:
                messagebox.showinfo("Tie", "This Round ended in a tie")


    PlayerSecond.mainloop()
