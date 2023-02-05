


# 9 lists 
#


import random
import time
import os


def main():

    game = True

    while game:
        player_score = 0
        computer_score = 0
        moves = 0

        board = [str(pos)for pos in range(1,82)]
        print('\nStarting game........')

        display_board(board)

        while True:

            while True:
                # player's turn
                player_move = input('\nChoose a position: ')

                if player_move.isalpha():
                    print('Numbers 1-81 only!')
                elif int(player_move) > 81:
                    print('Not more than 81!')
                
                elif move_check(int(player_move), board, 'O'):
                    moves += 1
                    break
                else:
                    print('Position already taken!')


            display_board(board)

            win_result = winner_check(board, 'human', 'O',moves)
            
            if win_result == 1:
                player_score += 1 

                print_score(player_score, computer_score)

            elif win_result == 3:
                break

            print("Computer's Turn........")

            # computer's turn here
            comp_possible_moves = []
            for item in board:
                if item.isnumeric():
                    comp_possible_moves.append(item)

            computer_move = random.choice(comp_possible_moves)
            print(f'COMPUTER CHOSE POSITION: {computer_move}')
            move_check(int(computer_move), board, 'X')
            moves += 1
            display_board(board)
            win_result = winner_check(board, 'comp', 'X',moves)

            if win_result == 2:
                computer_score += 1 

                print_score(player_score, computer_score)

            elif win_result == 3:
                break

        print_score(player_score, computer_score)


        if player_score > computer_score:
            print('PLAYER WINS!')
        elif player_score < computer_score:
            print('COMPUTER WINS!')
        elif player_score == computer_score:
            print("IT'S A DRAW!")
            

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
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|        |        |        |        |        |        |        |        |        |")
    print("|   {}    |   {}    |   {}    |   {}    |   {}    |   {}    |   {}    |   {}    |   {}    |".format(board[0],board[1],board[2],board[3],board[4],
                                                                                                            board[5],board[6],board[7],board[8]))
    print("|        |        |        |        |        |        |        |        |        |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|        |        |        |        |        |        |        |        |        |")
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[9],board[10],board[11],board[12],board[13],
                                                                                                            board[14],board[15],board[16],board[17]))
    print("|        |        |        |        |        |        |        |        |        |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|        |        |        |        |        |        |        |        |        |")
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[18],board[19],board[20],board[21],board[22],
                                                                                                            board[23],board[24],board[25],board[26]))
    print("|        |        |        |        |        |        |        |        |        |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|        |        |        |        |        |        |        |        |        |")
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[27],board[28],board[29],board[30],board[31],
                                                                                                            board[32],board[33],board[34],board[35]))
    print("|        |        |        |        |        |        |        |        |        |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|        |        |        |        |        |        |        |        |        |")
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[36],board[37],board[38],board[39],board[40],
                                                                                                            board[41],board[42],board[43],board[44]))
    print("|        |        |        |        |        |        |        |        |        |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|        |        |        |        |        |        |        |        |        |")
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[45],board[46],board[47],board[48],board[49],
                                                                                                            board[50],board[51],board[52],board[53]))
    print("|        |        |        |        |        |        |        |        |        |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|        |        |        |        |        |        |        |        |        |")
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[54],board[55],board[56],board[57],board[58],
                                                                                                            board[59],board[60],board[61],board[62]))
    print("|        |        |        |        |        |        |        |        |        |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|        |        |        |        |        |        |        |        |        |")
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[63],board[64],board[65],board[66],board[67],
                                                                                                            board[68],board[69],board[70],board[71]))
    print("|        |        |        |        |        |        |        |        |        |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|        |        |        |        |        |        |        |        |        |")
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[72],board[73],board[74],board[75],board[76],
                                                                                                            board[77],board[78],board[79],board[80]))
    print("|        |        |        |        |        |        |        |        |        |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+")




def move_check(chosen_pos, board, sign):
    # chosen pos is index 1-81 (string)
    # board is a list with element strings from 1-81
    # sign is 'x' or 'o'
    
    # if board index of chosen pos is not in x or o 
    # change element to sign
    # else return false
    if board[chosen_pos - 1] not in ['X','O'] and len(board[chosen_pos - 1].split()) != 0:
        board[chosen_pos- 1] = board_placer(chosen_pos, 'move',sign)
        return True
    return False

def board_placer(position,action, placer):
    # position is an index
    
    if action == 'move':
        if position > 9:
            # must place extra space because orig numbers have 2 spaces
            return placer + ' '
        else:
            
            return placer
    elif action == 'clear':
        if position > 9:
            return placer + ' '
        else:
            return placer

    # accepts a position
    # if the position is > than 9 
    # must put 'X '
    # if the pos is < than 9 'X'
    
def print_score(player_score,computer_score):
    print('HUMAN SCORE: {}'.format(str(player_score)))
    print('COMPUTER SCORE: {}'.format(str(computer_score)))
    
def winner_check(board,player,sign,game_moves):
    # HORIZONTAL COMBINATIONS 
    # loop through each row
    for row in [0,9,18,27,36,45,54,63,72]:
        # for each row, loop through each element
        for i in range(row,row+7):
            
            # if 3 adjacent positions with same sign
            if (board[i] == board[i+1] == board[i+2]) and board[i].strip() in [sign]:

                board[i] = board_placer(i, 'clear', ' ')
                board[i+1] = board_placer(i+1, 'clear', ' ')
                board[i+2] = board_placer(i+2, 'clear', ' ')
                if player == 'human':
                    return 1
                elif player == 'comp':
                    return 2
                
    #VERTICAL COMBINATIONS
    #loop through each column, 0-8 index 
    for column in [pos for pos in range(0,9)]:
        # loops through each num in each column
        for i in range(column,column + 55,9):

            # loop through the numbers in the column through steps of 9 to access the index
            if (board[i].strip() == board[i+9].strip() == board[i+18].strip()) and board[i].strip() in [sign]:

                board[i] = board_placer(i, 'clear', ' ')
                board[i+9] = board_placer(i+9, 'clear', ' ')
                board[i+18] = board_placer(i+18, 'clear', ' ')
                if player == 'human':
                    return 1
                elif player == 'comp':
                    return 2
     
     # DIAGONAL COMBINATIONS
     
     # Down diagonal right
    for row in [0,9,18,27,36,45,54]:
        for i in range(row,row+7):
            if (board[i].split() == board[i+10].split() == board[i+20].split()) and board[i].strip() in [sign]:

                board[i] = board_placer(i, 'clear', ' ')
                board[i+10] = board_placer(i+10, 'clear', ' ')
                board[i+20] = board_placer(i+20, 'clear', ' ')
                if player == 'human':
                    return 1
                elif player == 'comp':
                    return 2
            
    # diagonal up right
    for row in [72,63,54,45,36,27,18]:
        for i in range(row,row+7):
            if (board[i].split() == board[i-8].split() == board[i-16].split()) and board[i].strip() in [sign]:
                board[i] = board_placer(i, 'clear', ' ')
                board[i-8] = board_placer(i-8, 'clear', ' ')
                board[i-16] = board_placer(i-16, 'clear', ' ')
                if player == 'human':
                    return 1
                elif player == 'comp':
                    return 2 
                
    if game_moves >= 81:
        return 3
        
        
            
    
    
if __name__ == '__main__':
    main()
