from random import randint

board = []
size = 5

for x in range(size):
  board.append(["O"] * size)

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

for turn in range(5):
  print ("Turn", turn + 1)
  print ()
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sunk my battleship!")
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
    if turn == 4:
      print ("GAME OVER")
      print ()
      print ()
      board[ship_row][ship_col] = "B"
    print_board(board)
    print ()
    print ()
    
