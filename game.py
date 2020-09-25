import Board as b
import  destinations as d
import  cards as c
#import cgi
#import cgitb
#
#form = cgi.FieldStorage()
#
#num_of_players = form.getvalue("num_of_players")
#num_of_steps = form.getvalue("num_of_steps")
#starting_cash = form.getvalue("starting_cash")

s = input("please enter number of players between 3 and 6:")
while True:
    if int(s) > 6 or int(s) < 2:
        s = input("please enter a valid number of players:")
        continue
    else:
        break

board = b.Board(s)
print(board)
