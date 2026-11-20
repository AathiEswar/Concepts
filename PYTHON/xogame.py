def board(display_board):
    print(f"{display_board[7]} | {display_board[8]} | {display_board[9]}")
    print(f"{display_board[4]} | {display_board[5]} | {display_board[6]}")
    print(f"{display_board[1]} | {display_board[2]} | {display_board[3]}")

def user_symbol():
    choice_symbol = "wrong"
    acceptable_values1 = ['x',"X"]
    acceptable_values2= ['o',"O"]


    while choice_symbol not in acceptable_values1 or choice_symbol not in acceptable_values2:
        choice_symbol = input("Enter symbol for player1 (X or O):")

        if choice_symbol in acceptable_values1:
            player1 = "X"
            player2 = "O"
            return player1,player2

        elif choice_symbol in acceptable_values2:
            player1 = "O"
            player2 = "X"
            return player1,player2

        else:
            print("INVALID INPUT ENTER X OR O")


def position_update(display_board,player_sym,position_to_update):
    display_board[position_to_update] = player_sym

    return display_board

def win_no(display_board,player_sym):
    if (display_board[1] == display_board[2] == display_board[3] == player_sym or
        display_board[4] == display_board[5] == display_board[6] == player_sym or
        display_board[7] == display_board[8] == display_board[9] == player_sym or
        display_board[1] == display_board[4] == display_board[7] == player_sym or
        display_board[8] == display_board[5] == display_board[2] == player_sym or
        display_board[9] == display_board[6] == display_board[3] == player_sym or
        display_board[4] == display_board[5] == display_board[7] == player_sym or 
        display_board[1] == display_board[5] == display_board[9] == player_sym ):
        return True

    else:
        return False
def check_all_full(display_board):
    for i in range(1,10):
        if space_check(display_board,i):
            return False

    return True      

def space_check(display_board,position):
    return display_board[position] == " "
    
def player_choice(display_board):
    position = 10

    while position not in range(1,10) or not space_check(display_board,position):
        position = int(input("Enter the position to change:"))

        if position not in range(1,10):
            print("Enter a input of range 1-9")

    return position


print("WELCOME TO THE XO GAME")

while True:
    display_board = [" "," "," "," "," "," "," "," "," "," "]
    player1,player2 = user_symbol()
    turn = "player1"
    ready = input("Ready to play the game? n or y:")

    if ready.lower() ==  "y":
        game_on = True
    else:
        print("THANK YOU FOR PLAYING")
        game_on = False
        break
    while game_on:
        if turn == "player1":
            board(display_board)
            position = player_choice(display_board)
            position_update(display_board,player1,position)
            if win_no(display_board,player1):
                board(display_board)
                print("PLAYER 1 WON ")
                game_won_n = 1
                break

                game_on = False

            else:
                if check_all_full(display_board):
                    board(display_board)
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = "player2"

        else:
            board(display_board)
            position = player_choice(display_board)
            position_update(display_board,player2,position)
            if win_no(display_board,player2):
                board(display_board)
                print("PLAYER 2 WON ")
                break
                

            else:
                if check_all_full(display_board):
                    board(display_board)
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = "player1"

    if game_on ==1:

        break














