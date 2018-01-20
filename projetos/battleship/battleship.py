# gerar numero randomico
from random import randint 

board = [] # mesa de jogo

# usuario ter 4 oportunidades de tentar
# descobrir onde est o navio para afundar
for x in range(5):
  board.append(["O"] * 5)
  
def print_board(board):
  """imprime a mesa de jogo de forma amigvel"""
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  """gera uma posio aleatrio para a linha"""
  return randint(0, len(board) - 1)

def random_col(board):
  """gera uma posio aleatrio para a coluna"""
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row #fins de debug
#print ship_col #fins de debug

	# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

# comea o turno
for turn in range(4):
  # pergunta qual linha/coluna o usurio
  # acha que o navio est
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  # acertou a posio
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    break
    
    # errou
  else:
    # chute est fora da quantidade de 
    # linhas ou colunas da mesa do jogo
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    
    # j tentou essa posio antes
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
      
    # errou a posio do navio
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"

    # errou todas as tentativas, fim de jogo
    if turn == 3: print "Game Over"
  
  # Print (turn + 1) here!
  print "Turn ", turn + 1
  print_board(board)