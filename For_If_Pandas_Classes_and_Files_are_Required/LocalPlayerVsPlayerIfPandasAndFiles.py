# Import Necessary Libraries
import tkinter
from tkinter import *
from tkinter import messagebox
import pandas

# Initialize DataFrame
Data = {'X Wins': [0], 'O Wins': [0], 'Ties': [0]}
SavedData = pandas.DataFrame(Data)


def PlayerVersusPlayer():
    # Initialize TurnNumber Variable
    global TurnNumber
    TurnNumber = 1
    # Initialize Win Variable
    global Win
    Win = 0

    def SaveData():
        # Save Current X Wins/O Wins/Ties to CSV File
        try:
            global SavedData
            SavedData.to_csv('PvPSaveData.csv', index=False)
        except FileNotFoundError:
            pass

    def UpdateText(LabelText, Text, LabelName):
        # Update X Win/O Win/Ties Counter Function
        LabelText.set(f"Number of {LabelName}\n{str(Text)}")

    def LoadData():
        # Load Saved X Wins/O Wins/Ties from CSV File
        try:
            global SavedData
            SavedData = pandas.read_csv('PvPSaveData.csv')
            XWins = SavedData["X Wins"][0]
            UpdateText(XWinsLabelText, XWins, 'X Wins')
            OWins = SavedData["O Wins"][0]
            UpdateText(OWinsLabelText, OWins, 'O Wins')
            Ties = SavedData["Ties"][0]
            UpdateText(TiesLabelText, Ties, 'Ties')
            return SavedData, XWins, OWins, Ties
        except FileNotFoundError:
            pass

    def PlayerMove(Space, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8,Space9):
        global Win # Load Win Variable
        if Win == 0:
            global TurnNumber # Load TurnNumber Variable
            global SavedData # Load SavedData Variable
            if TurnNumber < 10:
                if Space.cget("text") == " ":
                    if TurnNumber % 2 == 1:
                        # If X's Turn, Make X Move
                        Space.config(text="X")
                        TurnNumber += 1
                        if (Space1.cget("text") == "X" and Space2.cget("text") == "X" and Space3.cget("text") == "X"
                                or Space1.cget("text") == "X" and Space2.cget("text") == "X" and Space3.cget("text") == "X"
                                or Space4.cget("text") == "X" and Space5.cget("text") == "X" and Space6.cget("text") == "X"
                                or Space7.cget("text") == "X" and Space8.cget("text") == "X" and Space9.cget("text") == "X"
                                or Space1.cget("text") == "X" and Space4.cget("text") == "X" and Space7.cget("text") == "X"
                                or Space2.cget("text") == "X" and Space5.cget("text") == "X" and Space8.cget("text") == "X"
                                or Space3.cget("text") == "X" and Space6.cget("text") == "X" and Space9.cget("text") == "X"
                                or Space1.cget("text") == "X" and Space5.cget("text") == "X" and Space9.cget("text") == "X"
                                or Space3.cget("text") == "X" and Space5.cget("text") == "X" and Space7.cget("text") == "X"):
                            # If Row of X's Completed, X Win
                            messagebox.showinfo("X Win", "X Player won!!")
                            SavedData["X Wins"] = SavedData["X Wins"] + 1
                            UpdateText(XWinsLabelText, SavedData["X Wins"][0], 'X Wins')
                            Win = 1
                        elif TurnNumber == 10:
                            # If All Turns Played and No Wins, Tie Game
                            messagebox.showinfo("Tie", "This game was a tie")
                            SavedData["Ties"] = SavedData["Ties"] + 1
                            UpdateText(TiesLabelText, SavedData["Ties"][0], 'Ties')
                            Win = 1

                    elif TurnNumber % 2 == 0:
                        # If O's Turn, Make O Move
                        Space.config(text="O")
                        TurnNumber += 1
                        if (Space1.cget("text") == "O" and Space2.cget("text") == "O" and Space3.cget("text") == "O"
                                or Space1.cget("text") == "O" and Space2.cget("text") == "O" and Space3.cget("text") == "O"
                                or Space4.cget("text") == "O" and Space5.cget("text") == "O" and Space6.cget("text") == "O"
                                or Space7.cget("text") == "O" and Space8.cget("text") == "O" and Space9.cget("text") == "O"
                                or Space1.cget("text") == "O" and Space4.cget("text") == "O" and Space7.cget("text") == "O"
                                or Space2.cget("text") == "O" and Space5.cget("text") == "O" and Space8.cget("text") == "O"
                                or Space3.cget("text") == "O" and Space6.cget("text") == "O" and Space9.cget("text") == "O"
                                or Space1.cget("text") == "O" and Space5.cget("text") == "O" and Space9.cget("text") == "O"
                                or Space3.cget("text") == "O" and Space5.cget("text") == "O" and Space7.cget("text") == "O"):
                            # If Row of O's Completed, O Win
                            messagebox.showinfo("O Win", "O Player won!!")
                            SavedData["O Wins"] = SavedData["O Wins"] + 1
                            UpdateText(OWinsLabelText, SavedData["O Wins"][0], 'O Wins')
                            Win = 1
                        elif TurnNumber == 10:
                            # If All Turns Played and No Wins, Tie Game
                            messagebox.showinfo("Tie", "This game was a tie")
                            SavedData["Ties"] = SavedData["Ties"] + 1
                            UpdateText(TiesLabelText, SavedData["Ties"][0], 'Ties')
                            Win = 1
        elif Win == 1:
            # Reset After Game Win
            Space1.config(text=" ")
            Space2.config(text=" ")
            Space3.config(text=" ")
            Space4.config(text=" ")
            Space5.config(text=" ")
            Space6.config(text=" ")
            Space7.config(text=" ")
            Space8.config(text=" ")
            Space9.config(text=" ")
            TurnNumber = 1
            Win = 0

    # Make Initial Scores
    XWins = SavedData["Ties"][0]
    OWins = SavedData["Ties"][0]
    Ties = SavedData["Ties"][0]

    # Initialize the Board
    LocalPvP = Tk()

    # Create the Title
    LocalPvP.title("Local PvP")
    # Create the 9 Playing Tiles
    Space1 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space1, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 40, 'bold'), height=2, width=6)
    Space1.grid(column=0, row=0)
    Space2 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space2, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 40, 'bold'), height=2, width=6)
    Space2.grid(column=0, row=1)
    Space3 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space3, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 40, 'bold'), height=2, width=6)
    Space3.grid(column=0, row=2)
    Space4 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space4, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 40, 'bold'), height=2, width=6)
    Space4.grid(column=1, row=0)
    Space5 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space5, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 40, 'bold'), height=2, width=6)
    Space5.grid(column=1, row=1)
    Space6 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space6, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 40, 'bold'), height=2, width=6)
    Space6.grid(column=1, row=2)
    Space7 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space7, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 40, 'bold'), height=2, width=6)
    Space7.grid(column=2, row=0)
    Space8 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space8, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 40, 'bold'), height=2, width=6)
    Space8.grid(column=2, row=1)
    Space9 = Button(LocalPvP, text=" ", command=lambda: PlayerMove(Space9, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9), font=('Times New Roman', 40, 'bold'), height=2, width=6)
    Space9.grid(column=2, row=2)
    # Create Buttons to Save W Wins/O Wins/Ties
    Button(LocalPvP, text="Save Wins Losses\n& Ties", command=lambda: SaveData(), font=('Times New Roman', 20, 'bold'),height=4, width=16).grid(column=3, row=0)
    Button(LocalPvP, text="Load Wins Losses\n& Ties", command=lambda: LoadData(), font=('Times New Roman', 20, 'bold'),height=4, width=16).grid(column=3, row=1)
    Button(LocalPvP, text="Exit Game", command=lambda: LocalPvP.destroy(), font=('Times New Roman', 40, 'bold'),height=2, width=8).grid(column=3, row=2)
    # Create X Wins Label
    XWinsLabelText = tkinter.StringVar(LocalPvP)
    XWinsLabelText.set(f"Number of X Wins\n{str(XWins)}")
    XWinsLabel = Label(LocalPvP, textvariable=XWinsLabelText, relief=RAISED, font=('Times New Roman', 15, 'bold'), height=7,width=14)
    XWinsLabel.grid(column=4, row=0)
    # Create O Wins Label
    OWinsLabelText = tkinter.StringVar(LocalPvP)
    OWinsLabelText.set(f"Number of O Wins\n{str(OWins)}")
    OWinsLabel = Label(LocalPvP, textvariable=OWinsLabelText, relief=RAISED, font=('Times New Roman', 15, 'bold'), height=7,width=14)
    OWinsLabel.grid(column=4, row=1)
    # Create Ties Label
    TiesLabelText = tkinter.StringVar(LocalPvP)
    TiesLabelText.set(f"Number of Ties\n{str(Ties)}")
    TiesLabel = Label(LocalPvP, textvariable=TiesLabelText, relief=RAISED, font=('Times New Roman', 15, 'bold'), height=7,width=14)
    TiesLabel.grid(column=4, row=2)
    LocalPvP.mainloop()