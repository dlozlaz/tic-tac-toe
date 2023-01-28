from random import randrange

def evaluate(game):
    """Evaluates the state of the game"""

    if 'xxx' in game:
      status = 'x'
    elif 'ooo' in game:
      status = 'o'
    elif '-' in game:
      status = '-'
    elif '-' not in game:
      status = '!'
    return(status)

def player_move(board):
  """Gets string with game board, asks the player which position to play"""
  mark = 'x'
  position = int(input('In which position do you want to play? '))
  while position < 0 or position > 19 or board[position] == 'o' or board[position] == 'x':
    if position < 0 or position > 19:
      print('You need to input a number between 0 and 19')
    elif board[position] == 'o' or board[position] == 'x':
      print('The position is already ocuppied')
    position = int(input('In which position do you want to play? '))
  board_1 = board[:position]
  board_2 = board[(position + 1):] 
  board = board_1 + mark + board_2
  return(board)

def pc_move(board):
  """Returns a game board with the computer's move"""
  mark = 'o'
  #position = randrange(0,20)
  opponent_position = board.find('x')
  if board[opponent_position + 1] == '-':
    position = opponent_position + 1
  elif board[opponent_position - 1] == '-':
      position = opponent_position - 1
  else:
    position = randrange(0,20)
    #print(position)

  board_1 = board[:position]
  board_2 = board[(position + 1):] 
  board = board_1 + mark + board_2
  return(board)

def call_moves():
  """Returns a game board with the computer's move"""
  board = '-' * 20
  print(board)
  
  
  while evaluate(board) == '-':
    board = player_move(board)
    print(board)
    if evaluate(board) == 'x':
      return('Player won')
    else:
      board = pc_move(board)
      print("It's computer's turn")
      print(board)
      if evaluate(board) == 'o':
        return('Computer won')
  if evaluate(board) == '!':
    return('The result is draw')

print(call_moves())
