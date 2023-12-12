import random #import necessary functions
from tkinter import * #import necessary functions
from tkinter import messagebox #import necessary functions

#TODO Soduko

#TODO Generate board that is filled in
def PlayerFirst():  # setting the function for when the player moves first
    PlayerFirst = Tk()  # initializing the window

    PlayerFirst.title("Player First")  # setting the title
    Space1 = Button(PlayerFirst, text=" ",
                    command=lambda: PlayerMove(Space1, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8,
                                               Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space1.grid(column=0, row=0)  # making the first tile
    Space2 = Button(PlayerFirst, text=" ",
                    command=lambda: PlayerMove(Space2, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8,
                                               Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space2.grid(column=0, row=1)  # making the next tile
    Space3 = Button(PlayerFirst, text=" ",
                    command=lambda: PlayerMove(Space3, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8,
                                               Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space3.grid(column=0, row=2)  # making the next tile
    Space4 = Button(PlayerFirst, text=" ",
                    command=lambda: PlayerMove(Space4, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8,
                                               Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space4.grid(column=1, row=0)  # making the next tile
    Space5 = Button(PlayerFirst, text=" ",
                    command=lambda: PlayerMove(Space5, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8,
                                               Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space5.grid(column=1, row=1)  # making the next tile
    Space6 = Button(PlayerFirst, text=" ",
                    command=lambda: PlayerMove(Space6, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8,
                                               Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space6.grid(column=1, row=2)  # making the next tile
    Space7 = Button(PlayerFirst, text=" ",
                    command=lambda: PlayerMove(Space7, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8,
                                               Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space7.grid(column=2, row=0)  # making the next tile
    Space8 = Button(PlayerFirst, text=" ",
                    command=lambda: PlayerMove(Space8, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8,
                                               Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space8.grid(column=2, row=1)  # making the next tile
    Space9 = Button(PlayerFirst, text=" ",
                    command=lambda: PlayerMove(Space9, Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8,
                                               Space9), font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space9.grid(column=2, row=2)  # making the next tile
    Button(PlayerFirst, text="Exit Game", command=lambda: PlayerFirst.destroy(), font=('Times New Roman', 40, 'bold'),
           height=1, width=8).grid(column=3, row=1)  # making the exit button

    PossibleSpaces = [Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8,
                      Space9]  # making list of possible spaces for the bot to select from


    PlayerFirst.mainloop()  # run the player moves first board
#TODO make 9x9 grid
#TODO for slot in grid
#TODO 	generate random number
#TODO 	if random number does not already exist in row/column/ whichever box it is in
#TODO 		slot text == str(random number)


#TODO make copy of board

#TODO remove random number of tutors numbers
#TODO while NumOfRemoved <= 60
#TODO 	pick random slot
#TODO 	if random slot text == " "
    #TODO 		do nothing
    #TODO 	if random slot != " "
    #TODO 		random slot text = " "
#TODO 		NumOfRemoved += 1

#TODO text boxes for slots on board with missing numbers
#TODO button to submit numbers
#TODO for slot in grid
#TODO 	if user input == same slot in filled in board turn text blue, otherwise turn it red, if empty turn font black