from tkinter import *
from SinglePlayer import PlayerFirst, PlayerSecond
from LocalPlayerVsPlayer import PlayerVersusPlayer
from ShallWePlayAGame import GlobalThermonuclearWarfare
def TicTacToe():
    main = Tk()

    main.title("Tic-Tac-Toe Main Menu")

    Button(main, text="Single Player", command=lambda: SinglePlayer(), font=('Times New Roman',75, 'bold')).grid(column=0, row=1)
    Button(main, text="Local Player versus Player", command=lambda: PlayerVersusPlayer(), font=('Times New Roman',75, 'bold')).grid(column=0, row=2)
    Button(main, text="Close This Menu", command=lambda: main.destroy(), font=('Times New Roman',75, 'bold')).grid(column=0, row=3)
    Button(main, text="Shall we play a game?", command=lambda: GlobalThermonuclearWarfare(), height=1,width=16, font=('Times New Roman',5, 'bold')).grid(column=0, row=4)

    main.mainloop()


def SinglePlayer():
    SinglePlayerMenu = Tk()

    SinglePlayerMenu.title("Single Player Menu")
    Label(SinglePlayerMenu, text="Choose your mode:", font=('Times New Roman', 75, 'bold')).grid(column=0, row=0)
    Button(SinglePlayerMenu, text="Player moves first", command=lambda: PlayerFirst(), font=('Times New Roman', 60, 'bold')).grid(column=0, row=1)
    Button(SinglePlayerMenu, text="AI moves first", command=lambda: PlayerSecond(), font=('Times New Roman', 60, 'bold')).grid(column=0, row=2)
    Button(SinglePlayerMenu, text="Close This Menu", command=lambda: SinglePlayerMenu.destroy(), font=('Times New Roman', 60, 'bold')).grid(column=0, row=3)

    SinglePlayerMenu.mainloop()


if __name__ == '__main__':
    TicTacToe()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
