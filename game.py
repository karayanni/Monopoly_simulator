import Board
import  destinations

while True:
    s = input("please enter number of players:")
    if s > 6 or s < 3:
        continue
    else:
        break

board = Board(s)
dest = destinations()