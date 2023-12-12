from tkinter import * #import necessary functions
from tkinter import messagebox #import necessary functions


def PlayerMove(Space, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9): #making the function for when a player moves
        global Win
        if Win == 0: #if no one has won
            global TurnNumber
            if TurnNumber < 10: # if not all moves have been played
                if Space.cget("text") == " ": #check to see if the tile is unplayed
                    if TurnNumber%2 == 1: # Every other turn
                        Space.config(text="X") #set the selected tile to X for the players move
                        TurnNumber += 1 #turn has been made
                        if Space1.cget("text") == "X" and Space2.cget("text") == "X" and Space3.cget("text") == "X" or Space1.cget("text") == "X" and Space2.cget("text") == "X" and Space3.cget("text") == "X" or Space4.cget("text") == "X" and Space5.cget("text") == "X" and Space6.cget("text") == "X" or Space7.cget("text") == "X" and Space8.cget("text") == "X" and Space9.cget("text") == "X" or Space1.cget("text") == "X" and Space4.cget("text") == "X" and Space7.cget("text") == "X" or Space2.cget("text") == "X" and Space5.cget("text") == "X" and Space8.cget("text") == "X" or Space3.cget("text") == "X" and Space6.cget("text") == "X" and Space9.cget("text") == "X" or Space1.cget("text") == "X" and Space5.cget("text") == "X" and Space9.cget("text") == "X" or Space3.cget("text") == "X" and Space5.cget("text") == "X" and Space7.cget("text") == "X":
                            messagebox.showinfo("X Win", "X Player won!!") # ^Checks for win, this line displays in case of win
                            Win = 1 #set it so that player can't move even if turnnumber below 10
                        elif TurnNumber == 10: #If no winner & all moves made
                            messagebox.showinfo("Tie","This game was a tie") #Game is a tie
                    elif TurnNumber%2 == 0: # Every other turn
                        Space.config(text="O") #set the selected tile to X for the players move
                        TurnNumber += 1 #Turn has been made
                        if Space1.cget("text") == "O" and Space2.cget("text") == "O" and Space3.cget("text") == "O" or Space1.cget("text") == "O" and Space2.cget("text") == "O" and Space3.cget("text") == "0" or Space4.cget("text") == "O" and Space5.cget("text") == "O" and Space6.cget("text") == "O" or Space7.cget("text") == "O" and Space8.cget("text") == "O" and Space9.cget("text") == "O" or Space1.cget("text") == "O" and Space4.cget("text") == "O" and Space7.cget("text") == "O" or Space2.cget("text") == "O" and Space5.cget("text") == "O" and Space8.cget("text") == "O" or Space3.cget("text") == "O" and Space6.cget("text") == "O" and Space9.cget("text") == "O" or Space1.cget("text") == "O" and Space5.cget("text") == "O" and Space9.cget("text") == "O" or Space3.cget("text") == "O" and Space5.cget("text") == "O" and Space7.cget("text") == "O":
                            messagebox.showinfo("O Win", "O Player won!!") # ^Checks for win, this line displays in case of win
                            Win = 1 #set it to so that player can't move even if turnnumber below 10
                        elif TurnNumber == 10: #If no winner & all moves made
                            messagebox.showinfo("Tie","This game was a tie") #Game is a tie

def PlayerVersusPlayer():

    global TurnNumber
    TurnNumber = 1  # define turnnumber variable
    global Win
    Win = 0  # define win variable

    LocalPvP = Tk() #create window

    LocalPvP.title("Local PvP") #make title
    Space1 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space1, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space1.grid(column=0, row=0) #making space1
    Space2 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space2, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space2.grid(column=0, row=1) #making space2
    Space3 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space3, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space3.grid(column=0, row=2) #making space3
    Space4 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space4, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space4.grid(column=1, row=0) #making space4
    Space5 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space5, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space5.grid(column=1, row=1) #making space5
    Space6 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space6, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space6.grid(column=1, row=2) #making space6
    Space7 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space7, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space7.grid(column=2, row=0) #making space7
    Space8 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space8, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space8.grid(column=2, row=1) #making space8
    Space9 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space9, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space9.grid(column=2, row=2) #making space9
    Button(LocalPvP, text="Exit Game", command=lambda: LocalPvP.destroy(), font=('Times New Roman', 40, 'bold'), height=1, width=8).grid(column=3, row=1)

    LocalPvP.mainloop() #start window