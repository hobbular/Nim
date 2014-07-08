import random

#############################################
# My variables for my game
#############################################
board = [['|','|','|','|','|'],
         ['|','|','|','|'],
         ['|','|','|'],
         ['|','|']]

human_move = True    # this is how we'll track whose turn it is

#############################################
# Displays the current state of the board
#############################################
def display_board(board):
    space_count = 0
    for line in board:
        print (space_count*' '),
        for item in line:
            print item,
        print
        space_count += 1

#############################################
# Changes the board based on the chosen move.
# If the move was illegal, returns False.
#############################################
def make_move(board,pile,count):
    if not '|' in board[pile] or count == 0:
        # tried to take sticks from an empty pile
        return False
    # remove UP TO count sticks from pile
    removed = 0
    index = 0
    while removed < count and '|' in board[pile]:
        # find a stick to remove
        while board[pile][index] != '|':
            index += 1
        # remove it
        board[pile][index] = ' '
        removed += 1
    return True

#############################################
# PLAY THE GAME!!
#############################################
while '|' in board[0] or '|' in board[1] or '|' in board[2] or '|' in board[3]:
    display_board(board)

    # if it's the human's turn:
    while human_move:
        pile_num = int(raw_input("pick a pile 1-4: "))
        while pile_num < 1 or pile_num > 4:
            pile_num = int(raw_input("that's not one of the options: "))
        how_many = int(raw_input("how many sticks: "))
        while how_many < 1:
            how_many = int(raw_input("nice try. gotta pick up at least one: "))
        pile_num -= 1
        success = make_move(board,pile_num,how_many)
        if success:
            break
        print "You can't remove sticks from an empty pile!"
    
    # if it's the computer's turn:
    while not human_move:
        ###########################################
        # TODO: MAKE THE COMPUTER CHOOSE A MOVE
        ###########################################
        pile_num = random.randint(0,3)
        how_many = random.randint(1,5)
        success = make_move(board,pile_num,how_many)
        if success:
            print "Computer removed",how_many,"sticks from pile",pile_num+1
            break

    # switch whose turn it is
    human_move = not human_move

#############################################
# WHO WON???
#############################################
if human_move:
    # the computer had the last move and picked up the last stick
    print "You win!"
else:
    # you had to pick up the last stick
    print "You lose!"
