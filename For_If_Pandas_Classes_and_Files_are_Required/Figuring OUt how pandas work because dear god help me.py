import pandas


Data = {"X Wins": [1], "O Wins": [2], "Ties": [3]}
SavedData = pandas.DataFrame(Data)


SavedData.to_csv('PvPSaveData.csv', index = False)