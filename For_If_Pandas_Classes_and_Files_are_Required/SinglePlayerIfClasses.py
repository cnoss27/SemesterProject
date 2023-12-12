import random #import necessary functions
from tkinter import * #import necessary functions
from tkinter import messagebox #import necessary functions

# Make Class For Single Player Board
class SinglePlayerBoard:
    def __init__(self, PlayerFirstOrPlayerSecond, TitleOfBoard, Players_First_Move_1_Or_0, TurnNumber, Win):
        self.TurnNumber = 1  # Define TurnNumber Variable
        self.Win = 0  # Define Win Variable
        self.PlayerFirstOrPlayerSecond = Tk()  # Initializing the Window

        self.PlayerFirstOrPlayerSecond.title(str(TitleOfBoard))  # setting the title
        Space1 = Button(self.PlayerFirstOrPlayerSecond, text=" ", command=lambda: PlayerMove(Space1, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
        Space1.grid(column=0, row=0)  # making the first tile
        Space2 = Button(self.PlayerFirstOrPlayerSecond, text=" ", command=lambda: PlayerMove(Space2, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
        Space2.grid(column=0, row=1)  # making the next tile
        Space3 = Button(self.PlayerFirstOrPlayerSecond, text=" ", command=lambda: PlayerMove(Space3, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
        Space3.grid(column=0, row=2)  # making the next tile
        Space4 = Button(self.PlayerFirstOrPlayerSecond, text=" ", command=lambda: PlayerMove(Space4, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
        Space4.grid(column=1, row=0)  # making the next tile
        Space5 = Button(self.PlayerFirstOrPlayerSecond, text=" ", command=lambda: PlayerMove(Space5, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
        Space5.grid(column=1, row=1)  # making the next tile
        Space6 = Button(self.PlayerFirstOrPlayerSecond, text=" ", command=lambda: PlayerMove(Space6, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
        Space6.grid(column=1, row=2)  # making the next tile
        Space7 = Button(self.PlayerFirstOrPlayerSecond, text=" ", command=lambda: PlayerMove(Space7, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
        Space7.grid(column=2, row=0)  # making the next tile
        Space8 = Button(self.PlayerFirstOrPlayerSecond, text=" ", command=lambda: PlayerMove(Space8, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
        Space8.grid(column=2, row=1)  # making the next tile
        Space9 = Button(self.PlayerFirstOrPlayerSecond, text=" ", command=lambda: PlayerMove(Space9, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
        Space9.grid(column=2, row=2)  # making the next tile
        Button(self.PlayerFirstOrPlayerSecond, text="Exit Game", command=lambda: self.PlayerFirstOrPlayerSecond.destroy(), font=('Times New Roman', 40, 'bold'), height=1, width=8).grid(column=3, row=1)  # making the exit button

        # making list of possible spaces for the bot to select from
        PossibleSpaces = [Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9]

        if TurnNumber == 1 and Players_First_Move_1_Or_0 == 1:
            AIMove = random.choice(PossibleSpaces)  # this section is so the bot makes one move before the player
            if AIMove.cget("text") == " ":  # this section is so the bot makes one move before the player
                AIMove.config(text="O")  # this section is so the bot makes one move before the player

        def PlayerMove(Space, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9):  # define the function for when the player moves
            if self.Win == 0:  # if no one has won
                if self.TurnNumber < 10:  # if not all moves have been played
                    AImoved = 0  # set it so Bot hasn't moved yet
                    if Space.cget("text") == " ":
                        Space.config(text="X")
                        if (Space1.cget("text") == "X" and Space2.cget("text") == "X" and Space3.cget("text") == "X"  # Checks row 1
                                or Space4.cget("text") == "X" and Space5.cget("text") == "X" and Space6.cget("text") == "X"  # Checks row 2
                                or Space7.cget("text") == "X" and Space8.cget("text") == "X" and Space9.cget("text") == "X"  # Checks row 3
                                or Space1.cget("text") == "X" and Space4.cget("text") == "X" and Space7.cget("text") == "X"  # Checks column 1
                                or Space2.cget("text") == "X" and Space5.cget("text") == "X" and Space8.cget("text") == "X"  # Checks column 2
                                or Space3.cget("text") == "X" and Space6.cget("text") == "X" and Space9.cget("text") == "X"  # Checks column 3
                                or Space1.cget("text") == "X" and Space5.cget("text") == "X" and Space9.cget("text") == "X"  # Checks diagonal 1
                                or Space3.cget("text") == "X" and Space5.cget("text") == "X" and Space7.cget("text") == "X"):  # Checks diagonal 2
                            messagebox.showinfo("Victory","You Won!!")  # Checks for win, this line displays in case of win
                            self.Win = 1  # set it so that player can't move even if turnnumber below 10
                        self.TurnNumber += 1  # turn has been made
                        if self.Win == 0:
                            AImoved = 0
                            if self.TurnNumber < 9:
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
                                                self.Win = 1  # set it so that player can't move even if turnnumber below 10
                                            AImoved = 1
                                            self.TurnNumber += 1  # turn has been made
                if self.Win == 0:
                    if Players_First_Move_1_Or_0 == 0:
                        if self.TurnNumber > 9:
                            messagebox.showinfo("Tie", "This Round ended in a tie")
                    elif Players_First_Move_1_Or_0 == 1:
                        if self.TurnNumber > 8:
                            messagebox.showinfo("Tie", "This Round ended in a tie")

        self.PlayerFirstOrPlayerSecond.mainloop()  # run the board