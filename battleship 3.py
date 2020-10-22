from random import randint

board = []
size = 5
turns = 1

for x in range(size):
  board.append(["O"] * size)

print ()
print ()
print ("Battleship!")
print ("___________")
print ()

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# print (ship_row)
# print (ship_col)

for turn in range(turns):
  print ()
  print ("Turn", turn + 1, "/", turns)
  print ()
  guess_row = int(input("Guess Row: ")) - 1
  guess_col = int(input("Guess Col: ")) - 1

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sunk my battleship!")
    print ()
    board[ship_row][ship_col] = "B"
    print_board(board)
    print ()
    break
  else:
    if (guess_row < 0 or guess_row > (size - 1)) or (guess_col < 0 or guess_col > (size - 1)):
      print ("Oops, that's not even in the ocean.")
      print ()
    elif(board[guess_row][guess_col] == "X"):
      print ("You guessed that one already.")
      print ()
    else:
      print ("You missed my battleship!")
      print ()
      board[guess_row][guess_col] = "X"
    if turn == turns - 1:
      print ("GAME OVER")
      print ()
      board[ship_row][ship_col] = "B"
    print_board(board)
    print ()
    
