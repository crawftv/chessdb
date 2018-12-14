import chess
from helper_functions import generate_fics_chart, generate_high_elo_move_commentary, generate_high_elo_weighted_moves
import chess.svg
import sys

def play():
    board = chess.Board()
    move_list = []
    player_color = color_picker()
    while len(move_list) <=8:
        
        chess_practice(board, player_color, move_list)
        if len(move_list) == 8:
          sys.exit()
        break
           
def color_picker():
    player_color = input("What color do you want to play: \n 'w' for White, 'b' for Black\n")
    return player_color

def chess_practice(board, player_color, move_list):
    if player_color == 'w':
        player_move(board, move_list)
        
    elif player_color =='b':
        computer_move(board, move_list)

def player_move(board, move_list):
    generate_fics_chart(move_list)
    move_string = input("Please enter your move. \n i.e. e4 or Nf3 \n")
    
    try: 
        board.push_san(move_string)
        move_list.append(move_string)
        print(move_list, len(move_list))
        generate_high_elo_move_commentary(move_list)
        return computer_move(board, move_list)
    except ValueError: 
        print(move_string + " is not a legal move. Legal moves are", board.legal_moves)
        return player_move(board, move_list)

def computer_move(board, move_list):   
    try:
        s = generate_high_elo_weighted_moves(move_list)
        board.push_san(s)
        move_list.append(s)
        print("Computer Plays " +s)
        
        print (board)
        print(move_list, len(move_list))

        return player_move(board, move_list)
    except ValueError:
        return computer_move(board, move_list)    