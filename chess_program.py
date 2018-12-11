#import chess.svg
import random
import chess as chess
import sys
#import pandas as pd
#import numpy as np

board = chess.Board()
move_list = []

def play():
    while len(move_list) <8:
        chess_practice()
        if len(move_list) == 8:
          sys.exit(0)
        break

def chess_practice():
    
    player_color = color_picker()
   
    print(player_color)
    if player_color == 'w':
        player_move()
        
    elif player_color =='b':
        computer_move()
            
def color_picker():
    player_color = input("What color do you want to play: \n 'w' for White, 'b' for Black\n")
    return player_color

def player_move():
    move_string = input("Please enter your move. \n i.e. e4 or Nf3 \n")
    move_list.append(move_string)
    try: 
        board.push_san(move_string)
        return computer_move()
        
    except ValueError: 
        print("That is not a legal move. Legal moves are", board.legal_moves)
        print(board)
        player_move()

def computer_move():
    moves=['e5','d5','a5','b5']
    s = random.choice(moves)   
    
    try:
      board.push_san(s)
      move_list.append(s)
    except ValueError:
      computer_move()
    
    print(board)
    print(move_list)
    return player_move()

#a.groupby(['move1w','10_q_buckets']).agg({'10_q_buckets' : np.size}).unstack(level=1).plot(kind='bar')

def generate_charts(move_list):
  pass