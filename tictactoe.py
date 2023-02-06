
import random
import time
import os
import string
import shutil

def main():
    
    # run the game
    game = True

    while game:
        # records scores and moves
        player_score = 0
        computer_score = 0
        moves = 0

        # 9x9 board
        board = [str(pos)for pos in range(1,82)]
        print('\nStarting game........')

        display_board(board)

        while True:

            while True:
                not_num = False
                
                # player's turn, asks user for a position on the board
                player_move = input('\nChoose a position: ')
                
                # checks if user inputs letter
                if player_move == '':
                    print('Invalid!')
                    continue
                
                for char in player_move:
                    if char.isalpha():
                        not_num = True

                # if input is all numbers
                if not not_num: 
                    # checks that input is within 1-81
                    if int(player_move) > 81:
                        print('Positions 1-81 only!')
                    # if input is valid, check if position on the board is available
                    elif move_check(int(player_move), board, 'O'):
                        moves += 1
                        break
                    else:
                        print('Position already taken!')
                else:
                    print('Not a number!')

            display_board(board)
        
            # checks winner
            win_result = winner_check(board, 'human', 'O',moves)
            
            # if player gets 3 matches, +1 to the score
            if win_result == 1:
                player_score += 1 
                print_score(player_score, computer_score)
            # if there are no more moves available, stop game
            elif win_result == 3:
                break

            print("Computer's Turn........")

            # computer's turn 
            comp_possible_moves = []
            
            # append all available moves to a list
            for item in board:
                if item.isnumeric():
                    comp_possible_moves.append(item)
            # randomly choose from that list
            computer_move = random.choice(comp_possible_moves)
            print(f'COMPUTER CHOSE POSITION: {computer_move}')

            # computer move
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


        # checks who got the most matches
        if player_score > computer_score:
            print('PLAYER WINS!')
        elif player_score < computer_score:
            print('COMPUTER WINS!')
        elif player_score == computer_score:
            print("IT'S A DRAW!")
            
        # asks user if wants to play again 
        while True:

            play_again = input('\nDo you want to play again? [Y/N] : ')
            if play_again.upper() == 'Y' or play_again.upper() == 'YES':
                break
            else:
                print('\nThanks for playing!')
                game = False
                break



def display_board(board):
    # This function prints the 9x9 board by filling in the arguments
    # with the elements on the list that represents the 9x9 board

    columns = shutil.get_terminal_size().columns
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+".center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("|   {}    |   {}    |   {}    |   {}    |   {}    |   {}    |   {}    |   {}    |   {}    |".format(board[0],board[1],board[2],board[3],board[4],
                                                                                                            board[5],board[6],board[7],board[8]).center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+".center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[9],board[10],board[11],board[12],board[13],
                                                                                                            board[14],board[15],board[16],board[17]).center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+".center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[18],board[19],board[20],board[21],board[22],
                                                                                                            board[23],board[24],board[25],board[26]).center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+".center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[27],board[28],board[29],board[30],board[31],
                                                                                                            board[32],board[33],board[34],board[35]).center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+".center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[36],board[37],board[38],board[39],board[40],
                                                                                                            board[41],board[42],board[43],board[44]).center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+".center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[45],board[46],board[47],board[48],board[49],
                                                                                                            board[50],board[51],board[52],board[53]).center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+".center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[54],board[55],board[56],board[57],board[58],
                                                                                                            board[59],board[60],board[61],board[62]).center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+".center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[63],board[64],board[65],board[66],board[67],
                                                                                                            board[68],board[69],board[70],board[71]).center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+".center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(board[72],board[73],board[74],board[75],board[76],
                                                                                                            board[77],board[78],board[79],board[80]).center(columns))
    print("|        |        |        |        |        |        |        |        |        |".center(columns))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+".center(columns))




        

def move_check(chosen_pos, board, sign):
    # This function checks whether a move is available 
    # by checking whether the position is already occupied
    

    # if position is not yet occupied by an 'X' or an 'O'
    # return True and place the appropriate sign, otherwise return False
    if board[chosen_pos - 1].strip() not in ['X','O','']:
        board[chosen_pos- 1] = board_placer(chosen_pos, 'move',sign)
        return True
    return False

def board_placer(position,action, placer):
    # This function checks whether a white space is needed when placing
    # a sign on the board. This is to avoid messing up the board when printing
    # When a position is more than 9, it requires an extra white space.
    
    if action == 'move':
        if position > 9:
            return placer + ' '
        else:
            return placer
    elif action == 'clear':
        if position >= 9:
            return placer + ' '
        else:
            return placer

    
def print_score(player_score,computer_score):
    # prints the score of the player and computer
    print('HUMAN SCORE: {}'.format(str(player_score)))
    print('COMPUTER SCORE: {}'.format(str(computer_score)))
    
def winner_check(board,player,sign,game_moves):
    # This function checks whether there is a match on the board.
    # It checks matches horizontally, vertically and diagonally all
    # across the board.
    
    # HORIZONTAL COMBINATIONS 
    # loops through the rows of the board
    for row in [0,9,18,27,36,45,54,63,72]:
        # loops through every element in the row
        for i in range(row,row+7):
            
            # checks if  3 adjacent positions has the same sign
            if (board[i] == board[i+1] == board[i+2]) and board[i].strip() in [sign]:
                # if True, clears the match and returns who made the match
                board[i] = board_placer(i, 'clear', ' ')
                board[i+1] = board_placer(i+1, 'clear', ' ')
                board[i+2] = board_placer(i+2, 'clear', ' ')
                if player == 'human':
                    return 1
                elif player == 'comp':
                    return 2
                
    #VERTICAL COMBINATIONS
    # loop through each column, 0-8 index 
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
     
    # Down-right diagonal
    # loops through the first 7 rows
    for row in [0,9,18,27,36,45,54]:
        # checks for diagonal combinations by adding +10
        for i in range(row,row+7):
            if (board[i].strip() == board[i+10].strip() == board[i+20].strip()) and board[i].strip() in [sign]:
                board[i] = board_placer(i, 'clear', ' ')
                board[i+10] = board_placer(i+10, 'clear', ' ')
                board[i+20] = board_placer(i+20, 'clear', ' ')
                if player == 'human':
                    return 1
                elif player == 'comp':
                    return 2
            
    # Up-right diagonal
    for row in [72,63,54,45,36,27,18]:
        for i in range(row,row+7):
            if (board[i].strip() == board[i-8].strip() == board[i-16].strip()) and board[i].strip() in [sign]:
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
