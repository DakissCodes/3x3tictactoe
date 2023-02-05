


# 9 lists 
#
















import random
import time
import os
board = [str(pos)for pos in range(1,82)]


def main():

    game = False

    while game:

        move = 0

        board = [str(pos)for pos in range(1,82)]
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
    # prints the 3x3 board
    print("+--------+--------+--------++--------+--------+--------++--------+--------+--------+")
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("|   {}    |   {}    |   {}    ||   {}    |   {}    |   {}    ||   {}    |   {}    |   {}    |".format(board[0],board[1],board[2],board[3],board[4],
                                                                                                            board[5],board[6],board[7],board[8]))
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("+--------+--------+--------++--------+--------+--------++--------+--------+--------+")
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("|   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   |".format(board[9],board[10],board[11],board[12],board[13],
                                                                                                            board[14],board[15],board[16],board[17]))
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("+--------+--------+--------++--------+--------+--------++--------+--------+--------+")
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("|   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   |".format(board[18],board[19],board[20],board[21],board[22],
                                                                                                            board[23],board[24],board[25],board[26]))
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("+--------+--------+--------++--------+--------+--------++--------+--------+--------+")
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("|   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   |".format(board[27],board[28],board[29],board[30],board[31],
                                                                                                            board[32],board[33],board[34],board[35]))
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("+--------+--------+--------++--------+--------+--------++--------+--------+--------+")
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("|   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   |".format(board[36],board[37],board[38],board[39],board[40],
                                                                                                            board[41],board[42],board[43],board[44]))
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("+--------+--------+--------++--------+--------+--------++--------+--------+--------+")
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("|   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   |".format(board[45],board[46],board[47],board[48],board[49],
                                                                                                            board[50],board[51],board[52],board[53]))
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("+--------+--------+--------++--------+--------+--------++--------+--------+--------+")
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("|   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   |".format(board[54],board[55],board[56],board[57],board[58],
                                                                                                            board[59],board[60],board[61],board[62]))
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("+--------+--------+--------++--------+--------+--------++--------+--------+--------+")
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("|   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   |".format(board[63],board[64],board[65],board[66],board[67],
                                                                                                            board[68],board[69],board[70],board[71]))
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("+--------+--------+--------++--------+--------+--------++--------+--------+--------+")
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("|   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   ||   {}   |   {}   |   {}   |".format(board[72],board[73],board[74],board[75],board[76],
                                                                                                            board[77],board[78],board[79],board[80]))
    print("|        |        |        ||        |        |        ||        |        |        |")
    print("+--------+--------+--------++--------+--------+--------++--------+--------+--------+")




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



                                                                                                        
