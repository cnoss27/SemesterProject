from tkinter import *
from tkinter import messagebox
import random
import time
from time import sleep

# I got a lot of help from online and copied some code for the min/max algorithms
# because I have no clue how to do it myself without quite a bit of help like this.
# I asked you in class, and you said this was okay.

# Initialize TurnNumber Variable
global TurnNumber
TurnNumber = 0
# Initialize tracking_var Variable (used to loop function on click without causing crash)
global tracking_var
tracking_var = False

def GlobalThermonuclearWarfare():
    global TurnNumber

    def MakeOptimalMove(Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9):
        global TurnNumber
        # Python3 program to find the next optimal move for a player
        if TurnNumber % 2 == 0:
            player, opponent = 'X', 'O'
        elif TurnNumber % 2 == 1:
            player, opponent = 'O', 'X'

        # This function returns true if there are moves
        # remaining on the board. It returns false if
        # there are no moves left to play.
        def isMovesLeft(board):

            for i in range(3):
                for j in range(3):
                    if (board[i][j] == ' '):
                        return True
            return False

        # This is the evaluation function as discussed
        # in the previous article ( http://goo.gl/sJgv68 )
        def evaluate(b):

            # Checking for Rows for X or O victory.
            for row in range(3):
                if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
                    if (b[row][0] == player):
                        return 10
                    elif (b[row][0] == opponent):
                        return -10

            # Checking for Columns for X or O victory.
            for col in range(3):

                if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):

                    if (b[0][col] == player):
                        return 10
                    elif (b[0][col] == opponent):
                        return -10

            # Checking for Diagonals for X or O victory.
            if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

                if (b[0][0] == player):
                    return 10
                elif (b[0][0] == opponent):
                    return -10

            if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

                if (b[0][2] == player):
                    return 10
                elif (b[0][2] == opponent):
                    return -10

            # Else if none of them have won then return 0
            return 0

        # This is the minimax function. It considers all
        # the possible ways the game can go and returns
        # the value of the board
        def minimax(board, depth, isMax):
            score = evaluate(board)

            # If Maximizer has won the game return his/her
            # evaluated score
            if (score == 10):
                return score

                # If Minimizer has won the game return his/her
            # evaluated score
            if (score == -10):
                return score

                # If there are no more moves and no winner then
            # it is a tie
            if (isMovesLeft(board) == False):
                return 0

            # If this maximizer's move
            if (isMax):
                best = -1000

                # Traverse all cells
                for i in range(3):
                    for j in range(3):

                        # Check if cell is empty
                        if (board[i][j] == ' '):
                            # Make the move
                            board[i][j] = player

                            # Call minimax recursively and choose
                            # the maximum value
                            best = max(best, minimax(board,
                                                     depth + 1,
                                                     not isMax))

                            # Undo the move
                            board[i][j] = ' '
                return best

                # If this minimizer's move
            else:
                best = 1000

                # Traverse all cells
                for i in range(3):
                    for j in range(3):

                        # Check if cell is empty
                        if (board[i][j] == ' '):
                            # Make the move
                            board[i][j] = opponent

                            # Call minimax recursively and choose
                            # the minimum value
                            best = min(best, minimax(board, depth + 1, not isMax))

                            # Undo the move
                            board[i][j] = ' '
                return best

                # This will return the best possible move for the player

        def findBestMove(board):
            bestVal = -1000
            bestMove = (-1, -1)

            # Traverse all cells, evaluate minimax function for
            # all empty cells. And return the cell with optimal
            # value.
            for i in range(3):
                for j in range(3):

                    # Check if cell is empty
                    if (board[i][j] == ' '):

                        # Make the move
                        board[i][j] = player

                        # compute evaluation function for this
                        # move.
                        moveVal = minimax(board, 0, False)

                        # Undo the move
                        board[i][j] = ' '

                        # If the value of the current move is
                        # more than the best value, then update
                        # best/
                        if (moveVal > bestVal):
                            bestMove = (i, j)
                            bestVal = moveVal

            return bestMove
            # Driver code

        board = [
            [str(Space1.cget("text")), str(Space2.cget("text")), str(Space3.cget("text"))],
            [str(Space4.cget("text")), str(Space5.cget("text")), str(Space6.cget("text"))],
            [str(Space7.cget("text")), str(Space8.cget("text")), str(Space9.cget("text"))]
        ]

        if TurnNumber == 0:
            # Randomly Choose First Move So the Board Changes Each Round, Also Speeds Up First Choice
            random.choice([Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9]).config(text="X")
            TurnNumber += 1
        elif TurnNumber == 9:
            # Once All 9 Moves Have Been Played Wait 0.5 Seconds Then Reset Board
            time.sleep(0.5)
            Space1.config(text=" "), Space2.config(text=" "), Space3.config(text=" "), Space4.config(text=" "), Space5.config(text=" "), Space6.config(text=" "), Space7.config(text=" "), Space8.config(text=" "), Space9.config(text=" ")
            TurnNumber = 0
        elif TurnNumber % 2 == 0:
            # Place Best Move For X's Turn
            bestMove = findBestMove(board)
            if bestMove[0] == 0:
                if bestMove[1] == 0:
                    Space1.config(text="X")
                    TurnNumber += 1
                if bestMove[1] == 1:
                    Space2.config(text="X")
                    TurnNumber += 1
                if bestMove[1] == 2:
                    Space3.config(text="X")
                    TurnNumber += 1
            if bestMove[0] == 1:
                if bestMove[1] == 0:
                    Space4.config(text="X")
                    TurnNumber += 1
                if bestMove[1] == 1:
                    Space5.config(text="X")
                    TurnNumber += 1
                if bestMove[1] == 2:
                    Space6.config(text="X")
                    TurnNumber += 1
            if bestMove[0] == 2:
                if bestMove[1] == 0:
                    Space7.config(text="X")
                    TurnNumber += 1
                if bestMove[1] == 1:
                    Space8.config(text="X")
                    TurnNumber += 1
                if bestMove[1] == 2:
                    Space9.config(text="X")
                    TurnNumber += 1
        elif TurnNumber % 2 == 1:
            # Place Best Move For O's Turn
            bestMove = findBestMove(board)
            if bestMove[0] == 0:
                if bestMove[1] == 0:
                    Space1.config(text="O")
                    TurnNumber += 1
                if bestMove[1] == 1:
                    Space2.config(text="O")
                    TurnNumber += 1
                if bestMove[1] == 2:
                    Space3.config(text="O")
                    TurnNumber += 1
            if bestMove[0] == 1:
                if bestMove[1] == 0:
                    Space4.config(text="O")
                    TurnNumber += 1
                if bestMove[1] == 1:
                    Space5.config(text="O")
                    TurnNumber += 1
                if bestMove[1] == 2:
                    Space6.config(text="O")
                    TurnNumber += 1
            if bestMove[0] == 2:
                if bestMove[1] == 0:
                    Space7.config(text="O")
                    TurnNumber += 1
                if bestMove[1] == 1:
                    Space8.config(text="O")
                    TurnNumber += 1
                if bestMove[1] == 2:
                    Space9.config(text="O")
                    TurnNumber += 1

    def TheOnlyWinningMove():
        # Display the Easter Egg Messages One After Another
        messagebox.showinfo("", "A strange game.")
        time.sleep(0)
        messagebox.showinfo("", "The only winning move is not to play.")
        time.sleep(0)
        messagebox.showinfo("", "How about a nice game of chess?")

    Joshua = Tk()  # create window

    Joshua.title("Global ThermoNuclear Warfare")  # make title
    Space1 = Label(Joshua, text=" ", relief=RAISED, font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space1.grid(column=0, row=0)  # making space1
    Space2 = Label(Joshua, text=" ", relief=RAISED, font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space2.grid(column=0, row=1)  # making space2
    Space3 = Label(Joshua, text=" ", relief=RAISED, font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space3.grid(column=0, row=2)  # making space3
    Space4 = Label(Joshua, text=" ", relief=RAISED, font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space4.grid(column=1, row=0)  # making space4
    Space5 = Label(Joshua, text=" ", relief=RAISED, font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space5.grid(column=1, row=1)  # making space5
    Space6 = Label(Joshua, text=" ", relief=RAISED, font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space6.grid(column=1, row=2)  # making space6
    Space7 = Label(Joshua, text=" ", relief=RAISED, font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space7.grid(column=2, row=0)  # making space7
    Space8 = Label(Joshua, text=" ", relief=RAISED, font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space8.grid(column=2, row=1)  # making space8
    Space9 = Label(Joshua, text=" ", relief=RAISED, font=('Times New Roman', 60, 'bold'), height=2, width=6)
    Space9.grid(column=2, row=2)  # making space9
    Button(Joshua, text="Click To Toggle\nSimulation of\nIdeal Moves", command=lambda: loop(True), font=('Times New Roman', 30, 'bold'), height=3, width=16).grid(column=3, row=1)
    Button(Joshua, text="Exit", command=lambda: Joshua.destroy(), font=('Times New Roman', 40, 'bold'), height=2, width=12).grid(column=3, row=2)


    def loop(toggle=False):
        # Function to Loop Best Moves On Click Without Crashing Everything
        global tracking_var
        if toggle:
            if tracking_var:
                tracking_var = False
            else:
                tracking_var = True

        if tracking_var:
            MakeOptimalMove(Space1, Space2, Space3, Space4, Space5, Space6, Space7, Space8, Space9)
            Joshua.after(100, loop)

    # Plays Easter Egg Text
    Joshua.after(30000, lambda: TheOnlyWinningMove())
    Joshua.mainloop()  # start window

    # This code is contributed by divyesh072019