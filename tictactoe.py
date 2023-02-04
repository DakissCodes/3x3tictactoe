
# TIC TAC TOE
# Player is O, computer is X


import random
import time
import os


def main():

    game = True

    while game:

        moves = 0
        board = ['1', '2', '3', '4', 'X', '6', '7', '8', '9']
        os.system('cls')
        print('\nStarting game........')

        time.sleep(2)
        display_board(board)

        while True:

            while True:
                # player's turn
                player_move = input('\nChoose a position: ')

                if move_check(player_move, board, 'O'):
                    moves += 1
                    break
                else:
                    print('Position already taken!')

            time.sleep(0.5)

            display_board(board)
            win_result = winner_check(board, moves)
            
            if win_result in [1,2,3]:
                break

            print("Computer's Turn........")
            time.sleep(1)

            # computer's turn here
            comp_possible_moves = []
            for item in board:
                if item.isnumeric():
                    comp_possible_moves.append(item)

            computer_move = random.choice(comp_possible_moves)
            move_check(computer_move, board, 'X')
            moves += 1
            display_board(board)
            win_result = winner_check(board, moves)
            
            if win_result in [1,2,3]:
                break

        if win_result == 1:
            print('PLAYER WINS!')
        elif win_result == 2:
            print('COMPUTER WINS!')
        else:
            print("DRAW!")
            

        while True:

            play_again = input('\nDo you want to play again? [Y/N] : ')
            if play_again.upper() == 'Y' or play_again.upper() == 'YES':
                break
            else:
                print('\nThanks for playing!')
                game = False
                break



def display_board(board):
    vert = "+-------+-------+-------+\n"
    pillar = "|       |       |       |\n"
    row_1 = "|   {}   |   {}   |   {}   |\n".format(
        board[0], board[1], board[2])
    row_2 = "|   {}   |   {}   |   {}   |\n".format(
        board[3], board[4], board[5])
    row_3 = "|   {}   |   {}   |   {}   |\n".format(
        board[6], board[7], board[8])
    # displays the board
    print('\n'+ vert + pillar + row_1 + pillar
          + vert + pillar + row_2 + pillar
          + vert + pillar + row_3 + pillar
          + vert)


def move_check(chosen_pos, board, sign):
    # checks whether the chosen position
    # is available by checking if they match
    for i in range(len(board)):
        if board[i] == str(chosen_pos):
            board[i] = sign
            return True

    return False


def winner_check(board, moves):
    # checks if there is a winner
    for num in range(0, 3):
        # checks for horizontal combinations
        if board[num] == board[num+1] == board[num+2]:
            if board[num] == 'O':
                return 1
            else:
                return 2
        # checks for vertical combinations
        if board[num] == board[num+3] == board[num+6]:
            if board[num] == 'O':
                return 1
            else:
                return 2
    # diagonal combinations
    if board[0] == board[4] == board[8]:
        if board[0] == 'O':
            return 1
        else:
            return 2
    if board[2] == board[4] == board[6]:
        if board[2] == 'O':
            return 1
        else:
            return 2
    # if moves reach 8 counts, it is a draw
    if moves == 8:
        return 3
    
    # if 4, continue the game
    return 4



if __name__ == "__main__":
    main()
    





