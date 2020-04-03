import random

# FUNCTIONS

# display the board
def display_board(board):
    # flood terminal with empty lines to clear old board
    print('\n'*100)
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])

# get player input for marker
def player_input():
    symbol = False
    while(symbol == False):
        player1 = input("\nPlease pick a marker 'X' or 'O': ").upper()
        if(player1 == 'X' or player1 == 'O'):
            symbol = True
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return (player1,player2)

# place the marker on space selected
def place_marker(board, marker, position):
    board[position] = marker
    return board

# check if 3 spaces are the same marker (if someone has won the game)
def win_check(board, mark):
    if (board[1] == mark and board[2] == mark and board[3] == mark):
        return True
    elif(board[4] == mark and board[5] == mark and board[6] == mark):
        return True
    elif(board[7] == mark and board[8] == mark and board[9] == mark):
        return True
    elif(board[1] == mark and board[4] == mark and board[7] == mark):
        return True
    elif(board[2] == mark and board[5] == mark and board[8] == mark):
        return True
    elif(board[3] == mark and board[6] == mark and board[9] == mark):
        return True
    elif(board[1] == mark and board[5] == mark and board[9] == mark):
        return True
    elif(board[3] == mark and board[5] == mark and board[7] == mark):
        return True
    return False

# pick a player to go first
def choose_first():
    # pick 1 or 2 randomly
    first = random.randint(1, 2)
    if first == 1:
        return "Player 1"
    return "Player 2"

# check if a space is occupied
def space_check(board, position):
    return  board[position] == ' '

# check if board is full
def full_board_check(board):
    for position in range(1,10):
        if(space_check(board, position)):
            return False
    return True

# take in player next move
def player_choice(board):
    taken = True
    while(taken):
        position = int(input('\nPlease enter a number: (1-9): '))
        if(space_check(board, position)):
            taken = False
    return position

# ask if would like to replay the game
def replay():
    again = True
    while(again):
        response = input("\nWould you like to play again? 'Yes' or 'No': ")
        if(response == "Yes"):
            print('\n'*100)
            again = False
        else:
            print("\nThanks for playing!")
            break
    

# THE GAME
def play_game():

    print('\nWelcome to Tic Tac Toe!')

    while(True):
        
        # Set up game 
        board = [' '] * 10
        player1, player2 = player_input()
        turn = choose_first()
        print(turn,"will go first")
        
        
        play_game = input("\nAre you ready to begin the game: Yes or No: ").lower()
        if(play_game == "yes"):
            game_on = True
        else:
            game_on = False
            

        #while game_on:
        while (game_on):

            #Player 1 Turn
            if(turn == "player1"):
                display_board(board)
                position = player_choice(board)
                place_marker(board, player1, position)
                
                # check if won
                if win_check(board, player1):
                    display_board(board)
                    print("\nWinner Winner Chicken Dinner")
                    game_on = False
                # check if full board
                elif(full_board_check(board)):
                    display_board(board)
                    print("\nIt's a tie!")
                    game_on = False
                # switch to player 2
                else:
                    turn = "player2"

            
            # Player2's turn.
            else:
                display_board(board)
                position = player_choice(board)
                place_marker(board, player2, position)
                
                # check if won -- make into fn in future to reduce repetitiveness
                if win_check(board, player2):
                    display_board(board)
                    print("\nWinner Winner Chicken Dinner")
                    game_on = False
                # check if board full
                elif(full_board_check(board)):
                    display_board(board)
                    print("\nIt's a tie!")
                    game_on = False
                # switch to player 1
                else:
                    turn = "player1"


        # if do not want to play again
        if (not replay()):
            break


play_game()