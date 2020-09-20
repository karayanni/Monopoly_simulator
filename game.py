import Board as b
import  destinations as d
import  cards as c

s = input("please enter number of players between 3 and 6:")
while True:
    if int(s) > 6 or int(s) < 2:
        s = input("please enter a valid number of players:")
        continue
    else:
        break

board = b.Board(s)
print(board)
